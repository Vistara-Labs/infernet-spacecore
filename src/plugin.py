from concurrent import futures
import sys
import time
import asyncio
import grpc
import logging
import subprocess

from grpc_health.v1.health import HealthServicer
from grpc_health.v1 import health_pb2, health_pb2_grpc

from main import NodeLifecycle
from proto import sc_pb2
from proto import sc_pb2_grpc

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class ScPluginServicer(sc_pb2_grpc.ScPluginServicer):
    """Implementation of SC Plugin service."""

    def Start(self, request, context):
        print("Start request received")

        node = NodeLifecycle()
        node.on_startup()
        node.lifecycle_main()

        return sc_pb2.StartResponse()

    def Stop(self, request, context):
        print("Stop request received")
        return sc_pb2.StopResponse()

    def Logs(self, request, context):
        print("Logs request received")
        return sc_pb2.LogsResponse()

    def Status(self, request, context):
        print("Status request received")
        return sc_pb2.StatusResponse()

async def serve():
    logger.info("Starting Anvil...")
    anvil_log = open("/tmp/anvil.log", "w")
    anvil_proc = subprocess.Popen(
        ["anvil", "--fork-url", "https://eth-mainnet.g.alchemy.com/v2/CygH7Y6PEyNCuKF6NFcG6DxYRXqI4zE2"],
        stdout=anvil_log, stderr=anvil_log
    )

    # Start Redis
    logger.info("Starting Redis server...")
    redis_log = open("/tmp/redis.log", "w")
    redis_proc = subprocess.Popen(["redis-server"], stdout=redis_log, stderr=redis_log)

    # We need to build a health service to work with go-plugin
    health = HealthServicer()
    health.set("plugin", health_pb2.HealthCheckResponse.ServingStatus.Value('SERVING'))

    # Start the server.
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    sc_pb2_grpc.add_ScPluginServicer_to_server(ScPluginServicer(), server)
    health_pb2_grpc.add_HealthServicer_to_server(health, server)
    server.add_insecure_port('[::]:1234')
    await server.start()

    # Output information
    logger.info("1|1|tcp|0.0.0.0:1234|grpc")
    sys.stdout.flush()

    try:
        await server.wait_for_termination()
    except KeyboardInterrupt:
        await server.stop(0)
        anvil_proc.kill()
        redis_proc.kill()

if __name__ == '__main__':
    # serve()
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(serve())
    loop.close()
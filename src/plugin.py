# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

from concurrent import futures
import sys
import time

import grpc


from grpc_health.v1.health import HealthServicer
from grpc_health.v1 import health_pb2, health_pb2_grpc

from main import NodeLifecycle
from proto import sc_pb2
from proto import sc_pb2_grpc

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

def serve():
    # We need to build a health service to work with go-plugin
    health = HealthServicer()
    health.set("plugin", health_pb2.HealthCheckResponse.ServingStatus.Value('SERVING'))

    # Start the server.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # kv_pb2_grpc.add_KVServicer_to_server(KVServicer(), server)

    sc_pb2_grpc.add_ScPluginServicer_to_server(ScPluginServicer(), server)

    health_pb2_grpc.add_HealthServicer_to_server(health, server)
    server.add_insecure_port('0.0.0.0:1234')
    server.start()

    # Output information
    print("1|1|tcp|0.0.0.0:1234|grpc")
    sys.stdout.flush()

    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
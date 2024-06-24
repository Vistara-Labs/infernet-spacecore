# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import sc_pb2 as sc__pb2

# import sc_pb2 as sc__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in sc_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ScPluginStub(object):
    """I want to have start, stop, logs, and status for running plugins

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Start = channel.unary_unary(
                '/proto.ScPlugin/Start',
                request_serializer=sc__pb2.StartRequest.SerializeToString,
                response_deserializer=sc__pb2.StartResponse.FromString,
                _registered_method=True)
        self.Stop = channel.unary_unary(
                '/proto.ScPlugin/Stop',
                request_serializer=sc__pb2.StopRequest.SerializeToString,
                response_deserializer=sc__pb2.StopResponse.FromString,
                _registered_method=True)
        self.Logs = channel.unary_unary(
                '/proto.ScPlugin/Logs',
                request_serializer=sc__pb2.LogsRequest.SerializeToString,
                response_deserializer=sc__pb2.LogsResponse.FromString,
                _registered_method=True)
        self.Status = channel.unary_unary(
                '/proto.ScPlugin/Status',
                request_serializer=sc__pb2.StatusRequest.SerializeToString,
                response_deserializer=sc__pb2.StatusResponse.FromString,
                _registered_method=True)


class ScPluginServicer(object):
    """I want to have start, stop, logs, and status for running plugins

    """

    def Start(self, request, context):
        """I want to have start, stop, logs, and status for running plugins
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stop(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Logs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ScPluginServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=sc__pb2.StartRequest.FromString,
                    response_serializer=sc__pb2.StartResponse.SerializeToString,
            ),
            'Stop': grpc.unary_unary_rpc_method_handler(
                    servicer.Stop,
                    request_deserializer=sc__pb2.StopRequest.FromString,
                    response_serializer=sc__pb2.StopResponse.SerializeToString,
            ),
            'Logs': grpc.unary_unary_rpc_method_handler(
                    servicer.Logs,
                    request_deserializer=sc__pb2.LogsRequest.FromString,
                    response_serializer=sc__pb2.LogsResponse.SerializeToString,
            ),
            'Status': grpc.unary_unary_rpc_method_handler(
                    servicer.Status,
                    request_deserializer=sc__pb2.StatusRequest.FromString,
                    response_serializer=sc__pb2.StatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.ScPlugin', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('proto.ScPlugin', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ScPlugin(object):
    """I want to have start, stop, logs, and status for running plugins

    """

    @staticmethod
    def Start(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.ScPlugin/Start',
            sc__pb2.StartRequest.SerializeToString,
            sc__pb2.StartResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Stop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.ScPlugin/Stop',
            sc__pb2.StopRequest.SerializeToString,
            sc__pb2.StopResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Logs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.ScPlugin/Logs',
            sc__pb2.LogsRequest.SerializeToString,
            sc__pb2.LogsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.ScPlugin/Status',
            sc__pb2.StatusRequest.SerializeToString,
            sc__pb2.StatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
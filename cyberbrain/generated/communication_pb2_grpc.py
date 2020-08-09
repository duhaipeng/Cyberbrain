# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import communication_pb2 as communication__pb2


class CommunicationStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SyncState = channel.unary_stream(
                '/Communication/SyncState',
                request_serializer=communication__pb2.State.SerializeToString,
                response_deserializer=communication__pb2.State.FromString,
                )
        self.FindFrames = channel.unary_unary(
                '/Communication/FindFrames',
                request_serializer=communication__pb2.CursorPosition.SerializeToString,
                response_deserializer=communication__pb2.FrameLocaterList.FromString,
                )
        self.GetFrame = channel.unary_unary(
                '/Communication/GetFrame',
                request_serializer=communication__pb2.FrameLocater.SerializeToString,
                response_deserializer=communication__pb2.Frame.FromString,
                )


class CommunicationServicer(object):
    """Interface exported by the server.
    """

    def SyncState(self, request, context):
        """Sync state between client and server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindFrames(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFrame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommunicationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SyncState': grpc.unary_stream_rpc_method_handler(
                    servicer.SyncState,
                    request_deserializer=communication__pb2.State.FromString,
                    response_serializer=communication__pb2.State.SerializeToString,
            ),
            'FindFrames': grpc.unary_unary_rpc_method_handler(
                    servicer.FindFrames,
                    request_deserializer=communication__pb2.CursorPosition.FromString,
                    response_serializer=communication__pb2.FrameLocaterList.SerializeToString,
            ),
            'GetFrame': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFrame,
                    request_deserializer=communication__pb2.FrameLocater.FromString,
                    response_serializer=communication__pb2.Frame.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Communication', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Communication(object):
    """Interface exported by the server.
    """

    @staticmethod
    def SyncState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Communication/SyncState',
            communication__pb2.State.SerializeToString,
            communication__pb2.State.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindFrames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Communication/FindFrames',
            communication__pb2.CursorPosition.SerializeToString,
            communication__pb2.FrameLocaterList.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFrame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Communication/GetFrame',
            communication__pb2.FrameLocater.SerializeToString,
            communication__pb2.Frame.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
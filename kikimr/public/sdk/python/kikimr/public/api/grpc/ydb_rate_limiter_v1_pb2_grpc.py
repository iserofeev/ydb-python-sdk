# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from kikimr.public.api.protos import ydb_rate_limiter_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2


class RateLimiterServiceStub(object):
    """Service that implements distributed rate limiting.

    To use rate limiter functionality you need an existing coordination node.

    Control plane API
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateResource = channel.unary_unary(
                '/Ydb.RateLimiter.V1.RateLimiterService/CreateResource',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.CreateResourceRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.CreateResourceResponse.FromString,
                )
        self.AlterResource = channel.unary_unary(
                '/Ydb.RateLimiter.V1.RateLimiterService/AlterResource',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.AlterResourceRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.AlterResourceResponse.FromString,
                )
        self.DropResource = channel.unary_unary(
                '/Ydb.RateLimiter.V1.RateLimiterService/DropResource',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.DropResourceRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.DropResourceResponse.FromString,
                )
        self.ListResources = channel.unary_unary(
                '/Ydb.RateLimiter.V1.RateLimiterService/ListResources',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.ListResourcesRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.ListResourcesResponse.FromString,
                )
        self.DescribeResource = channel.unary_unary(
                '/Ydb.RateLimiter.V1.RateLimiterService/DescribeResource',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.DescribeResourceRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.DescribeResourceResponse.FromString,
                )
        self.AcquireResource = channel.unary_unary(
                '/Ydb.RateLimiter.V1.RateLimiterService/AcquireResource',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.AcquireResourceRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.AcquireResourceResponse.FromString,
                )


class RateLimiterServiceServicer(object):
    """Service that implements distributed rate limiting.

    To use rate limiter functionality you need an existing coordination node.

    Control plane API
    """

    def CreateResource(self, request, context):
        """Create a new resource in existing coordination node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AlterResource(self, request, context):
        """Update a resource in coordination node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DropResource(self, request, context):
        """Delete a resource from coordination node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListResources(self, request, context):
        """List resources in given coordination node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeResource(self, request, context):
        """Describe properties of resource in coordination node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AcquireResource(self, request, context):
        """Take units for usage of a resource in coordination node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RateLimiterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateResource': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateResource,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.CreateResourceRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.CreateResourceResponse.SerializeToString,
            ),
            'AlterResource': grpc.unary_unary_rpc_method_handler(
                    servicer.AlterResource,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.AlterResourceRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.AlterResourceResponse.SerializeToString,
            ),
            'DropResource': grpc.unary_unary_rpc_method_handler(
                    servicer.DropResource,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.DropResourceRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.DropResourceResponse.SerializeToString,
            ),
            'ListResources': grpc.unary_unary_rpc_method_handler(
                    servicer.ListResources,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.ListResourcesRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.ListResourcesResponse.SerializeToString,
            ),
            'DescribeResource': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeResource,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.DescribeResourceRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.DescribeResourceResponse.SerializeToString,
            ),
            'AcquireResource': grpc.unary_unary_rpc_method_handler(
                    servicer.AcquireResource,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.AcquireResourceRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.AcquireResourceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Ydb.RateLimiter.V1.RateLimiterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RateLimiterService(object):
    """Service that implements distributed rate limiting.

    To use rate limiter functionality you need an existing coordination node.

    Control plane API
    """

    @staticmethod
    def CreateResource(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.RateLimiter.V1.RateLimiterService/CreateResource',
            kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.CreateResourceRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.CreateResourceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AlterResource(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.RateLimiter.V1.RateLimiterService/AlterResource',
            kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.AlterResourceRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.AlterResourceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DropResource(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.RateLimiter.V1.RateLimiterService/DropResource',
            kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.DropResourceRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.DropResourceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListResources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.RateLimiter.V1.RateLimiterService/ListResources',
            kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.ListResourcesRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.ListResourcesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeResource(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.RateLimiter.V1.RateLimiterService/DescribeResource',
            kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.DescribeResourceRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.DescribeResourceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AcquireResource(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.RateLimiter.V1.RateLimiterService/AcquireResource',
            kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.AcquireResourceRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_ydb__rate__limiter__pb2.AcquireResourceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

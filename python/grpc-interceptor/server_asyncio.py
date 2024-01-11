"""The Python AsyncIO implementation of the GRPC helloworld.Greeter server."""

import asyncio
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


from auth_interceptor import AuthenJwtInterceptor, token_cvar

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    async def SayHello(
        self,
        request: helloworld_pb2.HelloRequest,
        context: "grpc.aio.ServicerContext",
    ) -> helloworld_pb2.HelloReply:
        logging.info(
            "Handle rpc with id %s in server handler.", token_cvar.get()
        )
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)


async def serve() -> None:
    interceptors = [
        AuthenJwtInterceptor(),
    ]

    server = grpc.aio.server(interceptors=interceptors)
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    listen_addr = "[::]:8000"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
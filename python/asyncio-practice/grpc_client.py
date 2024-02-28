import asyncio

import grpc.aio
from grpc_health.v1 import health_pb2, health_pb2_grpc


async def main():

    channel = grpc.aio.insecure_channel("0.0.0.0:50050")
    stub = health_pb2_grpc.HealthStub(channel)

    response = await stub.Check(
        health_pb2.HealthCheckRequest()
    )
    print(response)
    await channel.close()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())



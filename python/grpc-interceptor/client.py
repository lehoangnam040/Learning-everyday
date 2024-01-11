import grpc
import helloworld_pb2
import helloworld_pb2_grpc


channel = grpc.insecure_channel("0.0.0.0:8000")
stub = helloworld_pb2_grpc.GreeterStub(channel)

resp = stub.SayHello(
    helloworld_pb2.HelloRequest(name="namlh"),
    metadata=(("authorization", f"sadf12431241234213123"), ),
)
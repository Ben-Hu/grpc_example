import os
import sys

import grpc
from hello import hello_pb2, hello_pb2_grpc


def request(name):
    greeter_service = os.environ.get("GREETER_SERVICE", "localhost:50051")
    with grpc.insecure_channel(greeter_service) as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name=name))
    print(response)


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else None
    request(name)

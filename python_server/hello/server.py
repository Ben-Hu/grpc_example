import logging
import sys
from concurrent import futures

import grpc
import hello_pb2
import hello_pb2_grpc

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def greeting(name):
    return f"Hello {name}"


class GreeterServicer(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        logging.info(f"greeting {request.name}")
        message = greeting(request.name)
        return hello_pb2.HelloReply(message=message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.info("server started")
    serve()

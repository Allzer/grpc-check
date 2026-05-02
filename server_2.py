import grpc
from concurrent import futures
import time
import proto_pb2
import proto_pb2_grpc

class SquaringService():
    def SquaringNumber(self, request, context):
        return proto_pb2.SquaringResponse(squaring_number=request.number**2)
    
    def CubeOfNumbers(self, request, context):
        return proto_pb2.SquaringResponse(squaring_number=request.number**3)
    
def server2():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto_pb2_grpc.add_SquaringServicer_to_server(SquaringService(), server)
    server.add_insecure_port('[::]:10000')
    server.start()
    print("server2 started")
    
    try:
        while True:
            time.sleep(60*60)
    except KeyboardInterrupt:
        server.stop(0)
    
if __name__ == '__main__':
    server2()
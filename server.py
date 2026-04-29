import grpc
from concurrent import futures
import time
import proto_pb2
import proto_pb2_grpc

class GreeterServicer(): #процедура которую мы будем вызывать
    def SayHello(self, request):
        return proto_pb2.HelloResponse(message=f"Hello, {request.name}!")
    
def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server) #Добавляем процедуру в grpc сервер  
    server.add_insecure_port('[::]:50051') #Указываем порт на котором стартует сервер
    server.start()
    print("server started")
    
    try:
        while True:
            time.sleep(60*60)
    except KeyboardInterrupt:
        server.stop(0)
        
if __name__ == "__main__":
    server( )
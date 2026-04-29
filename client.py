import grpc

import proto_pb2
import proto_pb2_grpc

def run():
    chanel = grpc.insecure_channel("localhost:50051") #подключаемся к каналу
    stub = proto_pb2_grpc.GreeterStub(chanel) #вызываем процедуру
    response = stub.SayHello(proto_pb2.HelloRequest(name="World"))
    print(f"Клиент получил ответ: {response.message}")
    
if __name__ == "__main__":
    run()
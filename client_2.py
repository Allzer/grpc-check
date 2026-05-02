import random
import grpc
import proto_pb2
import proto_pb2_grpc

def run():
    chanel = grpc.insecure_channel('localhost:10000')
    stub = proto_pb2_grpc.SquaringStub(chanel)
    goal_number = random.randint(0, 10)
    response = stub.SquaringNumber(proto_pb2.SquaringRequest(number=goal_number))
    response_2 = stub.CubeOfNumbers(proto_pb2.SquaringRequest(number=goal_number))
    print(f'Квадрат числа {goal_number} = {response.squaring_number}')
    print(f'Куб числа {goal_number} = {response_2.squaring_number}')
    
if __name__ == '__main__':
    run()
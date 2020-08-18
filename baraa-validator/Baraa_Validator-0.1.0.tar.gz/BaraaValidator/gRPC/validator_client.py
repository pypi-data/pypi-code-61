import os
import grpc
import __transactionValidator_pb2_grpc as transactionValidator_pb2_grpc, __transactionValidator_pb2 as transactionValidator_pb2
import sys
def run():
    transFile ="";
    if( len(sys.argv)>1 ):
        transFile=sys.argv[1];

    channel = grpc.insecure_channel('localhost:50051')
    stub = transactionValidator_pb2_grpc.TransactionValidatorServiceStub(channel)
    try:
        response = stub.validateTransactionFile(transactionValidator_pb2.transactionFile(transactionFile=transFile))
        isValid = response.isValid
        print(isValid)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        channel.unsubscribe(close)
        exit()

def close(channel):
    "Close the channel"
    channel.close()
if __name__ == "__main__":
    run()
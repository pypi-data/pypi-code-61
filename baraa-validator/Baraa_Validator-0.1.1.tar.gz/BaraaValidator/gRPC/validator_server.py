from concurrent import futures
import grpc
import __transactionValidator_pb2 as transactionValidator_pb2, __transactionValidator_pb2_grpc as transactionValidator_pb2_grpc
from BaraaValidator.transactionValidators import validateTransactionsFile

class TransactionValidatorService(transactionValidator_pb2_grpc.TransactionValidatorServiceServicer):
    def validateTransactionFile(self, request, context):
        return transactionValidator_pb2.isValid(isValid=(validateTransactionsFile(request.transactionFile)))
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transactionValidator_pb2_grpc.add_TransactionValidatorServiceServicer_to_server(TransactionValidatorService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
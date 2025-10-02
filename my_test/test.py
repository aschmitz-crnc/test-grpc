import my_test.test_pb2 as test_pb2
import my_test.test_pb2_grpc as test_pb2_grpc

class CrgServiceImpl(launcher_pb2_grpc.CrgService):
    def __init(self):
        pass

    def Test(self, request, response):
        print("Serving Test request")
        return test_pb2.TestResponse()

def __main__():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_service_impl = TestServiceImpl()
    test_pb2_grpc.add_TestServiceServicer_to_server(test_service_impl, server)
    server.add_insecure_port(f"0.0.0.0:12345")
    server.start()

if __name__ == '__main__':
    sys.exit(__main__())

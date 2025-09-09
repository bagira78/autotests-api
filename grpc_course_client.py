import grpc

import course_service_pb2
import course_service_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

request = course_service_pb2.GetCourseRequest(course_id="api-course")
response = stub.GetCourse(request)

# print(f"course_id: \"{response.course_id}\"")
# print(f"title: \"{response.title}\"")
# print(f"description: \"{response.description}\"")

print(response)

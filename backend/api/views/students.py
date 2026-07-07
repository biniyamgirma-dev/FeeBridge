from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from students.models import Student
from api.serializers.students import StudentSerializer
from api.permissions import IsStaffOrAdmin, IsAdmin


class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsStaffOrAdmin]


class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAdmin()]
        return [IsStaffOrAdmin()]
from rest_framework import viewsets
from apps.base.models import Student
from apps.base.api.serializers.student import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "uuid"
from rest_framework import serializers # type: ignore
from api.models import Company,Employee, Faculty


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields ='__all__' 

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()

    class Meta:
        model=Employee
        fields="__all__"

class FacultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Faculty
        fields="__all__"

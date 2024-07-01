from django.shortcuts import render,redirect
from rest_framework import viewsets
from api.models import Company,Employee, Faculty
from api.serializers import CompanySerializer,EmployeeSerializer, FacultySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .forms import LoginPage
from django.contrib.auth import authenticate, login
# Create your views here.




class CompanyViewSet(viewsets.ModelViewSet):

    queryset= Company.objects.all()
    serializer_class = CompanySerializer

    #companies/{company_id}/employees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            print("Methods gets exectuted")
            emps=Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
            pass
        except Exception as e:
            print(e)
            return ResourceWarning({
                'message':e
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    serializer_class = EmployeeSerializer


class FacutlyViewSet(viewsets.ModelViewSet):
    queryset= Faculty.objects.all()
    serializer_class = FacultySerializer



def login_page(request):
    form = LoginPage()
    if request.method == 'POST':
        form = LoginPage(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('companies')  # Redirect to your desired page
            else:
                form.add_error(None, 'Invalid username or password')
    return render(request, 'myapp/login.html', {'form': form})

def faculty(request):
    pass
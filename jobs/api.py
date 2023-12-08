from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import JobListSerializer, JobDetailSerializer,CompanySerializer,CategorySerializer

from .models import Job , Category, Company


class JobListAPI(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['agency', 'category','salary']
    search_fields = ['title', 'nature','location']
    ordering_fields = ['salary']
    
class JobDetailAPI(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobDetailSerializer
class CompanyAPI(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
class CategoryAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
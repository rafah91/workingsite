from django.urls import path
from .views import JobList, JobDetail, CategoryList
from .api import JobListAPI,JobDetailAPI,CategoryAPI,CompanyAPI


urlpatterns = [
     path('', JobList.as_view()),
     path('<slug:slug>', JobDetail.as_view()),
     path('Categories/',CategoryList.as_view()),
     
     
    #API
    path('api/list',JobListAPI.as_view()),
    path('api/list/<int:pk>' , JobDetailAPI.as_view()),
    path('api/list/category',CategoryAPI.as_view()),
]
 
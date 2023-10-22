from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

NATURE_TYPES=(('Full Time','Full Time'),('Part Time','Part Time'),('Remote','Remote'),('Freelance','Freelance'),)
# Create your models here.
class Job(models.Model):
    title=models.CharField(max_length=120)
    category=models.ForeignKey('Category',related_name='job_category',on_delete=models.SET_NULL,null=True,blank=True)
    agency=models.ForeignKey('Company',related_name='job_company',on_delete=models.SET_NULL,null=True,blank=True)
    lacation=models.CharField(max_length=120)
    salary=models.FloatField()
    created_at=models.DateTimeField(default=timezone.now)
    vacancy=models.IntegerField()
    nature=models.CharField(max_length=20,choices=NATURE_TYPES)
    application_date=models.DateField()
    description=models.TextField(max_length=50000)
    knowledge_requirements=models.TextField(max_length=10000)
    education_experience=models.TextField(max_length=10000)
    slug=models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) 
        super(Job, self).save(*args, **kwargs)
    
class Category:
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to='categories')
    job_count=models.IntegerField(max_length=10000)
    slug=models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
    
class Company:
    name=models.CharField(max_length=120)
    logo=models.ImageField(upload_to='campany')
    presentation=models.TextField(max_length=10000)
    website=models.TextField(max_length=300)
    email=models.TextField(max_length=300)
    slug=models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)   
        super(Company, self).save(*args, **kwargs)
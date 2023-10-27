import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random 
from jobs.models import Company,Category, Job

def add_companies(n):
    images=['1.png','2.png','3.png','4.png','5.png','6.png']
    fake=Faker()
    for n in range(n):
        Company.objects.create(
            name=fake.name(),
            logo=f"companies/{images[random.randint(0,5)]}",
            presentation=fake.text(),
            website=fake.domain_name(),
            email=fake.ascii_email(),
        )
        
def add_categories(n):
    images=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png']
    fake=Faker()
    for n in range(n):
        Category.objects.create(
            name=fake.name(),
            image=f"categories/{images[random.randint(0,9)]}",
            job_count=random.randint(0,10),
        
        )
        
def add_job(n):
   fake=Faker()
   for n in range(n):
        Job.objects.create(
            title=fake.name(),
            location=fake.city()
            salary=random.randint(500,3000)
            created_at=fake.date_this_month(),
            vacancy=random.randint(0,10),
            nature=
            application_date=fake.datetime(),
            description=fake.text(),
            knowledge_requirements=fake.text(),
            education_experience=fake.text(),
            
        )
        
        
#add_companies(6)
#add_categories(10)
add_job(10)

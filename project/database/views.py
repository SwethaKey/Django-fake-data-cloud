from django.shortcuts import render
from .models import Persons
from faker import Faker
# Create your views here.

fake = Faker()

def generate_fake_data(request):
    # Specify the number of fake data entries you want to create
    num_entries = 10

    for _ in range(num_entries):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        address = fake.address()
        city = fake.city()

        #create and save the Person instance
        person = Persons(first_name=first_name, last_name=last_name, email=email, address=address, city=city)
        person.save()
    
    return render(request, 'database/success.html')

def home(request):
    return render(request, 'database/home.html') 
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','community.settings')

import django

django.setup()

import random
from users.models import User, File
from faker import Faker


fakegen = Faker()

users = ['Peter', 'Stewie', 'Joe', 'Chris']

def add_user():
    user = User.objects.get_or_create(username=random.choice(users), email=fakegen.email())[0]
    user.save()
    return user

def populate(N=10):
    for i in range(N):
        user = add_user()
        fake_filename = fakegen.file_name()
        fake_date = fakegen.date()
        fake_url = fakegen.url()

        file = File.objects.get_or_create(owner=user, filename=fake_filename, date=fake_date, url=fake_url)

if __name__ == '__main__':
    populate(10)

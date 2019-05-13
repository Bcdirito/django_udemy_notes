import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django
django.setup()

from AppTwo.models import User

from faker import Faker

faker_gen = Faker()

def add_user():
    split_name = faker_gen.name().split()
    email = faker_gen.email()
    u = User.objects.get_or_create(first_name=split_name[0], last_name=split_name[1], email=email)[0]
    u.save()
    return u

def populate(N=5):
    for entry in range(N):
        usr = add_user()

if __name__ == "__main__":
    print("Populating Data")
    populate(20)
    print("Populated Data")



import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django
django.setup()

import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

faker_gen = Faker()
topics = ["Search", "Social", "Marketplace", "News", "Games"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    # is a tuple, so you want to use the first index
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # Create the Fake Data
        fake_url = faker_gen.url()
        fake_date = faker_gen.date()
        fake_name = faker_gen.company()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == "__main__":
    print("populating script!")
    populate(20)
    print("populating complete!")
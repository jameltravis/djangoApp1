"""Use Faker to populate DB with...you guessed it: fake data"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")
import random
import django
django.setup()
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker


fakegen = Faker()
topics = ["Search", "Social", "Marketplace", "News", "Games"]

def add_topic():
    """add new topic"""
    topi = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    topi.save()
    return topi

def populate(N=5):
    """creates our fake data"""

    # Create the fake data for that entry
    for entry in range(N):
        
        # get the topic for the entry
        top = add_topic()

        # Create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create a fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == "__main__":
    print("population script!")
    populate(20)
    print("Populating ...")

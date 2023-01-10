import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meter.settings")
import django
django.setup()

from faker import factory, Faker
from api.models import *
from model_bakery.recipe import Recipe, foreign_key

fake = Faker()

for i in range(100):
    meter = Recipe(Meter,
                   label=fake.name())
    meterdata = Recipe(MeterData,
                       meter_id=foreign_key(meter),
                       value= fake.random_number(fix_len=5),
                       timestamp=fake.future_datetime(end_date='+30d', tzinfo=None))
    meter.make()
    meterdata.make()

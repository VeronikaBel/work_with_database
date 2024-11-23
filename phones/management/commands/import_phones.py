import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.DictReader(csvfile, delimiter=';')
            next(phone_reader)

            for line in phone_reader:
                phone = Phone (
                    name = line['name'],
                    price = float(line['price']),
                    image = line['image'],
                    release_date = line['release_date'],
                    lte_exists = bool(line['lte_exists'])
                )
                
                phone.save()
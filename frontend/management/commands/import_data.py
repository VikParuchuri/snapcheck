import csv
from django.core.management.base import BaseCommand, CommandError
from api.models import PhoneRecord

class Command(BaseCommand):
    args = '<path>'
    help = 'Import phone records from csv.'

    def handle(self, *args, **options):
        path = args[0]
        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = PhoneRecord.objects.get_or_create(
                    phone_number=row[0],
                    username=row[1],
                    location=row[2]
                    )




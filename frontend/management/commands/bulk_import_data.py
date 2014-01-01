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
            records = []
            for row in reader:
                record = PhoneRecord(
                    phone_number=row[0],
                    username=row[1],
                    location=row[2]
                    )
                records.append(record)

                if len(records) > 100:
                    PhoneRecord.objects.bulk_create(records)
                    records = []
            PhoneRecord.objects.bulk_create(records)




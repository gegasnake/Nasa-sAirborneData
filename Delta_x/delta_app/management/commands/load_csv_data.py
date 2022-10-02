from django.core.management import BaseCommand
import csv
from ...models import Data


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        file_path = options['file']

        with open(file_path, 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)
            for row in csvreader:
                Data.objects.create(
                    id=row[1],
                    season=row[2],
                    latitude=row[3],
                    longitude=row[4],
                    date=row[5],
                    time=row[6],
                    turbidity=row[8],
                    salinity=row[10],
                    temperature=row[12],
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded data'))

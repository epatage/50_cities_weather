import csv

from django.core.management.base import BaseCommand

from cities.models import City

OBJECTS_LIST = {
    "Города": City,
}


def clear_data(self):
    for key, value in OBJECTS_LIST.items():
        value.objects.all().delete()
        self.stdout.write(
            self.style.WARNING(f'Существующие записи "{key}" были удалены.')
        )


class Command(BaseCommand):
    help = "Загружает CSV данные из файла data/cities.csv"

    def add_arguments(self, parser):
        parser.add_argument(
            "--delete-existing",
            action="store_true",
            dest="delete_existing",
            default=False,
            help="Удаляет существующие данные, записанные ранее",
        )

    def handle(self, *args, **options):

        if options["delete_existing"]:
            clear_data(self)

        records = []
        with open(
                "./data/cities.csv",
                encoding="utf-8",
                newline=""
        ) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                record = City(
                    name=row["name"], country=row["country"]
                )
                records.append(record)

        City.objects.bulk_create(records)
        self.stdout.write(self.style.SUCCESS(
            'Все записи "Городов" сохранены'
        ))

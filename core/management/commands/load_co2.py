from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load data from CO2 file'

    def handle(self, *args, **kwargs):
        raise NotImplementedError
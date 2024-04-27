import os
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    """very simple command for coverage"""
    def handle(self, *args, **options):
        os.system("coverage run --source='.' manage.py test")
        os.system("coverage report")


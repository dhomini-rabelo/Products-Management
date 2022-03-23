from pathlib import Path
from ..comand import BasicCommand
from django.conf import settings
import requests
import io

    

class Command(BasicCommand):

    help = 'Compact html file losing extends django command'

    def add_arguments(self, parser):
        parser.add_argument('html_path', type=str)

    def handle(*args, **options):
        base_path = f'{settings.BASE_DIR}/frontend/templates'
        path = f'{base_path}/{options["html_path"].replace(".", "/")}.html'

        with io.open(path, 'r') as file:
            reading_list = file.readlines()
            reading = file.read()

        first_line = reading_list[0].strip()
        if first_line.startswith((r'{% extends', r'{%extends')):
            html_base_archive_path = first_line.split("'")[1]
            html_base_path = f'{base_path}/{html_base_archive_path}'
            with io.open(html_base_path, 'r') as file:
                reading_base_list = file.readlines()
                reading_base = file.read()
            for i, line in enumerate(reading_base_list):
                if r'{% block' in line:
                    start = line.index(r'{% block') + 1
            



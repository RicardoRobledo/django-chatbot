from django.shortcuts import render
from django.conf import settings
from pathlib import Path

from .utils.cleaners import clean_data
from .utils import csv_handlers


__author__ = 'Ricardo'
__version__ = '0.1'


def index(request):

    path = f'{settings.PATH_CSV_FILE}urls.csv'
    archivo = Path(path)

    # checking out if .csv file exists
    if archivo.is_file():
        csv_handlers.read_csv(path)
    else:
        csv_handlers.create_csv(path)

    return render(request, 'frontend/index.html')

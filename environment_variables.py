import os
from dotenv import load_dotenv
from pathlib import Path

path = Path(__file__).resolve().parent / '.env'

load_dotenv(path)

DJANGO_SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
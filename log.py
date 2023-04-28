import os


def log(message):
    region = os.environ.get('TEST')
    print(f'Logging: {message} - {region}')

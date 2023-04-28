import os


def log(message):
    region = os.environ.get('us-east-1')
    print(f'Logging: {message} - {region}')

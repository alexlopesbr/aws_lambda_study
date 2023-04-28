import os


def log(message):
    variable = os.environ['TEST_VARIABLE']
    print(f'Logging: {message} - {variable}')

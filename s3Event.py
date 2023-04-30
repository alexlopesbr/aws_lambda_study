class S3Event:
    '''
        Represents an S3 even.
    '''
    def __init__(self, records):
        self.records = records


class S3Record:
    def __init__(self, s3, **kwargs):
        self.s3 = S3(**s3)


class S3:
    def __init__(self, bucket, object, **kwargs):
        self.bucket = Bucket(**bucket)
        self.object = Object(**object)


class Bucket:
    def __init__(self, name, **kwargs):
        self.name = name


class Object:
    def __init__(self, key, **kwargs):
        self.key = key

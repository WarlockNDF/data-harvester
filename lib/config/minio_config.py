
class MinioConfig:

    host: str | None = None
    access_key: str | None = None
    secret_key: str | None = None


    def __init__(self, host: str | None = None, access_key: str | None = None, secret_key: str | None = None):
        self.host = host
        self.access_key = access_key
        self.secret_key = secret_key
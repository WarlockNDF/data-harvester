

class MqttConfig:

    host: str = ""
    port: int = 1883
    username: str = ""
    password: str = ""

    def __init__(self, host: str, port: int, username: str, password: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def create(self, host: str, port: int, username: str, password: str):
        pass
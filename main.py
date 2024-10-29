import os
from dotenv import load_dotenv

from lib.storage import Storage
from lib.harvester import Harvester
from lib.config.mqtt_config import MqttConfig
from lib.config.minio_config import MinioConfig

def get_mqtt_config() -> MqttConfig:
    return MqttConfig(
        host = os.environ['MQTT_HOST'],
        port = int(os.environ['MQTT_PORT']),
        username = os.environ['MQTT_USERNAME'],
        password = os.environ['MQTT_PASSWORD']
    )

def get_minio_config() -> MinioConfig:
    return MinioConfig(
        host = os.environ['MINIO_HOST'],
        access_key = os.environ['MINIO_ACCESS_KEY'],
        secret_key = os.environ['MINIO_SECRET_KEY'],
    )


if __name__ == '__main__':
    load_dotenv()
    storage: Storage = Storage("harvest").with_local()
    harvester: Harvester = Harvester().define_storage(storage)
    harvester.define_mqtt(get_mqtt_config())
    harvester.connect()
    harvester.define_log_sub("test", extractor_key= "hello.world.foo")
    harvester.run()
import os
from dotenv import load_dotenv
from lib.storage import Storage
from lib.harvester import Harvester
from lib.config.mqtt_config import MqttConfig

def get_mqtt_config() -> MqttConfig:
    return MqttConfig(
        host = os.environ['MQTT_HOST'],
        port = int(os.environ['MQTT_PORT']),
        username = os.environ['MQTT_USERNAME'],
        password = os.environ['MQTT_PASSWORD']
    )

if __name__ == '__main__':
    load_dotenv()
    storage: Storage = Storage("harvest").with_local()
    harvester: Harvester = Harvester().define_storage(storage)
    harvester.define_mqtt(get_mqtt_config())
    harvester.define_image_sub(topic = "tester", extractor_key = "image")
    harvester.run_mqtt()
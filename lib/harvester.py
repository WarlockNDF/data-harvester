from typing import Self, Callable, Dict, Any

import uuid

import paho.mqtt.client as mqtt

from lib.storage import Storage
from lib.config.mqtt_config import MqttConfig


class Harvester:

    storage: Storage = None
    _mqtt = None

    def __init__(self):
        pass

    def define_storage(self, storage: Storage) -> Self:
        self.storage = storage
        return self

    def define_mqtt(self, config: MqttConfig) -> Self:
        self._mqtt = mqtt.Client(client_id= str(uuid.uuid4()), clean_session=False)
        return self

    def define_image_sub(self, topic: str, extractor_key: str):
        pass

    def __image_sub_handler(self, data: Dict[str, Any], extractor_key: str) -> str | bytes | None:
        nested_level = extractor_key.split('.')
        image = None
        for key in nested_level:
            image = data.get(key, None)
            if image is None: return None
        return image


    def run_mqtt(self):
        pass
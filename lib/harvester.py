from typing import Self, Callable, Dict, Any

import uuid

import json
import logging
import paho.mqtt.client as mqtt
from paho.mqtt.client import MQTTMessage

from lib.storage import Storage
from lib.config.mqtt_config import MqttConfig
from lib.utils import extract_key_data


class Harvester:

    storage: Storage = None
    __mqtt: mqtt.Client = None
    __mqtt_config: MqttConfig = None
    __connected = False

    def __init__(self):
        self.__log_on_connection_fail = None

    def define_storage(self, storage: Storage) -> Self:
        self.storage = storage
        return self

    def define_mqtt(self, config: MqttConfig) -> Self:
        self.__mqtt = mqtt.Client(client_id= str(uuid.uuid4()), clean_session=False, transport= "tcp", protocol= mqtt.MQTTv31)
        self.__mqtt.username_pw_set(username=config.username, password=config.password)
        self.__mqtt_config = config
        return self

    def define_image_sub(self, topic: str, extractor_key: str):
        pass

    def define_log_sub(self, topic: str, extractor_key: str = None) ->  Self:
        if not self.__connected: raise Exception("MQTT not connected");
        self.__mqtt.subscribe(topic, qos=1)
        self.__mqtt.message_callback_add(topic, lambda client, userdata, data: self.__log_topic_data(topic, client, userdata, data, extractor_key))
        return self

    @staticmethod
    def __log_topic_data(topic: str, client: mqtt.Client, _userdata: Any, data: MQTTMessage, extractor_key: str = ""):
        print("from topic ", topic, " receive")
        try:
            scope_data: Dict[str, Any] = json.loads(data.payload.decode("utf-8"))
            print(scope_data)
            result_data = extract_key_data(scope_data, extractor_key)
            print(result_data)
        except Exception as _:
            print(data.payload.decode("utf-8"))

    def connect(self) -> Self:
        logging.basicConfig(level=logging.DEBUG)
        self.__mqtt.enable_logger()
        self.__mqtt.connect(host= self.__mqtt_config.host, port=self.__mqtt_config.port)
        self.__connected = True
        return self

    def run(self):
        self.__mqtt.loop_forever()
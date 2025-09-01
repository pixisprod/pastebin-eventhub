import json

from aiokafka import AIOKafkaProducer

from . import EventPublisher


class AioPublisher(EventPublisher):
    def __init__(self, producer: AIOKafkaProducer):
        self.__producer = producer

    
    async def publish(self, topic, key, value):
        self.__producer.send_and_wait(
            topic=topic,
            key=key,
            value=value,
        )
import json

from aiokafka import AIOKafkaProducer


class AioProducer:
    def __init__(self, producer: AIOKafkaProducer):
        self.__producer = producer

    
    async def publish(self, topic: str, key: bytes, value: bytes):
        await self.__producer.send_and_wait(
            topic=topic,
            key=key,
            value=value,
        )
import json

from aiokafka import AIOKafkaConsumer, ConsumerRecord

from . import EventConsumer


class AioConsumer(EventConsumer):
    def __init__(
        self, 
        consumer: AIOKafkaConsumer,
        handlers: dict,
        to_check: str = 'event',
    ):
        self.__consumer = consumer
        self.__handlers = handlers
        self.__to_check = to_check


    async def __handle(self, msg: ConsumerRecord):
        decoded = json.loads(msg.value)
        handler = self.__handlers.get(decoded[self.__to_check])
        if not handler:
            print('')
        try:
            await handler(msg)
        except Exception as e:
            print(f'Error while trying to handle msg: {e}')


    async def consume(self):
        await self.__consumer.start()
        try:
            async for msg in self.__consumer:
                await self.__handle(msg)
        finally:
            await self.__consumer.stop()
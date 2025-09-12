import json
import asyncio
from typing import Callable, Awaitable

from aiokafka import AIOKafkaConsumer, ConsumerRecord
from aiokafka.errors import KafkaConnectionError


Handler = Callable[[ConsumerRecord], Awaitable[None]]


class AioConsumer:
    def __init__(
        self, 
        consumer: AIOKafkaConsumer,
        to_check: str = 'event',
    ):
        self.__consumer = consumer
        self.__handlers: dict = {}
        self.__to_check = to_check


    def handler(self, event: str):
        def decorator(func: Handler):
            self.__handlers[event] = func
            return func
        return decorator


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
        while True:
            try:
                await self.__consumer.start()
                break
            except KafkaConnectionError:
                print('Unable to connect to kafka, retrying in 5 seconds..')
                await asyncio.sleep(5)
        try:
            async for msg in self.__consumer:
                await self.__handle(msg)
        finally:
            await self.__consumer.stop()
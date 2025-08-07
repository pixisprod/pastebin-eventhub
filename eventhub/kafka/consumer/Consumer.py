from asyncio import AbstractEventLoop
from typing import Callable, Awaitable

from aiokafka import AIOKafkaConsumer, ConsumerRecord


class Consumer:
    def __init__(
        self,
        *topics: str,
        server: str,
        loop: AbstractEventLoop,
        group_id: int
    ):
        self.__consumer = AIOKafkaConsumer(
            *topics,
            group_id=group_id,
            loop=loop, 
            bootstrap_servers=server,
        )
    
    
    async def consume(self, consume_func: Callable[[ConsumerRecord], Awaitable[None]]) -> None:
        await self.__consumer.start()
        try:
            async for msg in self.__consumer:
                await consume_func(msg)
        finally:
            await self.__consumer.stop()

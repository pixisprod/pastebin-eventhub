from asyncio import AbstractEventLoop

from aiokafka import AIOKafkaProducer


class Producer:
    def __init__(
        self,
        loop: AbstractEventLoop,
        server: str,
    ):
        self.__producer = AIOKafkaProducer(loop=loop, bootstrap_servers=server)
    
    
    async def __aenter__(self):
        await self.__producer.start()
        return self

    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.__producer.stop()

    
    async def send(self, topic: str, message: bytes) -> None:
        await self.__producer.send(topic, message)
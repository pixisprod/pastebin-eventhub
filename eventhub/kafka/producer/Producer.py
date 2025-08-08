from asyncio import AbstractEventLoop

from aiokafka import AIOKafkaProducer


class Producer:
    def __init__(
        self,
        loop: AbstractEventLoop,
        server: str,
    ):
        self.__producer = AIOKafkaProducer(loop=loop, bootstrap_servers=server)
    

    async def start(self):
        await self.__producer.start()


    async def stop(self):
        await self.__producer.stop()

    
    async def send(self, topic: str, message: bytes) -> None:
        await self.__producer.send(topic, message)
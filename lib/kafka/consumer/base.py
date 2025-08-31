from abc import ABC, abstractmethod


class EventConsumer(ABC):
    @abstractmethod
    async def consume(self):
        raise NotImplementedError()
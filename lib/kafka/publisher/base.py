from abc import ABC, abstractmethod


class EventPublisher(ABC):
    @abstractmethod
    async def publish(self, topic: str, key: bytes, value: bytes) -> None:
        raise NotImplementedError()

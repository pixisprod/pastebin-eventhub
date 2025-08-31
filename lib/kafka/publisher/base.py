from abc import ABC, abstractmethod


class EventPublisher(ABC):
    @abstractmethod
    async def publish(self, topic: str, key: int, value: dict) -> None:
        raise NotImplementedError()

import json

from httpx import AsyncClient


class ConfluentSRClient:
    def __init__(self, server: str):
        self.__client = AsyncClient(base_url=server)


    async def close(self):
        await self.__client.aclose()


    async def register_schema(self, subject: str, schema: dict) -> int:
        r = await self.__client.post(
            url=f'/subjects/{subject}/versions',
            json={'schema': json.dumps(schema)}
        )
        r.raise_for_status()
        return r.json()['id']

    
    async def get_schema_by_id(self, schema_id: int) -> dict:
        r = await self.__client.get(f'/schemas/ids/{schema_id}')
        r.raise_for_status()
        return json.loads(r.json()['schema'])
    

    async def get_schema_id_by_subject(self, subject: str) -> int:
        r = await self.__client.get(f'/subjects/{subject}/versions/latest')
        r.raise_for_status()
        return r.json()['id']
import io
import struct
import json

import avro.schema
import avro.io

from eventhub.confluent.ConfluentSRClient import ConfluentSRClient


class AvroManager:
    def __init__(self, confluent_client: ConfluentSRClient):
        self.__confluent = confluent_client

    async def serialize(self, schema_id: int, record: dict) -> bytes:
        schema_dict = await self.__confluent.get_schema_by_id(schema_id=schema_id)
        schema = avro.schema.parse(json.dumps(schema_dict))
        buffer = io.BytesIO()
        buffer.write(b'\x00')
        buffer.write(struct.pack('>I', schema_id))

        encoder = avro.io.BinaryEncoder(buffer)
        writer = avro.io.DatumWriter(schema)
        writer.write(record, encoder)

        return buffer.getvalue()
    

    async def deserialize(self, data: bytes) -> dict:
        if data[0] != 0:
            raise ValueError('Unsupported magic byte')

        schema_id = struct.unpack('>I', data[1:5])[0]
        schema_dict = await self.__confluent.get_schema_by_id(schema_id)
        schema = avro.schema.parse(json.dumps(schema_dict))

        payload = io.BytesIO(data[5:])
        decoder = avro.io.BinaryDecoder(payload)
        reader = avro.io.DatumReader(schema)
        return reader.read(decoder)

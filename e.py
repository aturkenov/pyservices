import asyncio
from typing import Annotated
from pyservices import service, Depend

@service
class RecursiveService:
    _sub: Annotated['RecursiveService', Depend]

    async def print_schema(self):
        """
        Prints service schema
        """
        print(f"""
        self = {self}
        subx1 = {self._sub}
        subx2 = {self._sub._sub}
        subx3 = {self._sub._sub._sub}
        subx4 = {self._sub._sub._sub._sub}
        subx5 = {self._sub._sub._sub._sub._sub}
        subx6 = {self._sub._sub._sub._sub._sub._sub}
        subx7 = {self._sub._sub._sub._sub._sub._sub._sub}
        subx8 = {self._sub._sub._sub._sub._sub._sub._sub._sub}
        subx9 = {self._sub._sub._sub._sub._sub._sub._sub._sub._sub}
        subx10 = {self._sub._sub._sub._sub._sub._sub._sub._sub._sub._sub}
        """)

if __name__ == '__main__':
    endpoint = RecursiveService.print_schema.as_endpoint()
    asyncio.run(endpoint())


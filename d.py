import asyncio
from typing import Annotated
from pyservices import service, Depend

@service
class FirstService:
    ...

@service
class SecondService:
    _first: Annotated[FirstService, Depend]

@service
class MainService:
    _second: Annotated[SecondService, Depend]

    async def print_schema(self):
        """
        Prints service schema
        """
        print(f"""
        self = {self}
        second = {self._second}
        second.first = {self._second._first}
        """)

if __name__ == '__main__':
    endpoint = MainService.print_schema.as_endpoint()
    asyncio.run(endpoint())


import asyncio
from typing import Annotated
from pyservices import service, Depend

@service
class AService:
    ...

@service
class BService:
    a: Annotated[AService, Depend]

@service
class CService:
    b: Annotated[BService, Depend]

@service
class DService:
    ca: Annotated[CService, Depend]
    cb: Annotated[CService, Depend(new_recursive=True)]

@service
class MasterService:
    a: Annotated[AService, Depend]
    b: Annotated[BService, Depend]
    c: Annotated[CService, Depend]
    d: Annotated['DService', Depend]

    async def test(
        self,
        x: int
    ):
        """
        Hello, world!
        """
        print(f"""
        self = {self}
        a = {self.a}
        b.a = {self.b.a}
        b = {self.b}
        c = {self.c}
        d = {self.d}
        d.ca = {self.d.ca}
        d.cb = {self.d.cb}
        x = {x}
        type(x) = {type(x)}
        """)


if __name__ == '__main__':
    endpoint = MasterService.test.as_endpoint()
    asyncio.run(endpoint('1'))


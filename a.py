from typing import TYPE_CHECKING, Annotated
from pyservices import service, Depend


if TYPE_CHECKING:
    from b import SecondService


@service
class FirstService:

    _s_second: Annotated['SecondService', Depend]

    async def test(
        self,
        x: int
    ):
        return x ** 2


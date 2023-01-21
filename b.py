from typing import TYPE_CHECKING, Annotated
from pyservices import service, Depend


if TYPE_CHECKING:
    from a import FirstService


@service
class SecondService:

    _s_first: Annotated['FirstService', Depend]

    async def test(
        self,
        x: int
    ):
        return await self._s_first.test(x) ** 0.5


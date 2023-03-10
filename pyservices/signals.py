import asyncio
from inspect import iscoroutinefunction as is_async
from typing import Mapping, List, Callable, Union


class SignalManager:

    __signals: Mapping[str, List[Callable]] = {}

    def add(
        self,
        signal_name: str,
        procedure: Callable
    ) -> None:
        assert callable(procedure), 'procedure must be Callable'
        self.__signals.setdefault(signal_name, [])
        self.__signals[signal_name].append(procedure)

    def on(
        self,
        signal_name: Union[str, Callable] = None
    ) -> Callable:
        """
        Uses procedure name if signal_name is not passed
        Returns passed procedure
        >>> @signals.on
        >>> async def ():
        """
        def decorate(procedure: Callable):
            _signal_name = procedure.__name__ if signal_name is None else signal_name
            self.add(_signal_name, procedure)
            return procedure
        if callable(signal_name):
            _signal_name, procedure = signal_name.__name__, signal_name
            self.add(_signal_name, procedure)
            return procedure
        return decorate

    async def fire(
        self,
        signal_name: str,
        *args,
        **kwargs
    ) -> None:
        P = self.__signals.get(signal_name, [])
        C = []
        for procedure in P:
            if is_async(procedure):
                c = procedure(*args, **kwargs)
                C.append(c)
            else:
                procedure(*args, **kwargs)
        await asyncio.gather(*C)


service_signals = SignalManager()
endpoint_signals = SignalManager()


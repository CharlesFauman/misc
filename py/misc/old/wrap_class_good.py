# %%
from __future__ import annotations
from typing import Callable, overload


def add(a: int, b: int) -> int:
    return a + b

class Wrapper:
    @overload
    def __call__(
        self,
        func: None = None,
    ) -> Wrapper:
        ...

    @overload
    def __call__[**P, T](
        self,
        func: Callable[P, T],
    ) -> Callable[P, T]:
        ...

    def __call__[**P, T](
        self,
        func: Callable[P, T] | None = None,
    ) -> Callable[P, T] | Wrapper:
        if func is not None:
            return func

        return Wrapper()
    
wrapper = Wrapper()

wrapper()(add)(1, 2)

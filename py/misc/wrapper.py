# %%
from __future__ import annotations
from functools import partial, update_wrapper
from typing import Callable, Concatenate, ParamSpec, TypeVar, overload, Any, Generic

P = ParamSpec("P")
T = TypeVar("T")
K = ParamSpec("K")

class Wrapper(Generic[K]):
    def __init__(self, wrapped: Callable[Concatenate[Any, K], Any]):
        self.wrapped = wrapped

    @overload
    def __call__(
        self,
        func: Callable[P, T],
        *args: K.args,
        **kwargs: K.kwargs,
    ) -> Callable[P, T]:
        ...

    @overload
    def __call__(
        self,
        func: Any = None,
        *args: K.args,
        **kwargs: K.kwargs,
    ) -> Wrapper[K]:
        ...


    def __call__(
        self,
        func: Callable[P, T] | Any = None,
        *args: K.args,
        **kwargs: K.kwargs,
    ) -> Callable[P, T] | Wrapper[K]:
        if func is not None and callable(func):
            return self.wrapped(func, *args, **kwargs)

        return partial(Wrapper(self.wrapped), *args, **kwargs)  # type: ignore

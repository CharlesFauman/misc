# %%
from functools import partial
from typing import Any, Callable, TypedDict, Unpack, overload


def add(a: int, b: int) -> int:
    return a + b


class DoIt(TypedDict, total=False):
    doit: bool


class Wrapped[T, **P]:
    def __init__(self, func: Callable[P, T], **kwargs: Unpack[DoIt]):
        self.func = func
        self.doit = kwargs["doit"] if "doit" in kwargs else False

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        print("Wrapped")
        return self.func(*args, **kwargs)


@overload
def wrap_inner[T, **P](
    func: Callable[P, T],
    **kwargs: Unpack[DoIt],
) -> Callable[P, T]: ...


@overload
def wrap_inner[T, **P](
    func: None,
    **kwargs: Unpack[DoIt],
) -> Callable[[Callable[P, T]], Callable[P, T]]: ...


def wrap_inner[T, **P](
    func: Callable[P, T] | None = None,
    **kwargs: Unpack[DoIt],
) -> Callable[P, T] | Callable[[Callable[P, T]], Callable[P, T]]:
    if func:
        return Wrapped(func, **kwargs)
    return partial(wrap_inner, **kwargs)


logged_add = wrap_inner(add)

logged_add(1, 2)

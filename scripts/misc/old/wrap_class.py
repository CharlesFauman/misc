# # %%
# from __future__ import annotations
# from functools import partial
# from typing import Callable, Protocol, TypedDict, Unpack, overload


# def add(a: int, b: int) -> int:
#     return a + b


# class DoPrint(TypedDict, total=False):
#     do_print: bool


# class Wrapped[**P, T]:
#     def __init__(self, func: Callable[P, T], **kwargs: Unpack[DoPrint]):
#         self.func = func
#         self.do_print = kwargs["do_print"] if "do_print" in kwargs else False

#     def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
#         if self.do_print:
#             print("Wrapped")
#         return self.func(*args, **kwargs)


# class Wrapper[**P, T](Protocol):
#     def __call__(
#         self,
#         func: Callable[P, T] | None = None,
#         **kwargs: Unpack[DoPrint],
#     ) -> Callable[P, T] | Wrapper[P, T]: ...


# @overload
# def wrapper[**P, T](
#     func: None,
#     **kwargs: Unpack[DoPrint],
# ) -> Wrapper[P, T]: ...


# @overload
# def wrapper[**P, T](
#     func: Callable[P, T],
#     **kwargs: Unpack[DoPrint],
# ) -> Callable[P, T]: ...


# def wrapper[**P, T](
#     func: Callable[P, T] | None = None,
#     **kwargs: Unpack[DoPrint],
# ) -> Callable[P, T] | Wrapper[P, T]:
#     if func is not None:
#         return Wrapped(func, **kwargs)

#     return partial(wrapper, **kwargs)


# wrapper(do_print=True)(add)(1, 2)

# # %%

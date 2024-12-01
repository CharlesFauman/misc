# %%
from __future__ import annotations
from functools import update_wrapper
from typing import Callable
from misc.wrapper import Wrapper


class LogWrapper[**P, T]:
    def __init__(self, func: Callable[P, T], do_print: bool = False):
        self.func = func
        self.do_print = do_print
        update_wrapper(self, func)

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        if self.do_print:
            print("wrapping with log")
        return self.func(*args, **kwargs)


log_wrapper = Wrapper(LogWrapper)


def add(a: int, b: int) -> int:
    return a + b


print(log_wrapper()(do_print=True)(add, do_print=False)(1, 2))
print(log_wrapper(add, True)(1, 2))


@log_wrapper(False)
def add2(a: int, b: int) -> int:
    return a + b


print(add2(2, 3))

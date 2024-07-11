from _curses import *
from _curses import _CursesWindow as _CursesWindow
from collections.abc import Callable
from typing import Final, TypeVar
from typing_extensions import Concatenate, ParamSpec

# NOTE: The _curses module is ordinarily only available on Unix, but the
# windows-curses package makes it available on Windows as well with the same
# contents.

_T = TypeVar("_T")
_P = ParamSpec("_P")

# available after calling `curses.initscr()`
LINES: Final[int]
COLS: Final[int]

# available after calling `curses.start_color()`
COLORS: Final[int]
COLOR_PAIRS: Final[int]

def wrapper(func: Callable[Concatenate[_CursesWindow, _P], _T], /, *arg: _P.args, **kwds: _P.kwargs) -> _T: ...

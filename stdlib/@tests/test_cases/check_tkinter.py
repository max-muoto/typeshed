from __future__ import annotations

import sys
import tkinter
import traceback
import types
from typing_extensions import assert_type


def custom_handler(exc: type[BaseException], val: BaseException, tb: types.TracebackType | None) -> None:
    print("oh no")


root = tkinter.Tk()
root.report_callback_exception = traceback.print_exception
root.report_callback_exception = custom_handler


def foo(x: int, y: str) -> None:
    pass


root.after(1000, foo, 10, "lol")
root.after(1000, foo, 10, 10)  # type: ignore


# Font size must be integer
label = tkinter.Label()
label.config(font=("", 12))
label.config(font=("", 12.34))  # type: ignore
label.config(font=("", 12, "bold"))
label.config(font=("", 12.34, "bold"))  # type: ignore


if sys.version_info >= (3, 13):
    text_widget = tkinter.Text(root, height=10, width=40)

    text_widget.insert("1.0", "Hello world!")

    start_index = "1.0"
    end_index = "end"

    word_to_count = "Python"
    result_1 = text_widget.count(start_index, end_index, "chars", "displaychars")
    assert_type(result_1, tuple[int, ...])

    result_2 = text_widget.count(start_index, end_index, "chars")
    assert_type(result_2, tuple[int, ...] | None)

    result_3 = text_widget.count(start_index, end_index, "chars", "displaychars", return_ints=True)
    assert_type(result_3, tuple[int, ...])

    result_4 = text_widget.count(start_index, end_index, "chars", return_ints=True)
    assert_type(result_4, int)

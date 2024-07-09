from __future__ import annotations

import importlib.resources
import pathlib
import sys


class _CustomPathLike:
    def __init__(self, path: str) -> None:
        self.path = path

    def __fspath__(self) -> str:
        return self.path


if sys.version_info >= (3, 13):

    def f(pth: pathlib.Path | str | _CustomPathLike) -> None:
        importlib.resources.open_binary("pkg", pth)
        # Encoding defaults to "utf-8" for one arg.
        importlib.resources.open_text("pkg", pth)
        # Otherwise, it must be specified.
        importlib.resources.open_text("pkg", pth, pth)  # type: ignore
        importlib.resources.open_text("pkg", pth, pth, encoding="utf-8")

        # Encoding defaults to "utf-8" for one arg.
        importlib.resources.read_text("pkg", pth)
        # Otherwise, it must be specified.
        importlib.resources.read_text("pkg", pth, pth)  # type: ignore
        importlib.resources.read_text("pkg", pth, pth, encoding="utf-8")

        importlib.resources.read_binary("pkg", pth)
        importlib.resources.path("pkg", pth)
        importlib.resources.is_resource("pkg", pth)
        importlib.resources.contents("pkg", pth)

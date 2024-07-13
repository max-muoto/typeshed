import sys
import types
from contextlib import AbstractContextManager
from importlib.abc import ResourceReader, Traversable
from pathlib import Path
from typing import Callable, overload
from typing_extensions import TypeAlias
from warnings import deprecated

Package: TypeAlias = str | types.ModuleType

if sys.version_info >= (3, 12):
    Anchor: TypeAlias = Package

if sys.version_info >= (3, 12):
    def package_to_anchor(
        package_to_anchor: Callable[[Anchor | None], Traversable],
    ) -> Callable[[Anchor | None, Anchor | None], Traversable]: ...

if sys.version_info >= (3, 12):
    @overload
    @deprecated("First parameter to files is renamed to 'anchor'")
    def files(package: Anchor | None = None) -> Traversable: ...
    @overload
    def files(anchor: Anchor | None = None) -> Traversable: ...
else:
    def files(package: Package) -> Traversable: ...

def get_resource_reader(package: types.ModuleType) -> ResourceReader | None: ...

if sys.version_info >= (3, 12):
    def resolve(cand: Anchor | None) -> types.ModuleType: ...
else:
    def resolve(cand: Package) -> types.ModuleType: ...

if sys.version_info < (3, 12):
    def get_package(package: Package) -> types.ModuleType: ...

def from_package(package: types.ModuleType) -> Traversable: ...
def as_file(path: Traversable) -> AbstractContextManager[Path]: ...

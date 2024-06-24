from __future__ import annotations

from typing import Generic, Literal, Protocol, final, overload
from typing_extensions import TypeVar

_T = TypeVar("_T")
_EndT = TypeVar("_EndT", bound=Literal["send", "recv", "both"], default=Literal["both"])

class _CrossInterpterData(Protocol): ...

@final
class ChannelId(Generic[_EndT]):
    @overload
    def __new__(
        cls,
        id: int,
        send: Literal[True] = ...,
        recv: Literal[False] = ...,
        force: bool = False,
        _resolve: bool = False,
    ) -> ChannelId[Literal["send"]]: ...
    @overload
    def __new__(
        cls,
        id: int,
        send: Literal[False] = ...,
        recv: Literal[True] = ...,
        force: bool = False,
        _resolve: bool = False,
    ) -> ChannelId[Literal["recv"]]: ...
    @overload
    def __new__(
        cls,
        id: int,
        send: Literal[True] = ...,
        recv: Literal[True] = ...,
        force: bool = False,
        _resolve: bool = False,
    ) -> ChannelId[Literal["both"]]: ...
    @property
    def end(self) -> _EndT: ...
    @property
    def send(self) -> ChannelId[Literal["send"]]: ...
    @property
    def recv(self) -> ChannelId[Literal["recv"]]: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __str__(self) -> str: ...

def create() -> ChannelId: ...
def destroy(cid: int) -> None: ...
def list_all() -> None: ...
def list_interpreters(cid: int, send: bool = False) -> None: ...
def send(cid: int, obj: _CrossInterpterData, blocking: bool = True) -> None: ...
def send_buffer() -> None: ...
def recv() -> None: ...
def close() -> None: ...
def get_info() -> None: ...
def _register_end_EndTypes() -> None: ...
@overload
def _channel_id(
    id: int,
    send: Literal[True] = ...,
    recv: Literal[False] = ...,
    force: bool = False,
    _resolve: bool = False,
) -> ChannelId[Literal["send"]]: ...
@overload
def _channel_id(
    cls,
    id: int,
    send: Literal[False] = ...,
    recv: Literal[True] = ...,
    force: bool = False,
    _resolve: bool = False,
) -> ChannelId[Literal["recv"]]: ...
@overload
def _channel_id(
    cls,
    id: int,
    send: Literal[True] = ...,
    recv: Literal[True] = ...,
    force: bool = False,
    _resolve: bool = False,
) -> ChannelId[Literal["both"]]: ...

from typing import SupportsIndex

class QueueError(RuntimeError): ...
class QueueNotFoundError(QueueError): ...

def bind(qid: SupportsIndex) -> None: ...
def create(maxsize: SupportsIndex, fmt: SupportsIndex) -> int: ...
def destroy(qid: SupportsIndex) -> None: ...
def get(qid: SupportsIndex) -> tuple[object, int]: ...
def get_count(qid: SupportsIndex) -> int: ...
def get_maxsize(qid: SupportsIndex) -> int: ...
def get_queue_defaults(qid: SupportsIndex) -> tuple[int]: ...
def is_full(qid: SupportsIndex) -> bool: ...
def list_all() -> list[tuple[int, int]]: ...
def put(qid: SupportsIndex, obj: object, fmt: SupportsIndex) -> None: ...
def release(qid: SupportsIndex) -> None: ...

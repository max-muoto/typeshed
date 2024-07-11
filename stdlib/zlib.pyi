import sys
from _typeshed import ReadableBuffer
from typing import Final

DEFLATED: Final = 8
DEF_MEM_LEVEL: Final[int]  # can change
DEF_BUF_SIZE: Final = 16384
MAX_WBITS: Final[int]
ZLIB_VERSION: Final[str]  # can change
ZLIB_RUNTIME_VERSION: Final[str]  # can change
Z_NO_COMPRESSION: Final = 0
Z_PARTIAL_FLUSH: Final = 1
Z_BEST_COMPRESSION: Final = 9
Z_BEST_SPEED: Final = 1
Z_BLOCK: Final = 5
Z_DEFAULT_COMPRESSION: Final = -1
Z_DEFAULT_STRATEGY: Final = 0
Z_FILTERED: Final = 1
Z_FINISH: Final = 4
Z_FIXED: Final = 4
Z_FULL_FLUSH: Final = 3
Z_HUFFMAN_ONLY: Final = 2
Z_NO_FLUSH: Final = 0
Z_RLE: Final = 3
Z_SYNC_FLUSH: Final = 2
Z_TREES: Final = 6

class error(Exception): ...

class _Compress:
    def compress(self, data: ReadableBuffer) -> bytes: ...
    def flush(self, mode: int = ...) -> bytes: ...
    def copy(self) -> _Compress: ...

class _Decompress:
    unused_data: bytes
    unconsumed_tail: bytes
    eof: bool
    def decompress(self, data: ReadableBuffer, max_length: int = ...) -> bytes: ...
    def flush(self, length: int = ...) -> bytes: ...
    def copy(self) -> _Decompress: ...

def adler32(data: ReadableBuffer, value: int = 1, /) -> int: ...

if sys.version_info >= (3, 11):
    def compress(data: ReadableBuffer, /, level: int = -1, wbits: int = 15) -> bytes: ...

else:
    def compress(data: ReadableBuffer, /, level: int = -1) -> bytes: ...

def compressobj(
    level: int = -1, method: int = 8, wbits: int = 15, memLevel: int = 8, strategy: int = 0, zdict: ReadableBuffer | None = None
) -> _Compress: ...
def crc32(data: ReadableBuffer, value: int = 0, /) -> int: ...
def decompress(data: ReadableBuffer, /, wbits: int = 15, bufsize: int = 16384) -> bytes: ...
def decompressobj(wbits: int = 15, zdict: ReadableBuffer = b"") -> _Decompress: ...

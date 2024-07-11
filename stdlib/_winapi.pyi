import sys
from _typeshed import ReadableBuffer
from collections.abc import Sequence
from typing import Any, Final, Literal, NoReturn, final, overload

if sys.platform == "win32":
    ABOVE_NORMAL_PRIORITY_CLASS: Literal[0x8000]
    BELOW_NORMAL_PRIORITY_CLASS: Literal[0x4000]

    CREATE_BREAKAWAY_FROM_JOB: Literal[0x1000000]
    CREATE_DEFAULT_ERROR_MODE: Literal[0x4000000]
    CREATE_NO_WINDOW: Literal[0x8000000]
    CREATE_NEW_CONSOLE: Literal[0x10]
    CREATE_NEW_PROCESS_GROUP: Literal[0x200]

    DETACHED_PROCESS: Literal[8]
    DUPLICATE_CLOSE_SOURCE: Literal[1]
    DUPLICATE_SAME_ACCESS: Literal[2]

    ERROR_ALREADY_EXISTS: Literal[183]
    ERROR_BROKEN_PIPE: Literal[109]
    ERROR_IO_PENDING: Literal[997]
    ERROR_MORE_DATA: Literal[234]
    ERROR_NETNAME_DELETED: Literal[64]
    ERROR_NO_DATA: Literal[232]
    ERROR_NO_SYSTEM_RESOURCES: Literal[1450]
    ERROR_OPERATION_ABORTED: Literal[995]
    ERROR_PIPE_BUSY: Literal[231]
    ERROR_PIPE_CONNECTED: Literal[535]
    ERROR_SEM_TIMEOUT: Literal[121]

    FILE_FLAG_FIRST_PIPE_INSTANCE: Literal[0x80000]
    FILE_FLAG_OVERLAPPED: Literal[0x40000000]

    FILE_GENERIC_READ: Literal[1179785]
    FILE_GENERIC_WRITE: Literal[1179926]

    FILE_MAP_ALL_ACCESS: Literal[983071]
    FILE_MAP_COPY: Literal[1]
    FILE_MAP_EXECUTE: Literal[32]
    FILE_MAP_READ: Literal[4]
    FILE_MAP_WRITE: Literal[2]

    FILE_TYPE_CHAR: Literal[2]
    FILE_TYPE_DISK: Literal[1]
    FILE_TYPE_PIPE: Literal[3]
    FILE_TYPE_REMOTE: Literal[32768]
    FILE_TYPE_UNKNOWN: Literal[0]

    GENERIC_READ: Literal[0x80000000]
    GENERIC_WRITE: Literal[0x40000000]
    HIGH_PRIORITY_CLASS: Literal[0x80]
    INFINITE: Literal[0xFFFFFFFF]
    # Ignore the Flake8 error -- flake8-pyi assumes
    # most numbers this long will be implementation details,
    # but here we can see that it's a power of 2
    INVALID_HANDLE_VALUE: Literal[0xFFFFFFFFFFFFFFFF]  # noqa: Y054
    IDLE_PRIORITY_CLASS: Literal[0x40]
    NORMAL_PRIORITY_CLASS: Literal[0x20]
    REALTIME_PRIORITY_CLASS: Literal[0x100]
    NMPWAIT_WAIT_FOREVER: Literal[0xFFFFFFFF]

    MEM_COMMIT: Literal[0x1000]
    MEM_FREE: Literal[0x10000]
    MEM_IMAGE: Literal[0x1000000]
    MEM_MAPPED: Literal[0x40000]
    MEM_PRIVATE: Literal[0x20000]
    MEM_RESERVE: Literal[0x2000]

    NULL: Literal[0]
    OPEN_EXISTING: Literal[3]

    PIPE_ACCESS_DUPLEX: Literal[3]
    PIPE_ACCESS_INBOUND: Literal[1]
    PIPE_READMODE_MESSAGE: Literal[2]
    PIPE_TYPE_MESSAGE: Literal[4]
    PIPE_UNLIMITED_INSTANCES: Literal[255]
    PIPE_WAIT: Literal[0]

    PAGE_EXECUTE: Literal[0x10]
    PAGE_EXECUTE_READ: Literal[0x20]
    PAGE_EXECUTE_READWRITE: Literal[0x40]
    PAGE_EXECUTE_WRITECOPY: Literal[0x80]
    PAGE_GUARD: Literal[0x100]
    PAGE_NOACCESS: Literal[0x1]
    PAGE_NOCACHE: Literal[0x200]
    PAGE_READONLY: Literal[0x2]
    PAGE_READWRITE: Literal[0x4]
    PAGE_WRITECOMBINE: Literal[0x400]
    PAGE_WRITECOPY: Literal[0x8]

    PROCESS_ALL_ACCESS: Literal[0x1FFFFF]
    PROCESS_DUP_HANDLE: Literal[0x40]

    SEC_COMMIT: Literal[0x8000000]
    SEC_IMAGE: Literal[0x1000000]
    SEC_LARGE_PAGES: Literal[0x80000000]
    SEC_NOCACHE: Literal[0x10000000]
    SEC_RESERVE: Literal[0x4000000]
    SEC_WRITECOMBINE: Literal[0x40000000]

    STARTF_USESHOWWINDOW: Literal[0x1]
    STARTF_USESTDHANDLES: Literal[0x100]

    STD_ERROR_HANDLE: Literal[0xFFFFFFF4]
    STD_OUTPUT_HANDLE: Literal[0xFFFFFFF5]
    STD_INPUT_HANDLE: Literal[0xFFFFFFF6]

    STILL_ACTIVE: Literal[259]
    SW_HIDE: Literal[0]
    SYNCHRONIZE: Literal[0x100000]
    WAIT_ABANDONED_0: Literal[128]
    WAIT_OBJECT_0: Literal[0]
    WAIT_TIMEOUT: Literal[258]

    if sys.version_info >= (3, 10):
        LOCALE_NAME_INVARIANT: Final[str]
        LOCALE_NAME_MAX_LENGTH: Final[int]
        LOCALE_NAME_SYSTEM_DEFAULT: Final[str]
        LOCALE_NAME_USER_DEFAULT: str | None

        LCMAP_FULLWIDTH: Final[int]
        LCMAP_HALFWIDTH: Final[int]
        LCMAP_HIRAGANA: Final[int]
        LCMAP_KATAKANA: Final[int]
        LCMAP_LINGUISTIC_CASING: Final[int]
        LCMAP_LOWERCASE: Final[int]
        LCMAP_SIMPLIFIED_CHINESE: Final[int]
        LCMAP_TITLECASE: Final[int]
        LCMAP_TRADITIONAL_CHINESE: Final[int]
        LCMAP_UPPERCASE: Final[int]

    if sys.version_info >= (3, 12):
        COPYFILE2_CALLBACK_CHUNK_STARTED: Literal[1]
        COPYFILE2_CALLBACK_CHUNK_FINISHED: Literal[2]
        COPYFILE2_CALLBACK_STREAM_STARTED: Literal[3]
        COPYFILE2_CALLBACK_STREAM_FINISHED: Literal[4]
        COPYFILE2_CALLBACK_POLL_CONTINUE: Literal[5]
        COPYFILE2_CALLBACK_ERROR: Literal[6]

        COPYFILE2_PROGRESS_CONTINUE: Literal[0]
        COPYFILE2_PROGRESS_CANCEL: Literal[1]
        COPYFILE2_PROGRESS_STOP: Literal[2]
        COPYFILE2_PROGRESS_QUIET: Literal[3]
        COPYFILE2_PROGRESS_PAUSE: Literal[4]

        COPY_FILE_FAIL_IF_EXISTS: Literal[0x1]
        COPY_FILE_RESTARTABLE: Literal[0x2]
        COPY_FILE_OPEN_SOURCE_FOR_WRITE: Literal[0x4]
        COPY_FILE_ALLOW_DECRYPTED_DESTINATION: Literal[0x8]
        COPY_FILE_COPY_SYMLINK: Literal[0x800]
        COPY_FILE_NO_BUFFERING: Literal[0x1000]
        COPY_FILE_REQUEST_SECURITY_PRIVILEGES: Literal[0x2000]
        COPY_FILE_RESUME_FROM_PAUSE: Literal[0x4000]
        COPY_FILE_NO_OFFLOAD: Literal[0x40000]
        COPY_FILE_REQUEST_COMPRESSED_TRAFFIC: Literal[0x10000000]

        ERROR_ACCESS_DENIED: Literal[5]
        ERROR_PRIVILEGE_NOT_HELD: Literal[1314]

    def CloseHandle(handle: int, /) -> None: ...
    @overload
    def ConnectNamedPipe(handle: int, overlapped: Literal[True]) -> Overlapped: ...
    @overload
    def ConnectNamedPipe(handle: int, overlapped: Literal[False] = False) -> None: ...
    @overload
    def ConnectNamedPipe(handle: int, overlapped: bool) -> Overlapped | None: ...
    def CreateFile(
        file_name: str,
        desired_access: int,
        share_mode: int,
        security_attributes: int,
        creation_disposition: int,
        flags_and_attributes: int,
        template_file: int,
        /,
    ) -> int: ...
    def CreateJunction(src_path: str, dst_path: str, /) -> None: ...
    def CreateNamedPipe(
        name: str,
        open_mode: int,
        pipe_mode: int,
        max_instances: int,
        out_buffer_size: int,
        in_buffer_size: int,
        default_timeout: int,
        security_attributes: int,
        /,
    ) -> int: ...
    def CreatePipe(pipe_attrs: Any, size: int, /) -> tuple[int, int]: ...
    def CreateProcess(
        application_name: str | None,
        command_line: str | None,
        proc_attrs: Any,
        thread_attrs: Any,
        inherit_handles: bool,
        creation_flags: int,
        env_mapping: dict[str, str],
        current_directory: str | None,
        startup_info: Any,
        /,
    ) -> tuple[int, int, int, int]: ...
    def DuplicateHandle(
        source_process_handle: int,
        source_handle: int,
        target_process_handle: int,
        desired_access: int,
        inherit_handle: bool,
        options: int = 0,
        /,
    ) -> int: ...
    def ExitProcess(ExitCode: int, /) -> NoReturn: ...
    def GetACP() -> int: ...
    def GetFileType(handle: int) -> int: ...
    def GetCurrentProcess() -> int: ...
    def GetExitCodeProcess(process: int, /) -> int: ...
    def GetLastError() -> int: ...
    def GetModuleFileName(module_handle: int, /) -> str: ...
    def GetStdHandle(std_handle: int, /) -> int: ...
    def GetVersion() -> int: ...
    def OpenProcess(desired_access: int, inherit_handle: bool, process_id: int, /) -> int: ...
    def PeekNamedPipe(handle: int, size: int = 0, /) -> tuple[int, int] | tuple[bytes, int, int]: ...
    if sys.version_info >= (3, 10):
        def LCMapStringEx(locale: str, flags: int, src: str) -> str: ...
        def UnmapViewOfFile(address: int, /) -> None: ...

    @overload
    def ReadFile(handle: int, size: int, overlapped: Literal[True]) -> tuple[Overlapped, int]: ...
    @overload
    def ReadFile(handle: int, size: int, overlapped: Literal[False] = False) -> tuple[bytes, int]: ...
    @overload
    def ReadFile(handle: int, size: int, overlapped: int | bool) -> tuple[Any, int]: ...
    def SetNamedPipeHandleState(
        named_pipe: int, mode: int | None, max_collection_count: int | None, collect_data_timeout: int | None, /
    ) -> None: ...
    def TerminateProcess(handle: int, exit_code: int, /) -> None: ...
    def WaitForMultipleObjects(handle_seq: Sequence[int], wait_flag: bool, milliseconds: int = 0xFFFFFFFF, /) -> int: ...
    def WaitForSingleObject(handle: int, milliseconds: int, /) -> int: ...
    def WaitNamedPipe(name: str, timeout: int, /) -> None: ...
    @overload
    def WriteFile(handle: int, buffer: ReadableBuffer, overlapped: Literal[True]) -> tuple[Overlapped, int]: ...
    @overload
    def WriteFile(handle: int, buffer: ReadableBuffer, overlapped: Literal[False] = False) -> tuple[int, int]: ...
    @overload
    def WriteFile(handle: int, buffer: ReadableBuffer, overlapped: int | bool) -> tuple[Any, int]: ...
    @final
    class Overlapped:
        event: int
        def GetOverlappedResult(self, wait: bool, /) -> tuple[int, int]: ...
        def cancel(self) -> None: ...
        def getbuffer(self) -> bytes | None: ...

    if sys.version_info >= (3, 12):
        def CopyFile2(existing_file_name: str, new_file_name: str, flags: int, progress_routine: int | None = None) -> int: ...
        def NeedCurrentDirectoryForExePath(exe_name: str, /) -> bool: ...

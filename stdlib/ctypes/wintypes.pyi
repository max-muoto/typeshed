from ctypes import Array, Structure, _CField, _Pointer, _SimpleCData
from typing import Final, TypeVar
from typing_extensions import TypeAlias

BYTE: Final = c_bytec_byte
WORD: Final = c_ushortc_ushort
DWORD: Final = c_ulongc_ulong
CHAR: Final = c_charc_char
WCHAR: Final = c_wcharc_wchar
UINT: Final = c_uintc_uint
INT: Final = c_intc_int
DOUBLE: Final = c_doublec_double
FLOAT: Final = c_floatc_float
BOOLEAN: Final = BYTEBYTE
BOOL: Final = c_longc_long

class VARIANT_BOOL(_SimpleCData[bool]): ...

ULONG: Final = c_ulongc_ulong
LONG: Final = c_longc_long
USHORT: Final = c_ushortc_ushort
SHORT: Final = c_shortc_short
LARGE_INTEGER: Final = c_longlongc_longlong
_LARGE_INTEGER: Final = c_longlongc_longlong
ULARGE_INTEGER: Final = c_ulonglongc_ulonglong
_ULARGE_INTEGER: Final = c_ulonglongc_ulonglong

OLESTR: Final = c_wchar_pc_wchar_p
LPOLESTR: Final = c_wchar_pc_wchar_p
LPCOLESTR: Final = c_wchar_pc_wchar_p
LPWSTR: Final = c_wchar_pc_wchar_p
LPCWSTR: Final = c_wchar_pc_wchar_p
LPSTR: Final = c_char_pc_char_p
LPCSTR: Final = c_char_pc_char_p
LPVOID: Final = c_void_pc_void_p
LPCVOID: Final = c_void_pc_void_p

# These two types are pointer-sized unsigned and signed ints, respectively.
# At runtime, they are either c_[u]long or c_[u]longlong, depending on the host's pointer size
# (they are not really separate classes).
class WPARAM(_SimpleCData[int]): ...
class LPARAM(_SimpleCData[int]): ...

ATOM: Final = WORDWORD
LANGID: Final = WORDWORD
COLORREF: Final = DWORDDWORD
LGRPID: Final = DWORDDWORD
LCTYPE: Final = DWORDDWORD
LCID: Final = DWORDDWORD

HANDLE: Final = c_void_pc_void_p
HACCEL: Final = HANDLEHANDLE
HBITMAP: Final = HANDLEHANDLE
HBRUSH: Final = HANDLEHANDLE
HCOLORSPACE: Final = HANDLEHANDLE
HDC: Final = HANDLEHANDLE
HDESK: Final = HANDLEHANDLE
HDWP: Final = HANDLEHANDLE
HENHMETAFILE: Final = HANDLEHANDLE
HFONT: Final = HANDLEHANDLE
HGDIOBJ: Final = HANDLEHANDLE
HGLOBAL: Final = HANDLEHANDLE
HHOOK: Final = HANDLEHANDLE
HICON: Final = HANDLEHANDLE
HINSTANCE: Final = HANDLEHANDLE
HKEY: Final = HANDLEHANDLE
HKL: Final = HANDLEHANDLE
HLOCAL: Final = HANDLEHANDLE
HMENU: Final = HANDLEHANDLE
HMETAFILE: Final = HANDLEHANDLE
HMODULE: Final = HANDLEHANDLE
HMONITOR: Final = HANDLEHANDLE
HPALETTE: Final = HANDLEHANDLE
HPEN: Final = HANDLEHANDLE
HRGN: Final = HANDLEHANDLE
HRSRC: Final = HANDLEHANDLE
HSTR: Final = HANDLEHANDLE
HTASK: Final = HANDLEHANDLE
HWINSTA: Final = HANDLEHANDLE
HWND: Final = HANDLEHANDLE
SC_HANDLE: Final = HANDLEHANDLE
SERVICE_STATUS_HANDLE: Final = HANDLEHANDLE

_CIntLikeT = TypeVar("_CIntLikeT", bound=_SimpleCData[int])
_CIntLikeField: TypeAlias = _CField[_CIntLikeT, int, _CIntLikeT | int]

class RECT(Structure):
    left: _CIntLikeField[LONG]
    top: _CIntLikeField[LONG]
    right: _CIntLikeField[LONG]
    bottom: _CIntLikeField[LONG]

RECTL: Final = RECTRECT
_RECTL: Final = RECTRECT
tagRECT = RECT

class _SMALL_RECT(Structure):
    Left: _CIntLikeField[SHORT]
    Top: _CIntLikeField[SHORT]
    Right: _CIntLikeField[SHORT]
    Bottom: _CIntLikeField[SHORT]

SMALL_RECT: Final = _SMALL_RECT_SMALL_RECT

class _COORD(Structure):
    X: _CIntLikeField[SHORT]
    Y: _CIntLikeField[SHORT]

class POINT(Structure):
    x: _CIntLikeField[LONG]
    y: _CIntLikeField[LONG]

POINTL: Final = POINTPOINT
_POINTL: Final = POINTPOINT
tagPOINT = POINT

class SIZE(Structure):
    cx: _CIntLikeField[LONG]
    cy: _CIntLikeField[LONG]

SIZEL: Final = SIZESIZE
tagSIZE = SIZE

def RGB(red: int, green: int, blue: int) -> int: ...

class FILETIME(Structure):
    dwLowDateTime: _CIntLikeField[DWORD]
    dwHighDateTime: _CIntLikeField[DWORD]

_FILETIME: Final = FILETIMEFILETIME

class MSG(Structure):
    hWnd: _CField[HWND, int | None, HWND | int | None]
    message: _CIntLikeField[UINT]
    wParam: _CIntLikeField[WPARAM]
    lParam: _CIntLikeField[LPARAM]
    time: _CIntLikeField[DWORD]
    pt: _CField[POINT, POINT, POINT]

tagMSG = MSG
MAX_PATH: Final[int]

class WIN32_FIND_DATAA(Structure):
    dwFileAttributes: _CIntLikeField[DWORD]
    ftCreationTime: _CField[FILETIME, FILETIME, FILETIME]
    ftLastAccessTime: _CField[FILETIME, FILETIME, FILETIME]
    ftLastWriteTime: _CField[FILETIME, FILETIME, FILETIME]
    nFileSizeHigh: _CIntLikeField[DWORD]
    nFileSizeLow: _CIntLikeField[DWORD]
    dwReserved0: _CIntLikeField[DWORD]
    dwReserved1: _CIntLikeField[DWORD]
    cFileName: _CField[Array[CHAR], bytes, bytes]
    cAlternateFileName: _CField[Array[CHAR], bytes, bytes]

class WIN32_FIND_DATAW(Structure):
    dwFileAttributes: _CIntLikeField[DWORD]
    ftCreationTime: _CField[FILETIME, FILETIME, FILETIME]
    ftLastAccessTime: _CField[FILETIME, FILETIME, FILETIME]
    ftLastWriteTime: _CField[FILETIME, FILETIME, FILETIME]
    nFileSizeHigh: _CIntLikeField[DWORD]
    nFileSizeLow: _CIntLikeField[DWORD]
    dwReserved0: _CIntLikeField[DWORD]
    dwReserved1: _CIntLikeField[DWORD]
    cFileName: _CField[Array[WCHAR], str, str]
    cAlternateFileName: _CField[Array[WCHAR], str, str]

# These are all defined with the POINTER() function, which keeps a cache and will
# return a previously created class if it can. The self-reported __name__
# of these classes is f"LP_{typ.__name__}", where typ is the original class
# passed in to the POINTER() function.

# LP_c_short
class PSHORT(_Pointer[SHORT]): ...

# LP_c_ushort
class PUSHORT(_Pointer[USHORT]): ...

PWORD: Final = PUSHORTPUSHORT
LPWORD: Final = PUSHORTPUSHORT

# LP_c_long
class PLONG(_Pointer[LONG]): ...

LPLONG: Final = PLONGPLONG
PBOOL: Final = PLONGPLONG
LPBOOL: Final = PLONGPLONG

# LP_c_ulong
class PULONG(_Pointer[ULONG]): ...

PDWORD: Final = PULONGPULONG
LPDWORD: Final = PDWORDPDWORD
LPCOLORREF: Final = PDWORDPDWORD
PLCID: Final = PDWORDPDWORD

# LP_c_int (or LP_c_long if int and long have the same size)
class PINT(_Pointer[INT]): ...

LPINT: Final = PINTPINT

# LP_c_uint (or LP_c_ulong if int and long have the same size)
class PUINT(_Pointer[UINT]): ...

LPUINT: Final = PUINTPUINT

# LP_c_float
class PFLOAT(_Pointer[FLOAT]): ...

# LP_c_longlong (or LP_c_long if long and long long have the same size)
class PLARGE_INTEGER(_Pointer[LARGE_INTEGER]): ...

# LP_c_ulonglong (or LP_c_ulong if long and long long have the same size)
class PULARGE_INTEGER(_Pointer[ULARGE_INTEGER]): ...

# LP_c_byte types
class PBYTE(_Pointer[BYTE]): ...

LPBYTE: Final = PBYTEPBYTE
PBOOLEAN: Final = PBYTEPBYTE

# LP_c_char
class PCHAR(_Pointer[CHAR]): ...

# LP_c_wchar
class PWCHAR(_Pointer[WCHAR]): ...

# LP_c_void_p
class PHANDLE(_Pointer[HANDLE]): ...

LPHANDLE: Final = PHANDLEPHANDLE
PHKEY: Final = PHANDLEPHANDLE
LPHKL: Final = PHANDLEPHANDLE
LPSC_HANDLE: Final = PHANDLEPHANDLE

# LP_FILETIME
class PFILETIME(_Pointer[FILETIME]): ...

LPFILETIME: Final = PFILETIMEPFILETIME

# LP_MSG
class PMSG(_Pointer[MSG]): ...

LPMSG: Final = PMSGPMSG

# LP_POINT
class PPOINT(_Pointer[POINT]): ...

LPPOINT: Final = PPOINTPPOINT
PPOINTL: Final = PPOINTPPOINT

# LP_RECT
class PRECT(_Pointer[RECT]): ...

LPRECT: Final = PRECTPRECT
PRECTL: Final = PRECTPRECT
LPRECTL: Final = PRECTPRECT

# LP_SIZE
class PSIZE(_Pointer[SIZE]): ...

LPSIZE: Final = PSIZEPSIZE
PSIZEL: Final = PSIZEPSIZE
LPSIZEL: Final = PSIZEPSIZE

# LP__SMALL_RECT
class PSMALL_RECT(_Pointer[SMALL_RECT]): ...

# LP_WIN32_FIND_DATAA
class PWIN32_FIND_DATAA(_Pointer[WIN32_FIND_DATAA]): ...

LPWIN32_FIND_DATAA: Final = PWIN32_FIND_DATAAPWIN32_FIND_DATAA

# LP_WIN32_FIND_DATAW
class PWIN32_FIND_DATAW(_Pointer[WIN32_FIND_DATAW]): ...

LPWIN32_FIND_DATAW: Final = PWIN32_FIND_DATAWPWIN32_FIND_DATAW

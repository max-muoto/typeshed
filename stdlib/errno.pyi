import sys
from collections.abc import Mapping
from typing import Final

errorcode: Mapping[int, str]

EPERM: Final[int]
ENOENT: Final[int]
ESRCH: Final[int]
EINTR: Final[int]
EIO: Final[int]
ENXIO: Final[int]
E2BIG: Final[int]
ENOEXEC: Final[int]
EBADF: Final[int]
ECHILD: Final[int]
EAGAIN: Final[int]
ENOMEM: Final[int]
EACCES: Final[int]
EFAULT: Final[int]
EBUSY: Final[int]
EEXIST: Final[int]
EXDEV: Final[int]
ENODEV: Final[int]
ENOTDIR: Final[int]
EISDIR: Final[int]
EINVAL: Final[int]
ENFILE: Final[int]
EMFILE: Final[int]
ENOTTY: Final[int]
ETXTBSY: Final[int]
EFBIG: Final[int]
ENOSPC: Final[int]
ESPIPE: Final[int]
EROFS: Final[int]
EMLINK: Final[int]
EPIPE: Final[int]
EDOM: Final[int]
ERANGE: Final[int]
EDEADLK: Final[int]
ENAMETOOLONG: Final[int]
ENOLCK: Final[int]
ENOSYS: Final[int]
ENOTEMPTY: Final[int]
ELOOP: Final[int]
EWOULDBLOCK: Final[int]
ENOMSG: Final[int]
EIDRM: Final[int]
ENOSTR: Final[int]
ENODATA: Final[int]
ETIME: Final[int]
ENOSR: Final[int]
EREMOTE: Final[int]
ENOLINK: Final[int]
EPROTO: Final[int]
EBADMSG: Final[int]
EOVERFLOW: Final[int]
EILSEQ: Final[int]
EUSERS: Final[int]
ENOTSOCK: Final[int]
EDESTADDRREQ: Final[int]
EMSGSIZE: Final[int]
EPROTOTYPE: Final[int]
ENOPROTOOPT: Final[int]
EPROTONOSUPPORT: Final[int]
ESOCKTNOSUPPORT: Final[int]
ENOTSUP: Final[int]
EOPNOTSUPP: Final[int]
EPFNOSUPPORT: Final[int]
EAFNOSUPPORT: Final[int]
EADDRINUSE: Final[int]
EADDRNOTAVAIL: Final[int]
ENETDOWN: Final[int]
ENETUNREACH: Final[int]
ENETRESET: Final[int]
ECONNABORTED: Final[int]
ECONNRESET: Final[int]
ENOBUFS: Final[int]
EISCONN: Final[int]
ENOTCONN: Final[int]
ESHUTDOWN: Final[int]
ETOOMANYREFS: Final[int]
ETIMEDOUT: Final[int]
ECONNREFUSED: Final[int]
EHOSTDOWN: Final[int]
EHOSTUNREACH: Final[int]
EALREADY: Final[int]
EINPROGRESS: Final[int]
ESTALE: Final[int]
EDQUOT: Final[int]
ECANCELED: Final[int]  # undocumented
ENOTRECOVERABLE: Final[int]  # undocumented
EOWNERDEAD: Final[int]  # undocumented

if sys.platform == "sunos5" or sys.platform == "solaris":  # noqa: Y008
    ELOCKUNMAPPED: Final[int]
    ENOTACTIVE: Final[int]

if sys.platform != "win32":
    ENOTBLK: Final[int]
    EMULTIHOP: Final[int]

if sys.platform == "darwin":
    # All of the below are undocumented
    EAUTH: Final[int]
    EBADARCH: Final[int]
    EBADEXEC: Final[int]
    EBADMACHO: Final[int]
    EBADRPC: Final[int]
    EDEVERR: Final[int]
    EFTYPE: Final[int]
    ENEEDAUTH: Final[int]
    ENOATTR: Final[int]
    ENOPOLICY: Final[int]
    EPROCLIM: Final[int]
    EPROCUNAVAIL: Final[int]
    EPROGMISMATCH: Final[int]
    EPROGUNAVAIL: Final[int]
    EPWROFF: Final[int]
    ERPCMISMATCH: Final[int]
    ESHLIBVERS: Final[int]
    if sys.version_info >= (3, 11):
        EQFULL: Final[int]

if sys.platform != "darwin":
    EDEADLOCK: Final[int]

if sys.platform != "win32" and sys.platform != "darwin":
    ECHRNG: Final[int]
    EL2NSYNC: Final[int]
    EL3HLT: Final[int]
    EL3RST: Final[int]
    ELNRNG: Final[int]
    EUNATCH: Final[int]
    ENOCSI: Final[int]
    EL2HLT: Final[int]
    EBADE: Final[int]
    EBADR: Final[int]
    EXFULL: Final[int]
    ENOANO: Final[int]
    EBADRQC: Final[int]
    EBADSLT: Final[int]
    EBFONT: Final[int]
    ENONET: Final[int]
    ENOPKG: Final[int]
    EADV: Final[int]
    ESRMNT: Final[int]
    ECOMM: Final[int]
    EDOTDOT: Final[int]
    ENOTUNIQ: Final[int]
    EBADFD: Final[int]
    EREMCHG: Final[int]
    ELIBACC: Final[int]
    ELIBBAD: Final[int]
    ELIBSCN: Final[int]
    ELIBMAX: Final[int]
    ELIBEXEC: Final[int]
    ERESTART: Final[int]
    ESTRPIPE: Final[int]
    EUCLEAN: Final[int]
    ENOTNAM: Final[int]
    ENAVAIL: Final[int]
    EISNAM: Final[int]
    EREMOTEIO: Final[int]
    # All of the below are undocumented
    EKEYEXPIRED: Final[int]
    EKEYREJECTED: Final[int]
    EKEYREVOKED: Final[int]
    EMEDIUMTYPE: Final[int]
    ENOKEY: Final[int]
    ENOMEDIUM: Final[int]
    ERFKILL: Final[int]

if sys.platform == "win32":
    # All of these are undocumented
    WSABASEERR: Final[int]
    WSAEACCES: Final[int]
    WSAEADDRINUSE: Final[int]
    WSAEADDRNOTAVAIL: Final[int]
    WSAEAFNOSUPPORT: Final[int]
    WSAEALREADY: Final[int]
    WSAEBADF: Final[int]
    WSAECONNABORTED: Final[int]
    WSAECONNREFUSED: Final[int]
    WSAECONNRESET: Final[int]
    WSAEDESTADDRREQ: Final[int]
    WSAEDISCON: Final[int]
    WSAEDQUOT: Final[int]
    WSAEFAULT: Final[int]
    WSAEHOSTDOWN: Final[int]
    WSAEHOSTUNREACH: Final[int]
    WSAEINPROGRESS: Final[int]
    WSAEINTR: Final[int]
    WSAEINVAL: Final[int]
    WSAEISCONN: Final[int]
    WSAELOOP: Final[int]
    WSAEMFILE: Final[int]
    WSAEMSGSIZE: Final[int]
    WSAENAMETOOLONG: Final[int]
    WSAENETDOWN: Final[int]
    WSAENETRESET: Final[int]
    WSAENETUNREACH: Final[int]
    WSAENOBUFS: Final[int]
    WSAENOPROTOOPT: Final[int]
    WSAENOTCONN: Final[int]
    WSAENOTEMPTY: Final[int]
    WSAENOTSOCK: Final[int]
    WSAEOPNOTSUPP: Final[int]
    WSAEPFNOSUPPORT: Final[int]
    WSAEPROCLIM: Final[int]
    WSAEPROTONOSUPPORT: Final[int]
    WSAEPROTOTYPE: Final[int]
    WSAEREMOTE: Final[int]
    WSAESHUTDOWN: Final[int]
    WSAESOCKTNOSUPPORT: Final[int]
    WSAESTALE: Final[int]
    WSAETIMEDOUT: Final[int]
    WSAETOOMANYREFS: Final[int]
    WSAEUSERS: Final[int]
    WSAEWOULDBLOCK: Final[int]
    WSANOTINITIALISED: Final[int]
    WSASYSNOTREADY: Final[int]
    WSAVERNOTSUPPORTED: Final[int]

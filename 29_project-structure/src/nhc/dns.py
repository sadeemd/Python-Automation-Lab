import socket
from typing import Dict, Any

def dns_check(host: str, timeout: float = 3.0) -> Dict[str, Any]:
    """
    Returns a result dict with: ok, host, ip, error
    """
    socket.setdefaulttimeout(timeout)
    result = {"check": "dns", "host": host, "ok": False, "ip": None, "error": None}

    try:
        ip = socket.gethostbyname(host)
        result["ip"] = ip
        result["ok"] = True
    except Exception as e:
        result["error"] = str(e)

    return result

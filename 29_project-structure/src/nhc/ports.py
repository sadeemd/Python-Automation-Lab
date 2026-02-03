import socket
from typing import Dict, Any

def port_check(host: str, port: int, timeout: float = 2.0) -> Dict[str, Any]:
    """
    Returns a result dict with: ok, host, port, error
    """
    result = {"check": "port", "host": host, "port": port, "ok": False, "error": None}

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)

    try:
        s.connect((host, port))
        result["ok"] = True
    except Exception as e:
        result["error"] = str(e)
    finally:
        s.close()

    return result

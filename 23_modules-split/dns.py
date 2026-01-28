# dns.py
import socket

def resolve(domain: str) -> str:
    return socket.gethostbyname(domain)

import socket

def is_valid_target(target):
    try:
        socket.gethostbyname(target)
        return True
    except socket.error:
        return False

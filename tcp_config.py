import socket
from sys import getsizeof

NORMAL_NAME_SIZE = 200
NORMAL_SIZE_INDICATOR_SIZE = 100 # Have to convert to str
NORMAL_PACK_SIZE = 4096
ACK_STR = b"READY"

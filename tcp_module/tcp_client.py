from tcp_module.tcp_config import *

DEBUG_TAG = "[tcp_client]:"

def print_debug_info(*info_to_print):
    print(DEBUG_TAG, ' '.join(info_to_print))

class TCPClient:

    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self, addr, port):
        self.clientSocket.connect((addr, port))
    
    def send_ack(self):
        self.clientSocket.sendall(ACK_STR)
    
    def recv_ack(self):
        # Return True on success; otherwise return False
        receivedData = self.clientSocket.recv(getsizeof(ACK_STR))
        # print_debug_info("receivedData:", receivedData.decode())
        if receivedData.decode() != ACK_STR.decode():
            return False
        return True
    
    def send(self, str):
        # Return True on success; otherwise return False
        self.clientSocket.sendall(str.encode())
        if not self.recv_ack():
            return False
        return True
    
    def send_file_name(self, fileName):
        # Return True on success; otherwise return False
        self.clientSocket.sendall(fileName.encode())
        if not self.recv_ack():
            return False
        return True
    
    def send_file(self, file):
        # Return True on success; otherwise return False
        encodedFile = file.encode()
        sizeOfFile = getsizeof(encodedFile)
        self.clientSocket.sendall(str(sizeOfFile).encode())
        if not self.recv_ack():
            return False
        self.clientSocket.sendall(encodedFile)
        if not self.recv_ack():
            return False
        return True
    
    def receive(self, size):
        receivedData = self.clientSocket.recv(size)
        self.send_ack()
        return receivedData.decode()
        
    def receive_file_name(self):
        receivedData = self.clientSocket.recv(NORMAL_NAME_SIZE)
        self.send_ack()
        return receivedData.decode()
    
    def receive_file(self, clientID):
        # Return size, 'file' (probably str)
        size = int(self.clientSocket.recv(NORMAL_SIZE_INDICATOR_SIZE).decode())
        self.send_ack(clientID)
        remainingSize = size
        receivedData = b''
        while remainingSize > 0:
            if remainingSize < NORMAL_PACK_SIZE:
                tempReceivedData = self.clientSocket.recv(remainingSize)
            else:
                tempReceivedData = self.clientSocket.recv(NORMAL_PACK_SIZE)
            receivedData += tempReceivedData
            remainingSize -= getsizeof(tempReceivedData)
        self.send_ack(clientID)
        return size, receivedData.decode()



from tcp_config import *

DEBUG_TAG = "[tcp_server]:"

def print_debug_info(*info_to_print):
    print(DEBUG_TAG, ' '.join(info_to_print))

class TCPServer:

    def __init__(self):
        self.clientCount = 0
        self.clientConnections = {}
        self.clientConnAddresses = {}
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def bind(self, port):
        # print_debug_info("Listening as hostname:", socket.gethostbyname(socket.gethostname()))
        # self.serverSocket.bind((socket.gethostbyname(socket.gethostname()), port))
        self.serverSocket.bind(("127.0.0.1", port))

    def listen(self, maxUnansweredConn):
        self.serverSocket.listen(maxUnansweredConn)

    def accept(self):
        conn, addr = self.serverSocket.accept()
        clientID = self.clientCount
        self.clientCount += 1
        self.clientConnections[clientID] = conn
        self.clientConnAddresses[clientID] = addr
        return clientID
    
    def close(self):
        for connectedClient in self.clientConnections.values():
            connectedClient.close()
        self.serverSocket.close()
    
    def send_ack(self, clientID):
        self.clientConnections[clientID].sendall(ACK_STR)
    
    def recv_ack(self, clientID):
        # Return True on success; otherwise return False
        if self.clientConnections[clientID].recv(getsizeof(ACK_STR)) != ACK_STR:
            return False
        return True
    
    def send(self, clientID, str):
        # Return True on success; otherwise return False
        self.clientConnections[clientID].sendall(str)
        if not self.recv_ack(clientID):
            return False
        return True

    def send_file_name(self, clientID, fileName):
        # Return True on success; otherwise return False
        self.clientConnections[clientID].sendall(fileName.encode())
        if not self.recv_ack(clientID):
            return False
        return True
    
    def send_file(self, clientID, file):
        # Return True on success; otherwise return False
        encodedFile = file.encode()
        sizeOfFile = getsizeof(encodedFile)
        self.clientConnections[clientID].sendall(str(sizeOfFile).encode())
        if not self.recv_ack():
            return False
        self.clientConnections[clientID].sendall(encodedFile)
        if not self.recv_ack():
            return False
        return True
    
    def receive(self, clientID, size):
        receivedData = self.clientConnections[clientID].recv(size)
        self.send_ack(clientID)
        return receivedData.decode()
        
    def receive_file_name(self, clientID):
        receivedData = self.clientConnections[clientID].recv(NORMAL_NAME_SIZE)
        self.send_ack(clientID)
        return receivedData.decode()
    
    def receive_file(self, clientID):
        # Return size, 'file' (probably str)
        size = int(self.clientConnections[clientID].recv(NORMAL_SIZE_INDICATOR_SIZE).decode())
        self.send_ack(clientID)
        remainingSize = size
        receivedData = b''
        while remainingSize > 0:
            if remainingSize < NORMAL_PACK_SIZE:
                tempReceivedData = self.clientConnections[clientID].recv(remainingSize)
            else:
                tempReceivedData = self.clientConnections[clientID].recv(NORMAL_PACK_SIZE)
            receivedData += tempReceivedData
            remainingSize -= getsizeof(tempReceivedData)
        self.send_ack(clientID)
        return size, receivedData.decode()


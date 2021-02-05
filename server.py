from tcp_server import *

# Declare global variables here
DEBUG_TAG = "[server]:"
receivingServer = None
receivingServerPort = 8001
receivingServerMaxUnansweredConn = 5

def print_debug_info(*info_to_print):
    print(DEBUG_TAG, ' '.join(info_to_print))

def setup_tcp_server():
    global receivingServer
    receivingServer = TCPServer()
    receivingServer.bind(receivingServerPort)
    receivingServer.listen(receivingServerMaxUnansweredConn)

def accept_new_client():
    global receivingServer
    newClientId = receivingServer.accept()
    print_debug_info("Got new client connected with id:", str(newClientId))
    return newClientId

# Main function
def main():
    setup_tcp_server()
    newClientId = accept_new_client()
    newFileName = receivingServer.receive_file_name(newClientId)
    print_debug_info("The newFileName is:", newFileName)
    sizeOfNewFile, newFile = receivingServer.receive_file(newClientId)
    print_debug_info("The sizeOfNewFile is:", str(sizeOfNewFile))
    # print_debug_info("The newFile is:", newFile)
    receivingServer.close()
    
# Run main()
if __name__ == "__main__":
    main()

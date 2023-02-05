import sys
import socket

ip_adr = sys.argv[1]
port = sys.argv[2]

if sys.argv[3] == "-s":
    if sys.argv[4] == "-t": #server tcp
        print("Server tcp")
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind(('', int(port)))
        serverSocket.listen(1)

        while True:
            connectionSocket, addr = serverSocket.accept()
            data = connectionSocket.recv(1024)
            connectionSocket.send((addr[0] + ":" + str(addr[1])).encode('utf8'))
            connectionSocket.close()

    elif sys.argv[4] == "-u": #server udp
        print("Server udp")
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        serverSocket.bind(('', int(port)))
        while True:
            data, addr = serverSocket.recvfrom(2048)
            print(addr)
            serverSocket.sendto((addr[0] + ":" + str(addr[1])).encode('utf8') , addr)
    else:
        raise ValueError
else:
    if sys.argv[3] == "-t": #client tcp
        print("Client tcp")
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((ip_adr, int(port)))
        clientSocket.send(("Hi").encode('utf8'))
        data = clientSocket.recv(1024).decode('utf8')
        print(data)
        clientSocket.close()

    elif sys.argv[3] == "-u": #client udp
        print("Client udp")
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clientSocket.sendto(("Hi").encode('utf8'), (ip_adr, int(port)))
        data = clientSocket.recv(1024).decode('utf8')
        print(data)
        clientSocket.close()
    else:
        raise ValueError
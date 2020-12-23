import socket
import select

IP_ADRESS = "192.168.178.52"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP_ADRESS, 6969))
s.listen(5)

print("Server up and running!")

socket_list = [s]
users = {}

def receive_message(client_socket):  
    try:
        messageLen = client_socket.recv(8).decode("utf-8")
        message = client_socket.recv(int(messageLen))
        return message.decode("utf-8")
    except:
        return False

def send_message(client_socket, content):
    try:
        msg = str(content)
        client_socket.send(bytes(f'{len(msg):<8}'+msg, "utf-8"))
    except:
        print("<Message Error>")
        socket_list.remove(client_socket)

while True:
    read_sockets, _, exception_sockets = select.select(socket_list, [], socket_list)

    for client in read_sockets:
        if client == s:
            clientsocket, address = s.accept()
            print(f"Connection from {address} has been established.")
            clientsocket.send(bytes("Connected!", "utf-8"))
            username = clientsocket.recv(15)
            users[clientsocket] = username.decode("utf-8")
            print(users[clientsocket])
            socket_list.append(clientsocket)

        else:
            msg = receive_message(client)
            if msg != False: 
                print(users[client]+" > "+msg)
                for sentClient in socket_list:
                    if sentClient != s:
                        if sentClient != client:
                            send_message(sentClient, users[client]+" > "+msg)

    for client in exception_sockets:
        socket_list.remove(client)

        del users[client]
                            


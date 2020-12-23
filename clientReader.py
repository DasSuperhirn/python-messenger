import socket

IP_ADRESS = "192.168.178.52"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP_ADRESS, 6969))

s.send(bytes(f'clientReader', "utf-8"))

connectionMSG = s.recv(12)
print(connectionMSG.decode("utf-8"))

def receive_message():  
    try:
        messageLen = s.recv(8).decode("utf-8")
        message = s.recv(int(messageLen))
        return message.decode("utf-8")
    except:
        return False

while True:
    msg = receive_message()
    if msg != False:
        print(msg)

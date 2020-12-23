import socket

username = str(input("Username:"))

IP_ADRESS = "192.168.178.52"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP_ADRESS, 6969))

s.send(bytes(f'{username:<15}', "utf-8"))

connectionMSG = s.recv(12)
print(connectionMSG.decode("utf-8"))

def send_message(content):
    if content:
        msg = str(content)
        s.send(bytes(f'{len(msg):<8}'+msg, "utf-8"))

while True:
    #send_message(input())
    send_message(input())

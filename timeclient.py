from socket import *


client = socket(AF_INET, SOCK_STREAM)

client.connect((str(input('Введите IP: ')), 1303))

data = client.recv(1024)

message = data.decode('utf-8')

print(message)

client.close()
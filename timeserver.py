from socket import *
import datetime as d

time = d.datetime.now()

server = socket(AF_INET, SOCK_STREAM    )

server.bind(('', 1303))

while True:
    server.listen()
    user, addr = server.accept()
    user.send(str(time.strftime("%Y.%m.%d %H:%M")).encode('utf-8'))
    user.close()
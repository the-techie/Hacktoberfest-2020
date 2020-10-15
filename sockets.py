# import socket
# my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# my_socket.connect(("data.pr4e.org",80))
# cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()

# my_socket.send(cmd)

# while True:
#     data = my_socket.recv(512)
#     if len(data)<1:
#         break
#     print(data.decode(), end='')
    
# my_socket.close()

import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysocket.connect(('placementhansraj.com', 80))

cmd = "GET placementhansraj.com/internship/student HTTP/1.0\r\n\r\n".encode()

mysocket.send(cmd)

show = False

while True:
    data = mysocket.recv(1000)
    if len(data)<1:
        break
    if not show:
        pos = data.decode().find('\r\n\r\n')
        if pos == -1:
            show = False
        else:
            show = True
            data = data
            data = data[pos+4:]
            print(data.decode(), end='')
            continue
    if show:
        print(data.decode(), end='')

mysocket.close()
    
# This is the code from the video and it throws an error
# if I add the \r in line 7, the code works
# Heres the answer from Stack Overflow
# The '\r' character is the carriage return, and the carriage
# return-newline pair is both needed for newline in a # network virtual terminal session.
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()


# This is the code from the book and it works
# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(20)
#     if (len(data) < 1):
#         break
#     print(data.decode(),end='')

# mysock.close()

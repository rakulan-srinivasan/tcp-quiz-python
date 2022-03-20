import socket
import os
from time import sleep
from datetime import datetime

try:
    client_socket = socket.socket()
    port = 20000
    print('SYN to Server at ',datetime.now())
    client_socket.connect((socket.gethostname(), port))
    print(client_socket.recv(1024).decode(),' at ',datetime.now())
    print('Connected to (\'{}\', {})'.format(socket.gethostname(),port))
    client_socket.sendall('SYN-ACK from Client'.encode())
    print('SYN-ACK to Server at ',datetime.now())

    if client_socket.recv(1024).decode() == 'Window Terminated':
        print('Connection Lost - Quiz Terminated!')
        #client_socket.close()    
except (ConnectionRefusedError,ConnectionAbortedError, ConnectionResetError):
    pass
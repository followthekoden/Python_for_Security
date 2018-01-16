import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = ''
PORT = 50000
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()
conn.recv(1024)
conn.close()
sock.close()
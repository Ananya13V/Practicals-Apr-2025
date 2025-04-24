import socket

HOST = "127.0.0.1"
PORT = 4698

def send_data(data):
    return str(data).encode('utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("CLient connected to server using the host %s and port %d" %(HOST, PORT))
    a,b = input("Enter 2 numbers :").split()

    s.sendall(send_data(a))
    s.sendall(send_data(b))

    res = s.recv(1024)
    print("Sum of %s and %s = %s" %(a,b, res.decode('utf-8')))

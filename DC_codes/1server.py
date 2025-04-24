import socket

PORT = 4698
HOST = "127.0.0.1"

def send_data(data):
    return str(data).encode('utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Server started and listening on %s:%d" %(HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        data1 = conn.recv(1024)
        data2 = conn.recv(1024)

        a = int(data1.decode("utf-8"))
        b = int(data2.decode("utf-8"))

        print("Data 1 recd. from Client : ", a)
        print("Data 2 recd. from Client : ", b)

        res = a+b
        conn.sendall(send_data(res))
                          
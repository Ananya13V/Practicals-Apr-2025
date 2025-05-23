import socket
import threading

host = "127.0.0.1"
port = 9922
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []

def handle_client(client_, addr):
    while True:
        msg = client_.recv(1024)

        if not msg:
            if client_ in clients:
                print("\nClient{} disconnected.".fomat(addr))
                clients.remove(client_)
            break
        print("\nMessage from Client{}: {}".format(addr, msg.decode("utf-8")))

        for c in clients:
            if c!=client_:
                msg = "CLient" + addr + ": " + msg.decode("utf-8")
                c.send(msg.encode("utf-8"))
    client_.close()

while True:
    client, addr = server.accept()
    print("\n Client {} connected..".format(list(addr)[0]))
    clients.append(client)

    thread = threading.Thread(target=handle_client, args=(client, list(addr)[0]))
    thread.start()
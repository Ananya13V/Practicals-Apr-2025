import socket
import threading

host = "127.0.0.1"
port = 9922

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
print("\nCOnnected to the server {}".format(host))

def rec():
    while True:
        try:
            msg = client.recv(1024)
            print(msg.decode("utf-8"))
            print()

        except:
            client.close()
            break

thread= threading.Thread(target= rec)
thread.start()

while True:
    print()
    message = input()
    client.send(message.encode("utf-8"))

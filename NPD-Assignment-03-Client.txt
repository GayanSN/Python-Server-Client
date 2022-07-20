#! /usr/bin/python3

import socket
import sys
from threading import Thread

def client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect((host, port))

    while True:
        try:
            ts = Thread(target=send_data, args=(client,), daemon = True)
            tr = Thread(target=recv_data, args=(client,), daemon = True)

            ts.start()
            tr.start()
                
            ts.join()
            tr.join()

        except KeyboardInterrupt:
            client.close()
            exit(1)

def send_data(client,):
    while True:
        s_data = input("")
        client.send(s_data.encode('utf-8'))

def recv_data(client,):
    while True:
        r_data = client.recv(1024).decode('utf-8')
        print(r_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\nNo port number is provided!")
        print("       \uFFEC   ")
        print("usage : python3 " + str(sys.argv[0]) + " [port_number]\n")
        exit(1)

    port = int(sys.argv[1])
    host = "127.0.0.1"

    client()

#! /usr/bin/python3

import socket
import sys
from threading import Thread

def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((host, port))
    server.listen()
    conn, addr = server.accept()

    while True:
        try:
            ts = Thread(target=send_data, args=(conn,), daemon = True)
            tr = Thread(target=recv_data, args=(conn,), daemon = True)

            ts.start()
            tr.start()

            ts.join()
            tr.join()
            
        except KeyboardInterrupt:
            conn.close()
            exit(1)


def send_data(conn,):
        while True:
            s_data = input("")
            conn.send(s_data.encode('utf-8'))

def recv_data(conn,):
        while True:
            r_data = conn.recv(1024).decode('utf-8')
            print(r_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\nNo port number is provided!")
        print("       \uFFEC   ")
        print("usage : python3 " + str(sys.argv[0]) + " [port_number]\n")
        exit(1)

    port = int(sys.argv[1])
    host = "127.0.0.1"

    server()

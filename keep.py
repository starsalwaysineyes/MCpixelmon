import socket
import time

def listen_on_port(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    print(f"Listening on port {port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"Current time: {current_time}")

if __name__ == "__main__":
    print("start")
    listen_on_port(10)

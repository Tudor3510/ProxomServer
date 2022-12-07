import socket
import select

HOST = "127.0.0.1"
DAEMON_PORT = 45254

MESSAGES_PORT = 45259
MESSAGES_DST_PORT = 47777
MESSAGES_MAXIMUM_BUFFER = 100

MAX_DAEMON_CONNECTIONS = 1

messages_clients = []
def messages_running(messages_socket: socket):
    if select.select([messages_socket], [], [], 0):
        raw_message, addr = messages_socket.recvfrom(MESSAGES_MAXIMUM_BUFFER)
        


def start():
    daemon_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    daemon_socket.bind((HOST, DAEMON_PORT))
    daemon_socket.listen(MAX_DAEMON_CONNECTIONS)

    messages_socket = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
    messages_socket.bind((HOST, MESSAGES_PORT))



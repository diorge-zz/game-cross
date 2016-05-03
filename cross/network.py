import .game as cross
import socket


PORT = 13409
BUFFER_SIZE = 1024


class Server(object):
    """ Cross game TCP Server """

    def __init__(self):
        self.board = cross.new_board()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def start(self):
        """ Starts the server to outside connections """
        self.sock.bind((socket.gethostname(), PORT))
        self.sock.listen(2)

    def get_clients(self):
        """ Waits for two clients to connect """
        while len(self.clients) < 2:
            connection, _ = self.sock.accept()
            self.clients.append(ServerClient(connection))

    def broadcast(self, message):
        """ Broadcasts a message to every connected client """
        for client in self.clients:
            client.send(message)


class ServerClient(object):
    """ Cross game server-side TCP Client """

    def __init__(self, connection):
        """ Creates a connected client """
        self.connection = connection

    def close(self):
        """ Closes the open connection """
        self.connection.close()

    def receive(self):
        """ Receive data from this client """
        return self.connection.recv(BUFFER_SIZE)

    def send(self, message):
        """ Sends data to this client """
        return self.connection.send(message)


class Client(object):
    """ Client for connecting with the server """

    def __init__(self):
        """ Creates an empty connection """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, address):
        """ Connects with a server """
        self.sock.connect((address, PORT))

    def send_nickname(self, nickname):
        """ Sends your desired nickname to the server """
        self.sock.send('nickname;' + nickname)

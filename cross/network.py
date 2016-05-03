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
            connection, address = self.sock.accept()
            self.clients.append(Client(connection, address))


class Client(object):
    """ Cross game TCP Client """
    pass

import cross.game as cross
import socket


PORT = 13409
BUFFER_SIZE = 1024

COMMANDS = {
            'move': move_piece,
    }


def move_piece(srv, orig, dest):
    """ Moves a piece on the board from orig to dest """
    origPos = cross.Position.parse(orig)
    destPos = cross.Position.parse(dest)
    srv.board[destPos] = srv.board[origPos]


def process_message(msg, srv):
    """ Process a receive message from the active player """
    spl = msg.split(';')
    cmd = spl[0]
    args = spl[1:]
    COMMANDS[cmd](srv, *args)


class Server(object):
    """ Cross game TCP Server """

    def __init__(self):
        self.board = cross.new_board()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.active = None
        self.inactive = None

    def start(self):
        """ Starts the server to outside connections """
        self.sock.bind(('', PORT))
        self.sock.listen(2)

    def get_clients(self):
        """ Waits for two clients to connect """
        while len(self.clients) < 2:
            connection, _ = self.sock.accept()
            self.clients.append(ServerClient(connection))
        self.active

    def broadcast(self, message):
        """ Broadcasts a message to every connected client """
        for client in self.clients:
            client.send(message)

    def swap_players(self):
        """ Swaps the active and inactive players """
        self.active, self.inactive = (self.inactive, self.active)

    def read_play(self):
        """ Waits for the active player to make the next move """
        data = self.active.receive()
        process_message(data, self)


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

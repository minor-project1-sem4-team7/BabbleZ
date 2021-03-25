import threading
import socket
from datetime import datetime
import Security


def log(typ: str, text: str):
    '''
    [!] Information\n
    [#] Important or Warning\n
    [.] Process\n
    [-] Error\n
    [+] Success\n
    [N] Count
    '''

    timestamp = datetime.now()

    typ = '[' + typ + ']'
    with open('logfile.txt', 'a') as file:
        file.write(typ + ' ' + str(timestamp) + ' ' + text + '\n')


class Babble:
    def __init__(self):
        self.socket = socket.socket()
        self.port = 27526
        self.ip = '127.0.0.1'
        self.is_connected = False
        self.secure = Security.Security()

        log('!', f'Server IP {self.ip}')
        log('!', f'Server PORT {self.port}')

    def connect(self):
        try:
            self.socket.connect((self.ip, self.port))
            self.is_connected = True
            log('+', 'Connection made successfully to server')
        except:
            trial = 3
            while trial:
                log(f'{4 - trial}', 'Trying Again')
                trial -= 1
                try:
                    log('.', 'Connecting...')
                    self.socket.connect((self.ip, self.port))
                    self.is_connected = True
                    log('+', 'Connection made successfully to server')
                except:
                    log('-', 'Failed To connect!!!')

    def get_public_key(self, recv_id):
        pass

    def send_messg(self, message, reciver_id):
        if self.is_connected:
            self.secure.personal_encrypt(message)

    def recieve_messg(self):
        pass

    def save_messg(self):
        pass

    def status_report(self, userid):

        packet = '{} {}'.format(userid, datetime.now()).encode()
        while True:
            self.socket.send(packet)


if __name__ == '__main__':
    bab = Babble()
    # bab.connect()

    thread1 = threading.Thread(target=bab.connect())
    # thread2 = threading.Thread(target=bab.connect())

    thread1.start()
    print(bab.is_connected)
    # thread2.start()

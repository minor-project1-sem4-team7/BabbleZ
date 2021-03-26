import threading
import socket
from datetime import datetime
import Security
import user
import sys
import base64
import pickle


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
        self.profile = user.User()
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
        print(recv_id)
        return self.secure.public_key

    def send_messg(self, message, receiver_id):
        if self.is_connected:
            drop = list()
            pubkey = self.get_public_key(receiver_id)
            drop.append(self.secure.personal_encrypt(message, pubkey))

            metadata = list()
            metadata.append(self.secure.app_encrypt(receiver_id))
            metadata.append(self.secure.app_encrypt(self.profile.user_id))
            metadata.append(self.secure.app_encrypt(str(datetime.now())))
            metadata.append(self.secure.app_encrypt(str(sys.getsizeof(drop[0]))))

            drop.append(metadata)
            packet = pickle.dumps(drop)
            print(type(packet))
            # print(packet)
            # print(pickle.loads(packet))

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
    bab.connect()
    bab.send_messg('Hello What\'s app', 'noid')

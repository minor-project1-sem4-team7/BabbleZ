import threading
import socket
from datetime import datetime
import Security
import user
import sys
import pickle
import mongo_dao


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


class Babble(mongo_dao.MongoDAO, user.User, Security.Security):

    def __int__(self, username, password, userid, dp):
        pass

    def __init__(self, user_id, password):
        mongo_dao.MongoDAO.__init__(self)
        user.User.__init__(self)

        def loading_user_data():
            if self.if_user_exist(user_id):

                trial = 5
                while self.get_user_password(user_id) != Security.hash_str(password) and trial > 0:
                    trial -= 1
                    print('Failed To Login')  # TEMP REMAINING
                log('+', f'Logged In Successfully as {user_id}')

                user_dict = self.get_one('Profile','user_id',user_id)
                self.user_id = user_id
                self.username = user_dict["username"]
                self.user_dp = user_dict["display_profile"]

            else:
                print('User Not Found')  # TEMP REMAINING

        loading_user_data()
        Security.Security.__init__(self, self.get_publicKey(user_id), self.get_privateKey(user_id), self.get_one('Profile', 'user_id', self.user_id)["password"])
        self.password = self.get_one('Profile', 'user_id', self.user_id)["password"]

        self.socket = socket.socket()
        self.port = 27526
        self.ip = '127.0.0.1'
        self.is_connected = False

        log('!', f'Server IP {self.ip}')
        log('!', f'Server PORT {self.port}')

        self.connect()

    # connecting to server
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

    # get public key of provided user id
    def get_public_key(self, recv_id):
        if

    # send message method
    def send_messg(self, message, receiver_id):
        if self.is_connected:
            drop = list()
            pubkey = self.get_public_key(receiver_id)
            drop.append(self.secure.personal_encrypt(message, pubkey))

            metadata = list()
            metadata.append(self.secure.app_encrypt(receiver_id))
            metadata.append(self.secure.app_encrypt(self.user_id))
            metadata.append(self.secure.app_encrypt(str(datetime.now())))
            metadata.append(self.secure.app_encrypt(str(sys.getsizeof(drop[0]))))

            drop.append(metadata)
            packet = pickle.dumps(drop)
            print(packet)

    def recieve_messg(self):
        pass

    def save_messg(self):
        pass

    def status_report(self, userid):

        packet = '{} {}'.format(userid, datetime.now()).encode()
        while True:
            self.socket.send(packet)


if __name__ == '__main__':
    bab = Babble('superuser_Arnav','K!!L$Y')
    # bab.connect()
    # bab.send_messg('Hello Whats app', 'Abcd')

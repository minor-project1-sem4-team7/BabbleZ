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


class Babble:

    def __int__(self, username, password, userid, dp ):
        pass

    def __init__(self, user_id, password):
        self.dao = mongo_dao.MongoDAO()
        self.profile = user.User()

        def loading_user_data():
            if len(self.dao.get_collection('Profile')):

                trial = 5
                while self.dao.get_user_password(user_id) != Security.hash_str(password) or trial > 0:
                    trial -= 1
                    return 'Failed To Login'  # TEMP REMAINING

            else:
                return 'No user Found'  # TEMP REMAINING

        loading_user_data()




        self.secure = Security.Security()
        self.socket = socket.socket()
        self.port = 27526
        self.ip = '127.0.0.1'
        self.is_connected = False

        log('!', f'Server IP {self.ip}')
        log('!', f'Server PORT {self.port}')

        self.secure.password = self.dao.get_one('Profile', 'user_id', self.profile.user_id)["password"]

    # loading user credential keys
    def load_user_keys(self):
        my_id = self.profile.user_id
        if self.dao.if_user_exist(my_id):
            self.secure._public_key = self.dao.get_publicKey(my_id)
            self.secure._private_key = self.dao.get_privateKey(my_id)

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
        self.dao.get_publicKey(recv_id)
        return self.secure.public_key

    # send message method
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
    bab = Babble()
    bab.connect()
    bab.send_messg('Hello Whats app', 'Abcd')

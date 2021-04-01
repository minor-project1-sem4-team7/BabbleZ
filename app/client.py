import threading
import socket
from datetime import datetime
import Security
import user
import sys
import pickle
import mongo_dao
import logging

logging.basicConfig(filename='app_log.txt', level=logging.DEBUG,
                    format=f'%(levelname)s %(asctime)s %(name)s %(threadName)s : %(message)s')


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

    def __init__(self, user_id, passwd, username=''):
        mongo_dao.MongoDAO.__init__(self)
        user.User.__init__(self)
        self.logged_in = False

        def store_user_data():
            self.user_id = user_id
            self.username = username
            self.password = Security.hash_str(passwd)
            self.user_dp = 'Not set'  # TEMP
            # self.generate_keys()
            js_obj = {"user_id": user_id,
                      "username": username,
                      "password": self.password,
                      "public_key": str(self.public_key),
                      "private_key": str(self._private_key),
                      "about": 'not_set_yet',
                      "display_profile": self.user_dp
                      }
            self.insert('Profile', js_obj)
            print('Success')
            log('+', f'Signup Successful as {self.user_id}')

        def loading_user_data():
            if self.if_user_exist(user_id):

                if self.get_user_password(user_id) == Security.hash_str(passwd):
                    self.logged_in = True
                    log('+', f'Logged In Successfully as {user_id}')
                    user_dict = self.get_one('Profile', 'user_id', user_id)

                    self.user_id = user_id
                    self.username = user_dict["username"]
                    self.user_dp = user_dict["display_profile"]
                else:
                    raise str("Failed")

            else:
                raise str("user not found")

        if len(username) <= 0:
            loading_user_data()
            # pswd = passwd
            keys = self.get_myKeys(user_id)
            pub_Key = keys[0]
            prv_key = keys[1]
            Security.Security.__init__(self, passwd, pub_Key, prv_key)
            self.password = self.get_one('Profile', 'user_id', self.user_id)["password"]
            self.logged_in = True
            self.client = socket.socket()
            self.port = 27526
            self.ip = '127.0.0.1'
            self.is_connected = False

            log('!', f'Server IP {self.ip}')
            log('!', f'Server PORT {self.port}')



        else:
            try:
                Security.Security.__init__(self, passwd)
                store_user_data()
                self.success = True
            except:
                self.success = False

    def initiate_user_working(self):
        self.connect()

        recieve_thread = threading.Thread(target=self.recieve_messg())
        recieve_thread.start()

    # connecting to server
    def connect(self):
        try:
            self.client.connect((self.ip, self.port))
            self.is_connected = True
            log('+', 'Connection made successfully to server')
        except:
            trial = 3
            while trial:
                log(f'{4 - trial}', 'Trying Again')
                trial -= 1
                try:
                    log('.', 'Connecting...')
                    self.client.connect((self.ip, self.port))
                    self.is_connected = True
                    log('+', 'Connection made successfully to server')
                except:
                    log('-', 'Failed To connect!!!')

    # get public key of provided user id
    def get_public_key(self, recv_id):
        if self.if_user_exist(recv_id):
            return self.get_publicKey(recv_id)

    # send message method
    def send_messg(self, message, receiver_id):
        if self.is_connected:
            drop = list()
            pubkey = self.get_public_key(receiver_id)
            drop.append(Security.personal_encrypt(message, pubkey))

            metadata = list()
            metadata.append(self.app_encrypt(receiver_id))
            metadata.append(self.app_encrypt(self.user_id))
            metadata.append(self.app_encrypt(str(datetime.now())))
            metadata.append(self.app_encrypt(str(sys.getsizeof(drop[0]))))

            drop.append(metadata)
            packet = pickle.dumps(drop)
            print(packet)

    def recieve_messg(self):

        while True:
            try:
                message = self.client.recv(1024)
                print(message)

            except:
                print('Can not connect')

    def save_messg(self):
        pass

    def status_report(self, userid):

        packet = '{} {}'.format(userid, datetime.now()).encode()
        while True:
            self.client.send(packet)


if __name__ == '__main__':

    bab = Babble('superuser_Arnav', 'K!!L$Y')
    # bab.connect()
    # bab.send_messg('Hello Whats app', 'Abcd')

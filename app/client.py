import socket
import time
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
    """
    [!] Information\n
    [#] Important or Warning\n
    [.] Process\n
    [-] Error\n
    [+] Success\n
    [N] Count
    """

    timestamp = datetime.now()

    typ = '[' + typ + ']'
    with open('logfile.txt', 'a') as file:
        file.write(typ + ' ' + str(timestamp) + ' ' + text + '\n')


class Babble (mongo_dao.MongoDAO, user.User, Security.Security):

    def __init__(self, user_id, passwd, username=''):

        # Initiate Database
        mongo_dao.MongoDAO.__init__(self, user_id)

        # Initiate User
        user.User.__init__(self)
        # Set Default Login = False
        self.logged_in = False

        # Generate and Store New User Information
        def store_user_data():
            self.user_id = user_id
            self.username = username
            self.password = Security.hash_str(passwd)
            self.user_dp = 'Not set'  # TEMP

            js_obj = {"user_id": user_id,
                      "username": username,
                      "password": self.password,
                      "public_key": str(self._public_key),
                      "private_key": str(self._private_key),
                      "about": 'not_set_yet',
                      "display_profile": self.user_dp
                      }
            self.insert('Profile', js_obj)
            print('Success')
            log('+', f'Signup Successful as {self.user_id}')

        # Load Already Existed User Information
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

        # Check Request [Login/Signup]
        if len(username) <= 0:

            # Handling Login Request

            # Load Data Call
            loading_user_data()

            # Get Encryption Key Call
            keys = self.get_myKeys(user_id)

            # Initiate Security
            Security.Security.__init__(self, passwd, keys)

            # Set Password Again, Hashed Password
            self.password = self.get_one('Profile', 'user_id', self.user_id)["password"]

            # Set Login Flag
            self.logged_in = True

            # Socket Connection Started
            self.client = socket.socket()
            self.port = 27526
            self.ip = '127.0.0.1'
            self.is_connected = False

            log('!', f'Server IP {self.ip}')
            log('!', f'Server PORT {self.port}')

            # Initiate Connection To Server
            self.connect()

            # Send Login packet
            self.login_request()
        else:
            try:

                self.signup_success = False
                # Handling Signup Request
                self.connect()

                # Initiate Security Generation
                Security.Security.__init__(self, passwd)

                # Send Signup Packet
                self.signup_request()

                # Waiting Time
                limit = 300
                while not self.signup_success and limit:
                    limit -= 1
                    time.sleep(1)
                if self.signup_success:
                    store_user_data()
            except:
                self.signup_success = False

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
        if self.if_friend_exist(recv_id):
            return self.get_publicKey(recv_id)
        else:
            # returns the public key
            self.search_user(recv_id)
            # if rcv_public_key:
            #     return rcv_public_key
            # else:
            #     raise Exception()

    # send message method
    def send_msg(self, message, receiver_id):
        if self.is_connected:

            drop = list()
            try:
                pubkey = self.get_public_key(receiver_id)  # INCOMPLETE
                drop.append(Security.personal_encrypt(message, pubkey))
                           # INCOMPLETE

                metadata = list()
                metadata.append(Security.personal_encrypt(receiver_id))
                metadata.append(Security.personal_encrypt(self.user_id))
                metadata.append(Security.personal_encrypt(str(datetime.now())))
                metadata.append(Security.personal_encrypt(str(sys.getsizeof(drop[0]))))

                drop.append(metadata)
                drop.append(Security.personal_encrypt('msg'))
                packet = pickle.dumps(drop)
            except:
                log('-', 'Exception Raised while Sending message')
                return -1

            try:
                self.client.send(packet)
            except:
                log('-', 'Exception Packet Transfer')
                return -1

    def extract_payload(self, packet):
        drop = pickle.loads(packet)

        drop_type = self.personal_decrypt(drop[-1])

        if drop_type == 'msg':

            meta = drop[1]
            payload = self.personal_decrypt(drop[0])
            metadata = list()
            for values in meta:
                metadata.append(self.personal_decrypt(values))

            return self.imprint_message('received', metadata, payload)

    def received_message(self):
        try:
            message = self.client.recv(1024)
            if len(message):
                return self.extract_payload(message)
        except Exception as e:
            log('-',f'Exception {e}')

    def status_report(self, userid):

        packet = '{} {}'.format(userid, datetime.now()).encode()
        while True:
            self.client.send(packet)

    # Send Signup Request Packet
    def signup_request(self):
        pass

    # Send Login Request Packet
    def login_request(self):
        pass

    # Search for a user on server
    def search_user(self, recv_id) :
        pkt_typ = Security.personal_encrypt('publickey')
        recv_id = Security.personal_encrypt(recv_id)
        drop = [recv_id, pkt_typ]
        packet = pickle.dumps(drop)
        self.client.send(packet)


if __name__ == '__main__':

    # Testing Program
    bab = Babble('superuser_Arnav', 'K!!L$Y')

    import threading


    def receive():
        while True:
            bab.received_message()


    thread = threading.Thread(target=receive)
    thread.start()


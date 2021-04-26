import base64
import sys
import threading
import socket
import time
import mongo_dao
import rsa
import pickle
import logging
import Security

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

    from datetime import datetime
    timestamp = datetime.now()

    typ = '[' + typ + ']'
    with open('logfile.txt', 'a') as file:
        file.write(typ + ' ' + str(timestamp) + ' ' + text + '\n')


# Return Codes
rcd = {
    "-100": '[#] IDS Triggered ! Unauthorized User',
    "-99": 'Authentication Failure',
    "-98": 'Signup Failure',
    "-97": 'Update Error',
}


# Convert String to Public Key
def get_key(key: str) -> rsa.PublicKey:
    key = key[10:-1]
    key_numeric = [i for i in map(int, key.split(','))]
    return rsa.PublicKey(key_numeric[0], key_numeric[1])


# configuration
BUFFER_SIZE = 5210
IP = '0.0.0.0'
PORT = 27526

# Initial Global Authentication
# Server Global
__server_public_key__ = 'PublicKey(157137637721861869372539893459600696742127499758127772090085112140787972009214342489665530996268305128037221399721176471559193370133031726130729193098952822312718353677752558323517006429252983185444022055723152643529270527892933839066752166883567099046052682883104837595785078185695586176198813398487786120801, 65537)'
__server_private_key__ = rsa.PrivateKey(157137637721861869372539893459600696742127499758127772090085112140787972009214342489665530996268305128037221399721176471559193370133031726130729193098952822312718353677752558323517006429252983185444022055723152643529270527892933839066752166883567099046052682883104837595785078185695586176198813398487786120801, 65537, 12949942495625005057922821682031575493297383557282879855021586137180460454731932553926538183176604299808185189738530511358335038101965368461053574219199627204138226211032630865639909946301609871637999420688754637337432436740612186445776403921394153721997201757300882362884823386528726841072354839746652239409, 51531893765086721881235266883137551544676927249829260319578350386126932232021226958746139602207161292582494980437239217687526319681352565144107052797246775164631117, 3049327828668386721120818863117794595268767154099047823619298913277874965515397814480913499460684022693965710042216775476139992355879082303434853)

# Client Global
__client_initial_public_key__ = rsa.PublicKey(153479565307109564197997366112287960436400200886230813383955527999664984402398678762266835053163840025004137309234234296442926603527018877278452833043158154349572364075989212640279342343355762948079249181852702965699899782277805411509669798247394844322618281836704853954015313872756543429415231152518292985093, 65537)
__client_initial_private_key__ = rsa.PrivateKey(153479565307109564197997366112287960436400200886230813383955527999664984402398678762266835053163840025004137309234234296442926603527018877278452833043158154349572364075989212640279342343355762948079249181852702965699899782277805411509669798247394844322618281836704853954015313872756543429415231152518292985093, 65537, 30463130529546381602568773950419485013911131317089436814295642281759038666805041630522712214040240338209771855875595766179861593583463716002229484562769770821410178476803304192032061593058293310795361852950195777246633869875878028465944954891549813150775103835332448661683979058570160507285165184106812114945, 55537758210444071218413159150012759189767997919433615002525493775627266119765236783497321293067053544055718202682695521590801668269713670777849452295464272832468709, 2763517474463835864396985967076149699473333329194721245889576736985561944189010002379589782451842891236096628798805340946302137914880219004060577)

# Server Database Connection
_srv_db = mongo_dao.MongoDAO()

# Server Initialization
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()

print(f'Listening for connections on {IP}:{PORT}...!')

# Active Client List
active_clients = list()

# Log out Error Packet
error_logout_packet = pickle.dumps([Security.encrypt_data('Logging Out , Facing error with your Account, Try to Re Signin', __client_initial_public_key__), Security.encrypt_data('errorlogout',__client_initial_public_key__)])


# return codes Packet
def rcd_packet(code : int):

    if code == -100:
        typ = Security.encrypt_data('IDS_Warning', __client_initial_public_key__)
    else:
        typ = Security.encrypt_data('exception', __client_initial_public_key__)

    er = Security.encrypt_data(rcd[str(code)], __client_initial_public_key__)
    return pickle.dumps([er, typ])


# Per client Handler Class
class Handler:

    def __init__(self, userid : str, password : str, publickey : str, sock : socket.socket, adrs : tuple):

        _srv_db.update_by('Profiles', 'user_id', userid, {"public_key":publickey})
        self.user_id = userid
        self.password = password
        self.str_publickey = publickey
        self.public_key = get_key(publickey)
        self.user_socket = sock
        self.user_address = adrs
        self.status = True
        self.database = mongo_dao.MongoDAO(userid)

    # pickle packet Creator
    def manifest_packet(self, payload, rcvd_metadata, handler) -> bytes:

        drop = list()
        drop.append(payload)
        info = [self.user_id, rcvd_metadata[2], rcvd_metadata[3]]
        metadata = list()

        pkey = handler.public_key

        for value in info:
            metadata.append(Security.encrypt_data(value, pkey))

        drop.append(metadata)
        drop.append(Security.encrypt_data('msg', pkey))

        return pickle.dumps(drop)

    def send_msg(self, client : socket.socket, packet: bytes):

        try:
            client.send(packet)
        except:
            log('-',f'Error Sending Message with client {self.user_id}, Address {self.user_address} ')
            try:
                client.send(error_logout_packet)
            except:
                del self
            del self

    # Client Received Message Handler
    def receive_msg_handler(self):

        packet = ''
        while not len(packet):
            packet = self.user_socket.recv(BUFFER_SIZE)

        if len(packet):

            # Message Send Request Handler
            packet = pickle.loads(packet)

            pkt_typ = Security.decrypt_data(packet[-1])

            # Handling Incoming Packet
            if pkt_typ == 'msg':

                payload = packet[0]
                rcvd_metadata = list()
                for values in packet[1]:
                    rcvd_metadata.append(Security.decrypt_data(values))

                # Searching Receiver Object Handel
                rcvr_handler = next((x for x in active_clients if x.user_id == rcvd_metadata[0]), None)      # DEBUG

                # Creating Forward Packet
                packet = self.manifest_packet(payload, rcvd_metadata, rcvr_handler)

                if not rcvr_handler:
                    pass
                else:
                    self.send_msg(rcvr_handler.user_socket,packet)

            # Handling Status update packet
            elif pkt_typ == 'status':

                def update_status():
                    self.status = True
                    time.sleep(60)
                    self.status = False

                status_thread = threading.Thread(target=update_status)
                status_thread.start()

            # Password Change Request Handler
            elif pkt_typ == 'passwd':
                userid = Security.decrypt_data(packet[1])

                if userid == self.user_id:
                    newpass = Security.decrypt_data(packet[0])
                    try:
                        _srv_db.update_by('Profiles', 'user_id', self.user_id, {"password": newpass})

                    except:
                        self.send_msg(self.user_socket,rcd_packet(-97))
                else:
                    self.send_msg(self.user_socket,rcd_packet(-100))

            elif pkt_typ == 'publickey':
                user_id = Security.decrypt_data(packet[0])
                uid = Security.encrypt_data(user_id, self.public_key)
                pkey = Security.encrypt_data(_srv_db.get_publicKey(user_id),self.public_key)
                typ = Security.encrypt_data('publickey', self.public_key)
                drop = [uid, pkey, typ]
                self.send_msg(self.user_socket, pickle.dumps(drop))
            else:
                self.send_msg(self.user_socket,rcd_packet(-100))

            packet = ''

    def initiate_user(self):
        while True:
            self.receive_msg_handler()
        # recv_thread = threading.Thread(target= self.receive_msg_handler)
        # recv_thread.start()


# Message type Handler  (packet received, socket object, address of client)
def msg_classifier(packet, sock : socket.socket = None, adrs = None):

    # Received Bytes to list
    drop = pickle.loads(packet)
    # Packet type
    pkt_typ = Security.decrypt_data(drop[-1])

    # Login Request Handler
    if pkt_typ == 'login':

        password = Security.decrypt_data(drop[0])
        userid = Security.decrypt_data(drop[1])
        publickey = Security.decrypt_data(drop[2])

        if password == _srv_db.get_user_password(userid):
            if sock and adrs:
                client = Handler(userid, password, publickey, sock, adrs)

                active_clients.append(client)       # Adding to active clients list, HASHING

                client_thread = threading.Thread(target=client.initiate_user)
                client_thread.start()
            else:
                sock.send(rcd_packet(-100))
        else:
            sock.send(rcd_packet(-99))

    # Signup Request Handler
    elif pkt_typ == 'signup':

        try:
            metadata = list()
            for value in drop[0]:
                metadata.append(Security.decrypt_data(value))

            js_obj = {
                "user_id": metadata[0],
                "password": metadata[1],
                "public_key": metadata[2],
                "username": metadata[3]
            }
            _srv_db.insert('Profiles', js_obj)

            res = Security.encrypt_data('Success', get_key(js_obj['public_key']))
            drop = [res, Security.encrypt_data('signup', get_key(js_obj['public_key']))]
            packet = pickle.dumps(drop)
            sock.send(packet)
        except:
            sock.send(rcd_packet(-98))

    # Public Key Fetch Request Handler
    elif pkt_typ == 'publickey':
        user_id = Security.decrypt_data(drop[0])
        if user_id == '#0000':
            sock.send(Security.encrypt_data(__server_public_key__,__client_initial_public_key__))
        else:
            sock.send(rcd_packet(-100))

    # IDS condition, Invalid Request
    else:
        sock.send(rcd_packet(-100))


if __name__ == '__main__':

    def starting_server():

        first_packet = b''
        client_socket , client_address = server_socket.accept()
        log('+', f'Connected to {client_address}')
        # client_socket.send(f'Hello {client_address} You are connected'.encode())

        pack = client_socket.recv(BUFFER_SIZE)
        first_packet += pack
        # print(first_packet)
        if first_packet:
            try:
                msg_classifier(pack,client_socket, client_address)
            except Exception as e:
                log('-', f'Caught Exception Handeling Message, {e}')
                pass


    while True:
        server_thread = threading.Thread(target=starting_server())
        try:
            server_thread.start()
        except:

            log('#', 'Server Reset')
            pass


## IMPORTANT DATA LIMITER
    # SEND
    # Receive
    # Encrypt
    # Decrypt
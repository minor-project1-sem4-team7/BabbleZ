import socket
import select
import logging
import rsa
from security import Security
import threading
import pickle
from mongo_dao import MongoDAO

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



HEADER_LENGTH = 10

IP = "0.0.0.0"
PORT = 27526

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen()

sockets_list = [server_socket]

clients = {}
print(f'Listening for connections on {IP}:{PORT}...')


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8').strip())
        log('+', 'Message Recieved !')
        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
        log('-', 'Failed To Recieve!!!')
        return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            user = receive_message(client_socket)
            if user is False:
                continue

            sockets_list.append(client_socket)
            clients[client_socket] = user
            clients[client_socket] = user
            print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
        else:
            message = receive_message(notified_socket)

            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
                sockets_list.remove(notified_socket)
                del clients[notified_socket]

                continue

            user = clients[notified_socket]
            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]

def send_to_client(packet):
    while True:
        clientsocket, address = server_socket.accept()
        print(f"Connection from {address} has been established.")

        drop = list()
        msg = pickle.dumps(drop)
        msg = bytes(f"{len(msg):<{HEADER_LENGTH}}", 'utf-8')+msg
        print(msg)
        clientsocket.send(msg)
        log('+', 'Message send to client !')

def handler (msg_head):

    decrypt=Security ()
    handle = MongoDAO ()
    rec_packet=pickle.loads (msg_head)
    metadata=decrypt.app_decrypt (rec_packet[1])

    if rec_packet[2]=='key':
        pub_key=handle.get_publicKey (metadata[1][0])
        li=[pub_key, 'key']
        send_to_client (pickle.dump (li))

    elif rec_packet[2]=='msg':
        active=False
        json={"drop":msg_head, "status":"Not delivered"}
        handle.insert (metadata[1][0], json)

        if active:
            send_to_client (msg_head)

    elif rec_packet[2]=='signup':
        exist=False
        exist=handle.if_user_exist (metadeta[1][0])
        if exist:
            unique=["User ID is Unique"]
            send_to_client (pickle.dump (unique))
        else:
            Error=unique=["User ID already exists - ERROR"]
            send_to_client (pickle.dump (Error))



        
'''
---------------------------
Stored Database Structure:
---------------------------
Database : BabbleZ
    Collection : Profile
    Collection : Friends
        
    Collection : user_id
        {
            "type": received/sent
            "date": ''
            "size" ''
            "payload" : ''
            "status" : ''
        }
---------------------------------------        
Incoming / Sending Packet Structure:   
---------------------------------------     
    payload:
    metadata:
        user_id
        size
        msg_id
'''

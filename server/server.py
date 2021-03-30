import threading
import socket
import pickle
from server_security import Security


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


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 27526))
server.listen(5)

while True:
    print('Hello')


# class Server:
#     def __init__(self):
#         self.server = 'None'
#         self.create_socket()
#
#
#         #     client_socket
#             # self.clientport = 27526
#         # self.clientip = '127.0.0.1'
#         # self.is_connected = False
#         # log('!',f'Server IP {self.ip}')
#         # log('!',f'Server PORT {self.port}')
#
#     def create_socket(self):
#         try:
#             self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             self.server.bind(('0.0.0.0', 27526))
#             self.server.listen(5)
#             # while True:
#             #     message = self.server.recv(1024)
#             #     print(message)
#
#         except:
#             log('-', f'Error: unable to create socket')
#             exit(-1)
#
#     def is_Active(self):
#
#         active = None  # Remaining
#         if active == 1:
#             return True
#         else:
#             return False
#
#     def send(self, drop):
#         pass
#         # clientsocket.send((pickle.dumps(drop))
#
#     def forward(self, drop):
#         pass
#         #decypted_msg_list = Security.app_decrypt(drop[1])
#         # reciever_id=""
#         # send(decypted_msg_list)
#
#     def save_messg(self):
#         pass
#
#     def recieve(self):
#         pass
#
# if __name__ == '__main__':
#     serv = Server()
#

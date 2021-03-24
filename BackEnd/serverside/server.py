import threading
import socket
import app_decrypt from server_security

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
    with open('logfile.txt','a') as file:
        file.write(typ + ' '+str(timestamp) + ' ' +text+'\n')

class Server:
    def __init__(self):
        self.socket = socket.socket()
        self.port = 27526
        self.ip = '127.0.0.1'
        self.is_connected = False
        log('!',f'Server IP {self.ip}')
        log('!',f'Server PORT {self.port}')

    def is_Active ():
        bool active=func_call ()
        if active==1:
            return TRUE
        else:
            return False
    
    def forward (self, drop):
        list decypted_msg=app_decrypt (drop[1])
        
        reciever_id=""


    
    def save_messg(self):
        pass

    def send (self, drop):
        

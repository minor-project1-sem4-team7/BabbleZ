import threading
import socket


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


class Babble:
    def __init__(self):
        self.socket = socket.socket()
        self.port = 27526
        self.ip = '127.0.0.1'
        self.is_connected = False
        log('!',f'Server IP {self.ip}')
        log('!',f'Server PORT {self.port}')

    def connect(self):
        try:
            self.socket.connect((self.ip, self.port))
        except:
            trial = 3
            while(trial):
                log(f'{4-trial}','Trying Again')
                trial -= 1
                try:
                    log('.','Connecting...')
                    self.socket.connect((self.ip, self.port))
                except:
                    log('-','Failed To connect!!!')

    def send_messg(self):
        pass

    def recieve_messg(self):
        pass

    def save_messg(self):
        pass


if __name__ == '__main__':
    bab = Babble()
    # bab.connect()

    thread1 = threading.Thread(target=bab.connect())
    # thread2 = threading.Thread(target=bab.connect())

    thread1.start()
    # thread2.start()
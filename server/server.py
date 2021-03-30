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
    with open('logfile.txt','a') as file:
        file.write(typ + ' '+str(timestamp) + ' ' +text+'\n')


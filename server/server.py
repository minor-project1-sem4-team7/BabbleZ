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
    with open('logfile.txt', 'a') as file:
        file.write(typ + ' ' + str(timestamp) + ' ' + text + '\n')


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 27526))
server.listen()

users = []


def handler():
    pass


def send_to_client():
    pass


def new_connection():
    while True:
        client, address = server.accept()
        log('+', f'{address} Connected To server')
        client.send('Connected Successfully'.encode())

        thread = threading.Thread(target=handler)
        thread.start()


if __name__ == '__main__':
    print('Starting The Server...')
    log('!', 'Starting Server')
    new_connection()

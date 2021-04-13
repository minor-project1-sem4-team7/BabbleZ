import threading
import socket
import sys
import server_security
import pickle
import rsa


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


#     "public_key": "PublicKey(17829801829231194226214196779787310317963023829419602869344533041873976224222574158174433043922296023192052210437100599571338071832061342040022133913134511566871118286989542517572424653882641916492420011134966489473064599340856406903621308337409721230686016196598878301392140688302252651981572031975362493160707097442926874311240845980743824678105382455098153027061526674516562927980333650519026758929100212289819992178108505808160984441143557608315654364284732030367230432905580718013068278346929709695720649517925041926455282674668290175741014410077074921665134298590090224248272751006128156435150629234152637120807, 65537)",
def send_to_client():
    public_key = rsa.PublicKey(
        17829801829231194226214196779787310317963023829419602869344533041873976224222574158174433043922296023192052210437100599571338071832061342040022133913134511566871118286989542517572424653882641916492420011134966489473064599340856406903621308337409721230686016196598878301392140688302252651981572031975362493160707097442926874311240845980743824678105382455098153027061526674516562927980333650519026758929100212289819992178108505808160984441143557608315654364284732030367230432905580718013068278346929709695720649517925041926455282674668290175741014410077074921665134298590090224248272751006128156435150629234152637120807,
        65537)
    user_id = 'mnChar_akash'
    msg_id = '606481a645bfe65d56bfbba9'
    payload = 'Hello Man? How are you'
    size = str(sys.getsizeof(payload))
    app_key = server_security.gen_key('abcde')

    drop = list()
    drop.append(server_security.personal_encrypt(payload, public_key))
    metadata = [server_security.app_encrypt(user_id, app_key), server_security.app_encrypt(size, app_key),
                server_security.app_encrypt(msg_id, app_key)]
    drop.append(metadata)

    # packet = str(drop)
    packet = pickle.dumps(drop)

    while True:
        msg = input()
        if msg == 'pack':
            client = users[-1]
            client.send(packet)
        else:
            for client in users:
                client.send(msg.encode())


def new_connection():
    while True:
        global client
        client, address = server.accept()
        users.append(client)
        log('+', f'{address} Connected To server')
        # client.send('Connected Successfully'.encode())

        # thread = threading.Thread(target=handler)
        thread = threading.Thread(target=send_to_client)
        thread.start()


if __name__ == '__main__':
    # public_key = rsa.PublicKey(18483481882929351299432537832232086818027691837000167407093837700224114486430532484585575673270836162242999580070429751368547283863060945848234222113005147185064597494603266104789197677335398453422170616976907864519414483354376493105947551558040395743678096829269699397346433463188079745374980230772386496842012629697786063584038670152939993133739757291746478256263355303311187779329602851813649649426698929898206237431333631949655312288424013714371276906997864204770534447115222446200362973250563174448241998921105226454648733885111154086497038974003322116661815083429786761318717647088091248515052534667309239564257, 65537)
    # user_id = 'mnChar_akash'
    # msg_id = '606481a645bfe65d56bfbba9'
    # payload = 'Hello Man? How are you'
    # size = sys.getsizeof(payload)
    # app_key = server_security.gen_key('K!!L$Y')
    #
    # drop = list()
    # drop.append(server_security.personal_encrypt(payload, public_key))
    # us_i = server_security.app_encrypt(user_id, app_key)
    # sz = server_security.app_encrypt(str(size), app_key)
    # m_i = server_security.app_encrypt(msg_id, app_key)
    # metadata = [us_i, sz, m_i]
    # drop.append(metadata)
    # packet = pickle.dumps(drop)
    #
    # print(packet)

    print('Starting The Server...')
    log('!', 'Starting Server')
    new_connection ()

    # send_thread = threading.Thread(target= send_to_client())
    # send_thread.start ()

    '''
    payload:
    metadata:
        user_id
        size
        msg_id
    '''

# Temporary Program to check programs and their working
# Security
import Security

cls = Security

# print('Private Key : ', cls.get_private_key())

pvmsg = 'Hello This is a secret message'
enc_msg = cls.personal_encrypt(pvmsg)
dec_msg = cls.personal_decrypt(enc_msg)


if pvmsg == dec_msg:
    print('[+] Independent RSA Encryption successful')
else:
    print('[*] private enc msg :', enc_msg)
    print('[*] private dec msg :', dec_msg)
    print('[-] Failed RSA Encryption')


apmsg = 'This is my app password $uperst0ng'
app_enc = cls.app_encrypt(apmsg)
app_dec = cls.app_decrypt(app_enc)


if app_dec == apmsg:
    print('[+] Independent APP Encryption successful')
else:
    print('[*] App Enc msg :', app_enc)
    print('[*] App Dec msg :', app_dec)
    print('[-] Failed App Encryption')

# combined Encryption

my_msg = text = 'Hello This is my Private secret Message - hey Devil You There ? \n' \
                'We are going to Attack on Cyber castle or Hero Emilia at Night of Dark Monday\n' \
                'Be ready ! You are our main protagonist in this attack.\n' \
                'Message For Dark Lord Arnav 😈'


def zebrish(text):
    drop = list()
    secure = Security

    encrypted_msg = secure.personal_encrypt(text)
    drop.append(encrypted_msg)

    metadata = 'This Is app Meta Data , Encrypted by App Encryption'

    secure_meta = secure.app_encrypt(metadata)
    drop.append(secure_meta)                            # Send over network

    received_metadata = secure.app_decrypt(drop[1])
    original_msg = secure.personal_decrypt(drop[0])

    if text == original_msg and metadata == received_metadata :
        print('[+] Combined Test Successfully Passed')
        # print('Received Private message',original_msg)
        # print('Received App message',received_metadata)
    else:
        print('[-] Something went wrong')
        print('[*] Plain Message : ', text)
        print('[*] Private encrypted Message : ', encrypted_msg)
        print('[*] App Message : ', metadata)
        print('[*] App encrypted Message : ', secure_meta)
        print('[*] App decrypted Message : ', received_metadata)
        print('[*] Private decrypted Message : ', original_msg)
        print('[-] Test Failed')

zebrish(my_msg)

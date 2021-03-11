# Temporary Program to check programs and their working

# Security

import Security

cls = Security.Security()

# print('Private Key : ', cls.get_private_key())

pvmsg = 'Hello This is a secret message'
enc_msg = cls.private_encrypt(pvmsg)
dec_msg = cls.private_decrypt(enc_msg)

if pvmsg == dec_msg:
    print('[+] RSA Encryption successful')
else:
    print('[*] private enc msg :', enc_msg)
    print('[*] private dec msg :', dec_msg)
    print('[-] Failed RSA Encryption')


# print('App Key : ', cls._app_key)

apmsg = 'This is my app password $uperst0ng'
app_enc = cls.app_encrypt(apmsg)
app_dec = cls.app_decrypt(app_enc)


if app_dec == apmsg:
    print('[+] APP Encryption successful')
else:
    print('[*] App Enc msg :', app_enc)
    print('[*] App Dec msg :', app_dec)
    print('[-] Failed App Encryption')
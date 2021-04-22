import pickle
import rsa
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import hashlib
KEY_SIZE = 1024


# Salting key / Passwords
def salt_key(data):
    new_pass = data[:1] + '@4fsf4f' + \
               data[1:len(data) - 3] + '%5ssg' + data[len(data) - 3:]
    return new_pass


# Hashing Password
def hash_str(string: str):
    string = salt_key(string)
    return hashlib.sha512(string.encode()).hexdigest()


# Encrypt with, receiver's public key
def personal_encrypt(plain_text: str, public_key=None):

    encrypted = list()
    offset = 0
    chuk_size = 116
    end_loop = False

    __server_public_key__ = rsa.PublicKey(157137637721861869372539893459600696742127499758127772090085112140787972009214342489665530996268305128037221399721176471559193370133031726130729193098952822312718353677752558323517006429252983185444022055723152643529270527892933839066752166883567099046052682883104837595785078185695586176198813398487786120801, 65537)

    if not public_key:
        public_key = __server_public_key__

    while not end_loop:

        chunk = plain_text[offset: offset + chuk_size]

        if len(chunk) % chuk_size != 0:
            end_loop = True

        enc_chunk = rsa.encrypt(chunk.encode(), public_key)

        offset += chuk_size
        encrypted.append(enc_chunk)

    return pickle.dumps(encrypted)


# Generating Salted App Key , (App Encryption)
# def gen_key(data):
#     data = salt_key(data)
#     data = data.encode()
#     kdf = PBKDF2HMAC(
#         algorithm=hashes.SHA256(),
#         length=32,
#         salt=b'@0#5T13dgrgjjss9e23sTh',
#         iterations=100000,
#         backend=default_backend()
#     )
#     return base64.urlsafe_b64encode(kdf.derive(data))


# Decrypting Private Key Structure (Reload, Reform Public, Private Key for Runtime)
def get_key_list(key: str) -> list:
    key = key[11:-1]
    key_numeric = [i for i in map(int, key.split(','))]
    return key_numeric


class Security:

    def __init__(self, passw, privateKey=None, publicKey=None) -> None:

        self.password = passw

        # New user case
        if privateKey is None and publicKey is None:
            self.generate_keys()
            self.publicKey = str(self._public_key)
            self.privateKey = str(self._private_key)


        # Existing user case
        else:

            keys = get_key_list(privateKey)
            self.publicKey = 'PublicKey({},{})'.format(keys[0], keys[1])
            self.privateKey = privateKey
            self._public_key = rsa.PublicKey(keys[0], keys[1])
            self._private_key = rsa.PrivateKey(keys[0], keys[1], keys[2], keys[3], keys[4])
            # self._app_key = gen_key(passw)

    # personal Decryption for received messages
    def personal_decrypt(self, crypt_text):

        encrypted = pickle.loads(crypt_text)
        decrypted_text = ''

        for chunk in encrypted:
            decrypted_text += rsa.decrypt(chunk,self._private_key).decode()

        return decrypted_text

    # Meta Data Encryption App Encrypt
    # def app_encrypt(self, data):
    #     data = data.encode()
    #     func = Fernet(self._app_key)
    #     encrypted_data = func.encrypt(data)
    #     return encrypted_data

    # Meta Data Decryption App Decrypt
    # def app_decrypt(self, data):
    #     data = data
    #     func = Fernet(self._app_key)
    #     decrypted_data = func.decrypt(data)
    #     return decrypted_data.decode()

    # Fetch public key (Transfer Purpose)
    def get_my_publickey(self):
        return self.publicKey

    # New Key Generation
    def generate_keys(self):
        self._public_key, self._private_key = rsa.newkeys(KEY_SIZE)
        # self._app_key = gen_key(self.password)

    '''
        REMAINING :
            - SQL sync
            - First time cryptography
            - Key pickup form DB
            - password pickup
    '''

    # @property
    # def public_key(self):
    #     return self.public_key


if __name__ == '__main__':
    pub_k, priv_k = rsa.newkeys(KEY_SIZE)
    print(pub_k, '\n\n', priv_k)

    pub_k, priv_k = rsa.newkeys(KEY_SIZE)
    print(pub_k, '\n\n', priv_k)

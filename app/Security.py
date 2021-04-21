import rsa
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import hashlib

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
    __server_public_key__ = rsa.PublicKey(
        531836556116849503526789038592954213414151379898321835881401907556007177415927997307542592331199274089794331573843691592574639966270561486557382534282742103050057822993660888083548379856155488483196639832097391417134087217005299569802699831391478549250744498375602059643144903775349274801998146688120183504125221051061736348327457268507586608176443284233413990577635177136336631459383851827187507721004587701804374282750434372917940361127765542157619677292146401841569985916480798394424532280393237433015726920840531167288665933370139294868651026141601666325426407672025889314600906028786618408177562737233790002944266034792992474306740850812523601523756217918206069415070327585539353356359071939307735577061091608639360563326396192850344390658852913223887011225691903782488742287948888014633114365077164593903473318600607600949451658093178850075458821016403433532568744679880492952441636867853655522362814535616187809821323397068788947480892419246810990841597653670945038818458829019200666865229015233677540241824247978388149314379895411043381152108020013195083056299043554246377658123133279533462604856780710681653462894342224519486425570059768811070058412378593332019844589337496030320729967749686813819445032235455418790559505833,
        65537)

    if not public_key:
        public_key = __server_public_key__
    return rsa.encrypt(plain_text.encode(), public_key)


# Generating Salted App Key , (App Encryption)
def gen_key(data):
    data = salt_key(data)
    data = data.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'@0#5T13dgrgjjss9e23sTh',
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(data))


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
            self._app_key = gen_key(passw)

    # personal Decryption for received messages
    def personal_decrypt(self, crypt_text):
        return rsa.decrypt(crypt_text, self._private_key).decode()

    # Meta Data Encryption App Encrypt
    def app_encrypt(self, data):
        data = data.encode()
        func = Fernet(self._app_key)
        encrypted_data = func.encrypt(data)
        return encrypted_data

    # Meta Data Decryption App Decrypt
    def app_decrypt(self, data):
        data = data
        func = Fernet(self._app_key)
        decrypted_data = func.decrypt(data)
        return decrypted_data.decode()

    # Fetch public key (Transfer Purpose)
    def get_my_publickey(self):
        return self.publicKey

    # New Key Generation
    def generate_keys(self):
        self._public_key, self._private_key = rsa.newkeys(2048)
        self._app_key = gen_key(self.password)

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
    pubkey, privkey = rsa.newkeys(2048)

    print(type(pubkey))

    st_pub = str(privkey)
    st_prvk = str(privkey)
    print(type(st_pub), '\n\n\n', st_prvk)

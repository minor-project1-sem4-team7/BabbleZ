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

    # Testing Program

    # print(gen_key('K!!L$Y'))
    # obj = Security()
    # obj.password = 'super_usrre'
    # obj.generate_keys()
    # print(obj.public_key)
    # obj.password = 'Akash_password_mnChar'
    # print(hash_str('Akash_password_mnChar'))
    # print(hash_str('Himanshu_password_Otakuu'))
    # print(hash_str('Amarnath_password_arch'))
    # print(hash_str('Swati_password_Swati-P11'))

    # obj.fetch_keys()
    # print(obj._private_key)
    # print(obj.public_key)

    st = "PrivateKey(18483481882929351299432537832232086818027691837000167407093837700224114486430532484585575673270836162242999580070429751368547283863060945848234222113005147185064597494603266104789197677335398453422170616976907864519414483354376493105947551558040395743678096829269699397346433463188079745374980230772386496842012629697786063584038670152939993133739757291746478256263355303311187779329602851813649649426698929898206237431333631949655312288424013714371276906997864204770534447115222446200362973250563174448241998921105226454648733885111154086497038974003322116661815083429786761318717647088091248515052534667309239564257, 65537, 8262951496193968817168538282325032876002491957831925548820288645210584955421239005956760243457725527280702529821374961557527783124341358186391904412268257659459886436621854682669544128516296197390218574792704069681093207399126027969209017281039222340025952986922557531523502870202852745470818069213867537848300200000934738103607357432908995795369198427366945450405258697508611089095952396328525422407005877336566271167965051705110606093790056833897810913829375853227278988750233158244855094991808620324502281004830481592465933467295195242469923045057070768936317143526320071008468186302193088124630688486688635465673, 2565601716845612550796498649207323359575346478866593512704791577976882656113186297140219716888479284724181037044800426222102524438759567537531748989847271923994407102774550512486745248707614472763449288317370791972687748995621091227023528282988276174396488957955517874660270825066890492426194435004659866890730671264840343588407, 7204345772598971123328150306304454569943760126123876964932967110542726373026082930436987839494482406599848657006704425261133786077508337209852988232031808105045695293006651360566674315764179185388879516856811607037018491578378104252229744222530425023249557714982053464586679043396157136551)"
    print(get_key_list(st))

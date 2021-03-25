import rsa
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Security:

    def __init__(self) -> None:
        self._public_key = None
        self._private_key = None
        self.sender_key = None
        self._app_key = None
        self.key_status = False
        self.password = 'Hello_wwrsfaffasfrrssvg h7'            # test password variable REMAINING

        self.fetch_keys()

    # Encrypt with, receiver's public key
    def personal_encrypt(self, plain_text: str, public_key):
        return rsa.encrypt(plain_text.encode(), public_key)

    def personal_decrypt(self, crypt_text):
        return rsa.decrypt(crypt_text, self._private_key).decode()

    def app_encrypt(self, data):
        data = data.encode()
        func = Fernet(self._app_key)
        encrypted_data = func.encrypt(data)
        return encrypted_data

    def app_decrypt(self, data):
        data = data
        func = Fernet(self._app_key)
        decrypted_data = func.decrypt(data)
        return decrypted_data.decode()

    def get_private_key(self) -> str:
        return self._public_key

    def fetch_keys(self):
        def salt_key(data):
            new_pass = data[:1] + '@4fsf4f' + \
                       data[1:len(data) - 3] + '%5ssg' + data[len(data) - 3:]
            return new_pass

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

        def generate_keys(password) -> None:
            self._public_key, self._private_key = rsa.newkeys(2048)
            self._app_key = gen_key(password)       # generate REMAINING

        # get database keys or generate keys
        generate_keys(self.password)
        # get local keys function REMAINING


        '''
            REMAINING :
                - SQL sync
                - First time cryptography
                - Key pickup form DB
                - password pickup
        '''

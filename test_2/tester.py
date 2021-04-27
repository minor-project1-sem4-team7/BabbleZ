import threading

import client
import Security

if __name__ == '__main__':
    user_object = client.Babble('vmTesting', 'vmTesting')


    def receive():
        while True:
            user_object.received_message()

    # Receive Message Thread
    thread = threading.Thread(target=receive)
    thread.start()

    # user_object.send_msg('Hello Testing', 'test_2')
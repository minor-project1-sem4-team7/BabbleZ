import threading
import client
import Security

if __name__ == '__main__':
    user_object = client.Babble('vmTesting_1', 'vmTesting_1', 'vmTest User one')
    # user_object = client.Babble('testing_show', 'testingshow', 'testing_ss')
    user_object = client.Babble('vmTesting_1', 'vmTesting_1')
    # print(user_object.logged_in)

    def receive():
        while True:
            user_object.received_message()

    # Receive Message Thread
    thread = threading.Thread(target=receive)
    thread.start()

    user_object.send_msg('Hello Testing, This is a message form VmTesting 1 user', 'vmTesting')
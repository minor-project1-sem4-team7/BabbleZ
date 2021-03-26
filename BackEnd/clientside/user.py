import re


class User:

    def __init__(self):
        self.user_id = None
        self.user_name = None
        self.user_password = None
        self.user_dp = None
        self.user_about = None

        # Testing Purpose
        self.user_id = 'SuperHash'

    def check_userid(self, id) -> bool:
        pass

    def get_user_id(self):
        # get id REMAINING
        id = input('Enter UserID : ')  # TEMP
        if not self.check_userid(id):
            self.user_id = id
        else:
            print('Re enter name, Duplicate')  # TEMP

    def get_user_name(self):

        # get username REMAINING
        name = input('Enter username : ')  # TEMP

        allowed_char = '[^a-zA-Z #_]'
        if re.findall(allowed_char, name):
            print('Not Allowed')  # TEMP
        else:
            self.user_name = name

    def get_user_password(self):

        # get user password REMAINING

        password = input('Enter Password : ')  # TEMP

        if len(password) >= 8:

            allowed_char = '[^a-zA-Z0-9@_$* ]'
            if re.findall(allowed_char, password):
                print('Bad Character !')  # TEMP
            else:
                self.user_password = password
        else:
            print('Min Length = 8')  # TEMP

    def get_user_dp(self):
        # get user dp REMAINING
        pass

    def get_user_about(self):

        # get user about REMAINING

        about = input('Enter About : ')  # TEMP
        res_char = '[<;>\\;{}=]'
        if re.findall(res_char, about):
            print('Character Not allowed')  # TEMP
        else:
            self.user_about = about

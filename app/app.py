# from flask import Flask, render_template,url_for,redirect,request
# import client
# import logging
#
# babbleZ_app = Flask(__name__)
#
# logging.basicConfig(filename='logfile.txt', level=logging.DEBUG,
#                     format=f'%(levelname)s %(asctime)s %(name)s %(threadName)s : %(message)s')
#
#
# @babbleZ_app.route('/')
# def my_home():
#     return render_template('index.html')
#
#
# @babbleZ_app.route('/<string:page_name>')
# def html_page(page_name):
#     try:
#         return render_template(page_name + '.html')
#     except:
#         return render_template('error404.html')
#
#
# def login_user(username, password):
#     return client.Babble(username, password)
#
#
# def create_user(userid, username, password):
#     pass
#
#
# if __name__ == "__main__":
#     # Mongo Server start
#     # os check, specific based changed
#     babbleZ_app.run(debug=True)
#     usr = client.Babble()



from flask import Flask, render_template, url_for, redirect, request
import client
# import logging

babbleZ_app = Flask(__name__)

# logging.basicConfig(filename='logfile.txt', level=logging.DEBUG,
#                     format=f'%(levelname)s %(asctime)s %(name)s %(threadName)s : %(message)s')

users = {}


@babbleZ_app.route('/', methods=["POST", "GET"])
def my_home():
    # login
    if request.method == "POST" and 'loginid' in request.form and 'loginpassword' in request.form:
        loginid = request.form['loginid']
        loginpassword = request.form['loginpassword']

        try:
            usr = login_user(loginid, loginpassword)
            if usr.logged_in:
                return render_template("ui_chat")

        except:
            return render_template('error404.html')

        # make condition
        # sd = server__database()
        # ok = sd.check_client_existence(loginid)
        # if ok:
        #     # password check
        #     pswd_check = sd.password_check(loginid, loginpassword)
        #     if pswd_check:
        #         return render_template("ui_chat.html",
        #                                message_backend=[{'sent': 'hey how are you'}, {'receive': 'fine'},
        #                                                 {'receive': 'dfajaslfjs'}, {'sent': 'heasdfadsfe you'}])
        #     else:
        #         return "<h1>password doesn't match</h1>"
        #
        #
        # else:
        #     return "<h1>404 Error </h1>"



    # signup
    # elif request.method == "POST" and 'signupid' in request.form and 'signuppassword' in request.form:
    #     signupid = request.form['signupid']
    #     signuppassword = request.form['signuppassword']
    #
    #     sd = server__database()
    #     ok = sd.check_client_existence(signupid)
    #     if ok:
    #         return "<h1>name already exist"
    #
    #     database = {'userid': signupid, 'username': 'afhkasjd', 'password': signuppassword, 'public_key': 'agasgads',
    #                 'app_key': 'agdfadgfda'
    #         , 'client_socket': 'afdagdsd'}
    #
    #     sd.create_database(database)
    #     # users[signupid]=signuppassword
    #     return render_template("index.html")

    else:
        return render_template('index.html')


@babbleZ_app.route('/<string:page_name>')
def html_page(page_name):
    try:
        return render_template(page_name + '.html')
    except:
        return render_template('error404.html')


def login_user(user_id, password):
    return client.Babble(user_id, password)


def create_user(userid, username, password):
    pass


if __name__ == "__main__":
    # Mongo Server start
    # os check, specific based changed
    babbleZ_app.run(debug=True)
    # usr = client.Babble()

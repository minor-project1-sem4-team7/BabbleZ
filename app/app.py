from flask import Flask, render_template, url_for, redirect, request
import client
import logging

babbleZ_app = Flask(__name__)

logging.basicConfig(filename='app_log.txt', level=logging.DEBUG,
                    format=f'%(levelname)s %(asctime)s %(name)s %(threadName)s : %(message)s')

users = {}


@babbleZ_app.route('/', methods=["POST", "GET"])
def my_home():
    return redirect('index')


@babbleZ_app.route('/<string:page_name>', methods=["POST", "GET"])
def html_page(page_name):
    try:
        if page_name == 'index':
            # Login
            if request.method == "POST" and 'loginid' in request.form and 'loginpassword' in request.form:
                loginid = request.form['loginid']
                loginpassword = request.form['loginpassword']

                try:
                    usr = login_user(loginid, loginpassword)
                    usr.initiate_user_working()
                    return render_template("ui_chat.html")

                except:
                    return render_template('error404.html')
            # Sign up
            elif request.method == "POST" and 'signupid' in request.form and 'signuppassword' in request.form:
                signupid = request.form['signupid']
                signup_name = request.form['signup_name']
                signuppassword = request.form['signuppassword']
                usr = create_user(signupid, signup_name, signuppassword)  # REMAIN
                if usr.success:
                    return "<h1>Success</h1>"

                return redirect("index")
            # Default
            else:
                return render_template('index.html')
        else:
            return render_template(page_name + '.html')

    except:
        return render_template('error404.html')


def login_user(user_id, password):
    return client.Babble(user_id, password)


def create_user(userid, username, password):
    return client.Babble(userid, password, username)


if __name__ == "__main__":

    babbleZ_app.run(debug=True)


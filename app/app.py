from flask import Flask, render_template, url_for, redirect, request, after_this_request
import client
import logging
import threading

babbleZ_app = Flask(__name__)

logging.basicConfig(filename='app_log.txt', level=logging.DEBUG,
                    format=f'%(levelname)s %(asctime)s %(name)s %(threadName)s : %(message)s')

users = {}
usr = None


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
                    # Babble Object
                    user_object = login_user(loginid, loginpassword)

                    def receive():
                        while True:
                            user_object.received_message()

                    # Receive Message Thread
                    thread = threading.Thread(target=receive)
                    thread.start()

                    # Main Chat App Model
                    return render_template("ui_chat.html")
                except:
                    return render_template('error404.html')
            # Sign up
            elif request.method == "POST" and 'signupid' in request.form and 'signuppassword' in request.form:
                signupid = request.form['signupid']
                signup_name = request.form['signup_name']
                signuppassword = request.form['signuppassword']

                # Babble Object
                user_object = create_user(signupid, signup_name, signuppassword)  # REMAIN
                if user_object.success:
                    script = '''
                    <script>
                         setTimeout(function(){
                            alert('Signup Successful');
                            window.location.href = 'index';
                         }, 5);
                    </script>
                    '''
                    return script
                else:
                    script = '''<script>
                        setTimeout(function(){
                            alert('Signup Failure');
                            window.location.href = 'index';
                        }, 5);
                    </script>
                    '''
                    return script
            # Default
            else:
                return render_template('index.html')
        else:
            return render_template(page_name + '.html')

    except:
        return render_template('error404.html')


# returns Babble object (ALREADY EXISTED USER)
def login_user(user_id, password):
    return client.Babble(user_id, password)


# returns Babble object (CREATE NEW)
def create_user(userid, username, password):
    return client.Babble(userid, password, username)


if __name__ == "__main__":
    babbleZ_app.run(debug=True)

from flask import Flask, render_template, url_for, redirect, request, jsonify
import client
import logging
import threading

babbleZ_app = Flask(__name__)

logging.basicConfig(filename='app_log.txt', level=logging.DEBUG,
                    format=f'%(levelname)s %(asctime)s %(name)s %(threadName)s : %(message)s')

users = {}
usr = None

client_database = list()
friend_list = list()

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
                    global client_database
                    global friend_list
                    user_object = login_user(loginid, loginpassword)
                    client_database = user_object.get_collection(user_object.user_id)       # TEMP
                    user_object.get_collection(user_object.user_id)  # TEMP

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


@babbleZ_app.route('/inner_interface/<doc>', methods=['GET', 'POST'])
def get_javascript_data(doc):
    if request.method == "POST":
        userid = int(request.form['userid'])
        print(userid)

    # print(client_database)
    return render_template("userdata.html", message_backend=client_database[userid])
    # return jsonify({'messages': client_database[userid]})


@babbleZ_app.route('/refreshmessages')
def refresh_messages():
    return render_template("userdata.html", message_backend=client_database)


@babbleZ_app.route('/inner_interface', methods=["POST", "GET"])
def inner_interface():
    if request.method == "POST" and 'searchfriends' in request.form:
        friend = request.form['searchfriends']
        if friend not in friend_list:
            friend_list.append(friend)
            length = len(friend_list)
            return render_template("ui_chat.html", friendlist=friend_list, len=length)

        else:
            return "<h1> friend already exist </h1>"


    elif request.method == "POST" and 'messagetype in request.form':
        # print("hey how are you")
        # msg=str(request.json['message'])
        # client_datatbase.append({'sent':msg})
        try:
            msg = request.form['message']
            userid = int(request.form['userid'])
            client_database[userid].append({'sent': msg});

            return jsonify({'sent': msg})
        except:
            print("caught an exception")
            return jsonify({'sent': 'over'})
        # msg=request.form['messagetype']
        # client_database.append({'sent':msg})
        # return render_template("ui_chat.html",friendlist=friend_list,message_backend=client_database)







    else:
        # friend_list=['himanshu','amarnath','rahul','arnav','akash',]
        length = len(friend_list)
        return render_template("ui_chat.html", friendlist=friend_list, message_backend=client_database, len=length)


# @babbleZ_app.route('/anotheruser',methods=["POST","GET"])
# def anotheruser():
#     if request.method=="POST" and 'messagetype' in request.form:
#         msg=request.form['messagetype']
#         anotheruser_database.append({'sent':msg})
#         return render_template("ui_chat.html",message_backend=anotheruser_database)

#     else:
#         return render_template("ui_chat.html",message_backend=anotheruser_database)


# returns Babble object (ALREADY EXISTED USER)
def login_user(user_id, password):
    return client.Babble(user_id, password)


# returns Babble object (CREATE NEW)
def create_user(userid, username, password):
    return client.Babble(userid, password, username)


if __name__ == "__main__":
    babbleZ_app.run(debug=True)

# Friend List
# client Database

from flask import Flask, render_template
import client

babbleZ_app = Flask(__name__)


@babbleZ_app.route('/')
def my_home():
    return render_template('index.html')


@babbleZ_app.route('/<string:page_name>')
def html_page(page_name):
    try:
        return render_template(page_name+'.html')
    except:
        return render_template('error404.html')


def login_user(username, password):
    return client.Babble(username, password)


def create_user(userid, username, password):
    pass


if __name__ == "__main__":
    # Mongo Server start
    # os check, specific based changed
    babbleZ_app.run(debug=True)
    usr = client.Babble()

# command line commands
# pip install flask
# python -c "import flask; print(flask.__version__)"

# commands after .py-file is saved:

# export FLASK_APP=hello
# export FLASK_ENV=development # not required line
# flask run

# check in browser
# http://127.0.0.1:5000/


from flask import Flask

# to let us create dictionary to send parameters from URL to web-page
from flask import request

# w/ the command line command:
# curl v=3 http://127.0.0.1:5000/
# we can send v=3 get-command that will be accepted
# but if we try POST-command like below
# curl -d v=3 http://127.0.0.1:5000/
# this method isn't allowed


app = Flask(__name__)
# создаете ваш экземпляр приложения Flask с именем app
# передаете специальную переменную __name__, которая содержит имя текущего модуля Python.
# Она указывает экземпляру его расположение.
# Это необходимо, так как Flask устанавливает ряд путей за кадром.
# app используется для обработки поступающих веб-запросов и отправки ответов пользователю


# @app.route("/")
# декоратор, который превращает стандартную функцию Python в функцию просмотра Flask,
# конвертирующую возвращаемое значение функции в ответ HTTP,
# который отображается клиентом HTTP, например веб-браузером
# функция будет отвечать на веб-запросы для URL /
@app.route("/", methods=["GET", "POST"])
# method added


def index():
    return str(request.args)


# http://127.0.0.1:5000/hello
@app.route("/hello")
def hello():
    return "Hello World"

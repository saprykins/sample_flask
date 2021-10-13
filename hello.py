# command line commands
# pip install flask
# python -c "import flask; print(flask.__version__)"

# commands after file is saved:
# export FLASK_APP=hello
# export FLASK_ENV=development # not required line
# flask run

# check in browser
# http://127.0.0.1:5000/


from flask import Flask

app = Flask(__name__)
# создаете ваш экземпляр приложения Flask с именем app
# передаете специальную переменную __name__, которая содержит имя текущего модуля Python.
# Она указывает экземпляру его расположение.
# Это необходимо, так как Flask устанавливает ряд путей за кадром.
# app используется для обработки поступающих веб-запросов и отправки ответов пользователю


@app.route("/")
# декоратор, который превращает стандартную функцию Python в функцию просмотра Flask,
# конвертирующую возвращаемое значение функции в ответ HTTP,
# который отображается клиентом HTTP, например веб-браузером

# функция будет отвечать на веб-запросы для URL /
def index():
    return "Index Page"


# http://127.0.0.1:5000/hello
@app.route("/hello")
def hello():
    return "Hello World"

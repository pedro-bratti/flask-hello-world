from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello():
    return 'Mi vieja mula ya no es lo que era!!'

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8888)

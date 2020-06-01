from flask import Flask
from flask_restplus import Api, Resource

from functions import hello, snore, np_estimate_pi, estimate_pi

app = Flask(__name__)
api = Api(app=app)


@api.route('/hello')
class Hello(Resource):

    def get(self):
        return hello()


@api.route('/sleep/<float:t>')
class Sleep(Resource):

    def get(self, t: float):
        return snore(t=t)


@api.route('/estimate-pi-np/<int:n>')
class EstimatePiNumpy(Resource):

    def get(self, n: int):
        return np_estimate_pi(n=n)


@api.route('/estimate-pi/<int:n>')
class EstimatePi(Resource):

    def get(self, n: int):
        return estimate_pi(n=n)


def main():
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host="0.0.0.0")


if __name__ == "__main__":
    main()

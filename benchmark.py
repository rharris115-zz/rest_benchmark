from flask import Flask
from flask_restplus import Api, Resource
import numpy as np
from random import random
from time import time

app = Flask(__name__)
api = Api(app=app)


def timed(func):
    def _t(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        elapsed = time() - start
        return {**result, 'elapsed': elapsed}

    return _t


@api.route('/hello')
class Hello(Resource):

    @timed
    def get(self):
        return {'message': 'Hello World!'}


@api.route('/estimate-pi-np/<int:n>')
class EstimatePiNumpy(Resource):

    @timed
    def get(self, n: int):
        inside_unit_circle = ((np.random.uniform(size=n) ** 2
                               + np.random.uniform(size=n) ** 2) < 1).sum()
        return {'estimated_pi': 4 * inside_unit_circle / n}


@api.route('/estimate-pi/<int:n>')
class EstimatePi(Resource):

    @timed
    def get(self, n: int):
        inside_unit_circle = sum(1 if random() ** 2 + random() ** 2 < 1 else 0 for i in range(n))
        return {'estimated_pi': 4 * inside_unit_circle / n}


def main():
    app.run()


if __name__ == "__main__":
    main()

from flask import Flask
from flask_restplus import Api, Resource
import numpy as np
from random import random
from time import time, sleep

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

    def get(self):
        return {'message': 'Hello World!'}


@api.route('/sleep/<float:t>')
class Sleep(Resource):

    @timed
    def get(self, t: float):
        sleep(t)
        return {'slept': t}


@api.route('/estimate-pi-np/<int:n>')
class EstimatePiNumpy(Resource):

    @timed
    def get(self, n: int):
        # Estimate Pi by sampling uniformly distributed points in the unit square. The fraction that are at most 1 from
        # the origin will roughly equal Pi / 4.
        return {'estimatedPi': 4 * ((np.random.uniform(size=n) ** 2
                                     + np.random.uniform(size=n) ** 2) < 1).mean()}


@api.route('/estimate-pi/<int:n>')
class EstimatePi(Resource):

    @timed
    def get(self, n: int):
        # Estimate Pi by sampling uniformly distributed points in the unit square. The fraction that are at most 1 from
        # the origin will roughly equal Pi / 4.
        return {'estimatedPi': sum(4 if random() ** 2 + random() ** 2 < 1 else 0
                                   for _ in range(n)) / n}


def main():
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host="0.0.0.0")


if __name__ == "__main__":
    main()

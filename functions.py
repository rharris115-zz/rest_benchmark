from random import random
from time import time, sleep
from typing import Dict, Any

import numpy as np


def timed(func):
    def _t(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        elapsed = time() - start
        return {**result, 'elapsed': elapsed}

    return _t


@timed
def hello() -> Dict[str, Any]:
    return {'message': 'Hello World!'}


@timed
def snore(t: float) -> Dict[str, Any]:
    sleep(t)
    return {'slept': t}


@timed
def np_estimate_pi(n: int) -> Dict[str, Any]:
    # Estimate Pi by sampling uniformly distributed points in the unit square. The fraction that are at most 1 from
    # the origin will roughly equal Pi / 4.
    return {'estimatedPi': 4 * ((np.random.uniform(size=n) ** 2 + np.random.uniform(size=n) ** 2) < 1).mean()}


@timed
def estimate_pi(n: int) -> Dict[str, Any]:
    return {'estimatedPi': sum(4 if random() ** 2 + random() ** 2 < 1 else 0 for _ in range(n)) / n}

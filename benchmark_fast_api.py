from fastapi import FastAPI, Path

from functions import hello, snore, np_estimate_pi, estimate_pi

app = FastAPI()


@app.get("/hello")
async def _hello():
    return hello()


@app.get('/sleep/{t}')
def _snore(t: float = Path(..., title='The number of seconds to sleep.')):
    return snore(t=t)


@app.get('/estimate-pi-np/{n}')
def _np_estimate_pi(n: int = Path(..., title='The size of the sample from which to estimate pi.')):
    return np_estimate_pi(n=n)


@app.get('/estimate-pi/{n}')
def _estimate_pi(n: int = Path(..., title='The size of the sample from which to estimate pi.')):
    return estimate_pi(n=n)

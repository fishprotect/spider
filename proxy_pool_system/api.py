from db import RedisClient
from flask import Flask,g
__all__ = ['app']
app = Flask(__name__)

def get_conn():
    if not hasattr(g,'redis'):
        g.redis = RedisClient()
    return g.redis

@app.route('/')
def index():
    return '<h1>welcome to proxy pool system</h1>'

@app.route('/random')
def get_proxy():
    con = get_conn()
    return con.random()
@app.route('/count')

def get_count():
    con = get_conn()
    return str(con.count())
if __name__=="__main__":
    app.run()


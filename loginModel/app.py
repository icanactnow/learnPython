# -*-coding:utf-8-*-
# import flask
import base64
import random

import time

import requests
from flask import Flask, request, redirect

app = Flask(__name__)
user = {"eric": ["1234"]}
redirect_uri = 'http://localhost:5000/client/passport'
client_id = '1234'
user[client_id] = []
auth_code = {}
oauth_redirect_uri = []


def gen_token(uid):
    token = base64.b64encode(':'.join([str(uid), str(random.random()), str(time.time() + 7200)]))
    user[uid].append(token)
    return token


def gen_auth_code(uri):
    code = random.randint(1, 10000)
    user[code] = uri
    return code


def verify_token(token):
    _token = base64.b64decode(token)
    if not user.get(_token.split(':')[0])[-1] == token:
        return -1
    if _token.split(':')[-1] >= time.time():
        return 1
    else:
        return 0


@app.route('/oauth', methods=['GET', 'POST'])
def oauth():
    if request.args.get('redirect_uri'):
        oauth_redirect_uri.append(request.args.get('redirect_uri'))
    if request.args.get('user'):
        # print '1234'
        if user[request.args.get('user')][0]==request.args.get('pw') and oauth_redirect_uri:
            uri = oauth_redirect_uri[0]+ '?code =%s' % gen_auth_code(oauth_redirect_uri[0])
            print '1234'
            return redirect(uri)
    if request.args.get('code'):
        if auth_code.get(request.args.get('code'))==request.args.get('oauth_redirect_uri'):
            return gen_token(request.args.get('client_id'))
    return 'plase login'
@app.route('/client/login',methods=['GET','POST'])
def client_login():
    uri = 'http://localhost:5000/oauth?response_type=code&client_id=%s&redirect_uri=%s' % (client_id, redirect_uri)
    return redirect(uri)
@app.route('/client/passport', methods=['POST', 'GET'])
def client_passport():
    code = request.args.get('code')
    uri = 'http://localhost:5000/oauth?grant_type=authorization_code&code=%s&redirect_uri=%s&client_id=%s' % (code, redirect_uri, client_id)
    return redirect(uri)

@app.route('/test1', methods=['POST', 'GET'])
def test():
    token = request.args.get('token')
    if verify_token(token) == 1:
        return 'data'
    else:
        return 'error'

if __name__ == '__main__':
    app.run(debug=True)































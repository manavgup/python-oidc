import datetime
import flask
import logging
from flask import Flask, jsonify, session

from flask_session import Session 
from flask_pyoidc import OIDCAuthentication
from flask_pyoidc.provider_configuration import ProviderConfiguration, ClientMetadata
from flask_pyoidc.user_session import UserSession

app = Flask(__name__)
# See https://flask.palletsprojects.com/en/2.0.x/config/

OIDC_REDIRECT_URI = 'https://localhost:5000/redirect_uri'
ISSUER = 'https://preprod.login.w3.ibm.com/oidc/endpoint/default'
CLIENT_ID = 'ZWZhODJhYzctMjYxZC00'
CLIENT_SECRET = 'ZDk0NmVhMDAtNTcxZi00'
PROVIDER_NAME = 'preprod'
SECRET_KEY = 'dev_key'

app.config.update({'OIDC_REDIRECT_URI': OIDC_REDIRECT_URI,
                   'SECRET_KEY': 'dev_key',  # make sure to change this!!
                   'SESSION_TYPE': 'filesystem',
                   'DEBUG': True})

#app.config['SESSION_TYPE'] = 'filesystem'
Session(app) # use server-side session 


PROVIDER_CONFIG1 = ProviderConfiguration(issuer=ISSUER,
                                         client_metadata=ClientMetadata(CLIENT_ID, CLIENT_SECRET))
auth = OIDCAuthentication({PROVIDER_NAME: PROVIDER_CONFIG1}, app=app)


@app.route('/')
@auth.oidc_auth(PROVIDER_NAME)
def index():
    user_session = UserSession(session)
    return jsonify(access_token=user_session.access_token,
                   id_token=user_session.id_token,
                   userinfo=user_session.userinfo)

@app.route('/logout')
@auth.oidc_logout
def logout():
    return "You've been successfully logged out!"


@auth.error_view
def error(error=None, error_description=None):
    return jsonify({'error': error, 'message': error_description})


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    auth.init_app(app)
    app.run(ssl_context='adhoc', debug=True)

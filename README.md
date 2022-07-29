# python-oidc
OIDC authentication example with python


## Environment varibles
`OIDC_REDIRECT_URI = 'https://example.com/redirect_uri'` # must be registeed with the Identity Provider (IdP) <br/>
`ISSUER = 'https://provider.com/oidc/endpoint/default'` # Issuer URI to call<br/>
`CLIENT_ID = 'client_ID'` # registered client ID <br/>
`CLIENT_SECRET = 'client_secret'` # client secret registered with IdP <br/>
`PROVIDER_NAME = 'provider'` # friendly name to remember the provider<br/>
`SECRET_KEY = 'dev_key'` # make sure to change this!<br/>

## Routes

The app has two routes: <br/>
`/` - protected URL behind `@auth.oidc_auth(PROVIDER_NAME)` decorator <br/>
`/logout` - logout and terminate session.<br/>

## Install / configure

`pip install -r requirements.txt`

## Run

`python app.py`


## Testing

`podman run -d --name flask-oidc -e OIDC_REDIRECT_URI='example.com/redirect_uri' -e ISSUER='https://idp.com/oidc/endpoint/default' -e CLIENT_ID='client_id' -e CLIENT_SECRET='client_secret' -p 5000:5000 docker.io/manavg/flask-oidc:v1` 

# python-oidc
OIDC authentication example with python


## Environment varibles
`OIDC_REDIRECT_URI = 'https://example.com/redirect_uri'` # must be registeed with the identity provider <br/>
`ISSUER = 'https://provider.com/oidc/endpoint/default'` # Issuer URI to call<br/>
`CLIENT1 = 'client_ID'` # registered client ID <br/>
`PROVIDER_NAME = 'preprod'` # friendly name to remember the provider<br/>
`SECRET_KEY = 'dev_key'` # make sure to change this!<br/>

## Routes

The app has two routes: <br/>
`/` - protected URL behind `@auth.oidc_auth(PROVIDER_NAME)` decorator <br/>
`/logout` - logout and terminate session.<br/>

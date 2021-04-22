import os
import requests
import asana
from dotenv import load_dotenv


load_dotenv('.env')


def secret_auth() -> asana.Client:
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')
    redirect_uri = os.environ.get('redirect_uri')

    client = asana.Client.oauth(
      client_id=client_id,
      client_secret=client_secret,
      redirect_uri=redirect_uri,
      # response_type='code'
    )

    url, state = client.session.authorization_url()

    req = requests.get(url)
    response = req.text
    print(response)

    return client


def token_auth(token: str) -> asana.Client:
    return asana.Client.access_token(token)

if __name__ == '__main__':

    secret = False

    if secret:
        client = secret_auth()
    else:  # auth with token

        token = os.environ.get('RealBkk_token')
        # token = os.environ.get('personal_Apps_token')
        client = token_auth(token)

    print(f'Authorized = {client.session.authorized}')










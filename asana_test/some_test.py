import os
import asana
from dotenv import load_dotenv


load_dotenv('.env')


# client_id = os.environ.get('client_id')
# client_secret = os.environ.get('client_secret')
# redirect_uri = os.environ.get('redirect_uri')
# client = asana.Client.oauth(
#   client_id='1200227892108962',
#   client_secret='06373d89fe962454370fcf62de8711ad',
#   redirect_uri='urn:ietf:wg:oauth:2.0:oob'
# )
#
# url, state = client.session.authorization_url()
#
# print(f'Authorized = {client.session.authorized}')

token = os.environ.get('RealBkk_token')
# token = os.environ.get('personal_Apps_token')

client = asana.Client.access_token(token)
print(f'Authorized = {client.session.authorized}')

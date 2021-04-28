import os
import requests
import asana
from dotenv import load_dotenv
from typing import List


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


def get_all_projects(client: asana.Client) -> List[dict]:
    workspace_gid = os.environ.get('workspace_gid')
    return client.projects.find_by_workspace(workspace=workspace_gid)


def get_project_by_name(client: asana.Client) -> List[dict]:
    workspace_gid = os.environ.get('workspace_gid')
    return []


if __name__ == '__main__':

    secret = False

    if secret:
        client = secret_auth()
    else:  # auth with token
        token = os.environ.get('personal_Apps_token')
        client = token_auth(token)

    if not client.session.authorized:
        print('Authorize failed')
        quit()

    # for _ in client.workspaces.find_all():
    #     print(_)
    #     workspace_gid = _['gid']
    #     projects = client.projects.find_by_workspace(workspace=workspace_gid)
    #     for p in projects:
    #         print(p)

    projects = get_all_projects(client)
    for each in projects:
        print(each)









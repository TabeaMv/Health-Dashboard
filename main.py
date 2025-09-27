import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os


### Get the first authorization code
# load_dotenv()
# client_id = os.getenv("CLIENT_ID")
# code = "a13d12e15637a08254d042fe6fd9a350e4468434" # already used
# client_secret = os.getenv("CLIENT_SECRET")
# redirect_uri = os.getenv("REDIRECT_URI")
# payload = {'code': code, 
#            'redirect_uri': redirect_uri, 
#            'client_id': client_id, 
#            'grant_type': 'authorization_code'}
# client_info = HTTPBasicAuth(client_id, client_secret)

# r = requests.post('https://api.fitbit.com/oauth2/token', data=payload, auth=client_info)

# print(r.text)


def get_valid_access_token():
    pass


with open("tokens.json") as f:
    d = json.load(f)
    access_token, refresh_token = d["access_token"], d["refresh_token"]



# from dotenv import load_dotenv
# import os
# from typing import Union
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# load_dotenv()
# print("Das Client Secret heißt: "+str(os.getenv("CLIENT_SECRET")))
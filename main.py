import requests
from requests.auth import HTTPBasicAuth
import json

with open("C:/Users/tabea/Desktop/Own Projects/FitbitDashboard/tokens.json") as f:
    d = json.load(f)

client_id = "23TJQ9"
code = "958a3de68656eae849a2921601bdb14634165af8"
client_secret = "400476a08bb45734357899e5fb32ea8b"
redirect_uri = "http://localhost:8080"
payload = {'code': code, 
           'redirect_uri': redirect_uri, 
           'client_id': client_id, 
           'grant_type': 'authorization_code'}
client_info = HTTPBasicAuth(client_id, client_secret)

r = requests.post('https://api.fitbit.com/oauth2/token', data=payload, auth=client_info)

print(r.text)


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
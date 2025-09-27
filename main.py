"""This module manages the fitbit API requests.

It is supposed to get the token pairs for the OAuth2.0 authentification
process and grant access to the user data.
"""
__author__ = "Tabea Maxine Merlevede"
__credits__ = ""
__email__ = "tabea.merlevede@gmail.com"

# standard library imports
import os
import json
from pathlib import Path

# related third party imports
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


class FitBitClient():


    def __init__(self, name="Tabea Merlevede"):
        self.name = name
        self.client_id = None
        self.client_secret = None
        self.access_token = None
        self.refresh_token = None
        self.user_id = None
        self.tokens_filepath = Path("tokens.json")
        self.load_env()
        if self.tokens_filepath.exists():
            self.load_tokens()
        else:
            self.get_initial_tokens()

    
    def load_env(self):
        '''loads information of client_id and client_secret from .env'''
        load_dotenv()
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")


    def get_initial_tokens(self):
        '''
        gets called if there is no existing token pair.
        User needs to provide new authorization code.
        '''
        load_dotenv()
        authorization_code = input("Please provide the authorization code that you received" \
                    "in the browser. More information on how to get the authorization code" \
                    "can be found in the ReadMe file of this project.")
        redirect_uri = os.getenv("REDIRECT_URI")
        payload = {
            "code": authorization_code,
            "redirect_uri": redirect_uri,
            "client_id": self.client_id,
            "grant_type": "authorization_code"
        }
        client_ident = HTTPBasicAuth(self.client_id, self.client_secret)
        api_response = requests.post("https://api.fitbit.com/oauth2/token",
                                     data=payload,
                                     auth=client_ident)
        if api_response.status_code==200:
            with open("tokens.json", "x") as f:
                response = api_response.json()
                json.dump(response, f, indent=4)
                print("Token pair initialized and saved in 'tokens.json'.")
        else:
            print(f"Error with the API request: {api_response.status_code}")
            print(api_response.text)


    def load_tokens(self):
        '''loads current access/refresh tokens and user_id from tokens.json'''
        pass


    def get_valid_access_token(self):
        '''
        Checks if access token is still valid.
        If token is outdated, requests new access/refresh token pair.
        '''
        pass


# with open("tokens.json") as f:
#     d = json.load(f)
#     access_token, refresh_token = d["access_token"], d["refresh_token"]


def main():
    tabea_fitbit = FitBitClient()


if __name__=='__main__':
    main()












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
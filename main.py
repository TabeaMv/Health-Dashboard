"""
This module manages the fitbit API requests.
It handles the OAuth 2.0 authentification process and grants access to user data.
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
    '''Manages Fitbit API authentification and stores client and token information.'''

    def __init__(self, tokens_filepath="tokens.json"):
        self.client_id = None
        self.client_secret = None
        self.access_token = None
        self.refresh_token = None
        self.user_id = None
        self.tokens_filepath = Path(tokens_filepath)
        self.load_env()



    @classmethod
    def from_file(cls):
        """Factory: create client and load tokens from file"""
        obj = cls()
        obj.load_tokens()
        return obj
    

    @classmethod
    def from_auth_code(cls):
        """
        Factory: initialize first access/refresh token pair.
        User interaction necessary!
        """
        obj = cls()
        obj.initialize_tokens()
        obj.load_tokens()
        return obj



    def load_env(self):
        '''loads information of client_id and client_secret from .env'''
        load_dotenv()
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")


    def initialize_tokens(self):
        '''
        gets called if there is no existing token pair.
        User needs to provide new authorization code.
        '''
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
        # send api request for the initial access/refresh token pair
        api_response = requests.post("https://api.fitbit.com/oauth2/token",
                                     data=payload,
                                     auth=client_ident)
        # check api response for successful retrieval of the tokens
        if api_response.status_code==200:
            with open(self.tokens_filepath, "w") as f:
                response = api_response.json()
                json.dump(response, f, indent=4)
                print("Token pair initialized and saved in 'tokens.json'.")
        else:
            raise RuntimeError(
                f"Failed to initialize tokens (HTTP {api_response.status_code}): "
                f"{api_response.text}"
            )


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
    tabea_fitbit = FitBitClient.from_file()


if __name__=='__main__':
    main()
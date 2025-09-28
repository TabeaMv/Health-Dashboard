"""
This module manages the fitbit API requests.
It handles the OAuth 2.0 authentification process and grants access to user data.
"""
__author__ = "Tabea Maxine Merlevede"
__email__ = "tabea.merlevede@gmail.com"

# standard library imports
import os
import json
from pathlib import Path
import logging

# related third party imports
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s",
                    filename="fitbit.log",
                    filemode="a")

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


    def save_tokens(self, token_pair):
        response = token_pair.json()
        with open(self.tokens_filepath, "w") as f:
                json.dump(response, f, indent=4)
                logging.info("Token pair initialized and saved in 'tokens.json'.")
        self.access_token = response["access_token"]
        self.refresh_token = response["refresh_token"]
        self.user_id = response["user_id"]


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
        client_auth = HTTPBasicAuth(self.client_id, self.client_secret)
        # send api request for the initial access/refresh token pair
        api_response = requests.post("https://api.fitbit.com/oauth2/token",
                                     data=payload,
                                     auth=client_auth)
        # check api response for successful retrieval of the tokens
        if api_response.status_code==200:
            self.save_tokens(api_response)
        else:
            raise RuntimeError(
                f"Failed to initialize tokens (HTTP {api_response.status_code}): "
                f"{api_response.text}"
            )


    def load_tokens(self):
        '''loads current access/refresh tokens and user_id from tokens.json'''
        try:
            with open(self.tokens_filepath, "r") as f:
                d = json.load(f)
                self.access_token, self.refresh_token = d["access_token"], d["refresh_token"]
                self.user_id = d["user_id"]
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Token file '{self.tokens_filepath}' not found."
            )
        except KeyError as e:
            raise KeyError(
                f"Missing key in token file: {e}. Check file content."
            )


    def get_valid_access_token(self):
        '''
        Checks if access token is still valid.
        If token is outdated, requests new access/refresh token pair.
        '''
        payload = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "client_id": self.client_id
        }
        client_auth = HTTPBasicAuth(self.client_id, self.client_secret)
        api_response = requests.post("https://api.fitbit.com/oauth2/token",
                                     data=payload,
                                     auth=client_auth)
        if api_response.ok:
            self.save_tokens(api_response)
        else:
            raise RuntimeError(
                f"Failed to refresh token pair (HTTP \
                    {api_response.status_code}): {api_response.text}"
            )


    def data_access(self):
        '''
        Makes API request.
        If access token is valid: access user information.
        If access token is invalid: get new token pair, then access user information.
        '''
        for _ in range(2): # 1. try + max. one token refresh
            request_header = {"Authorization": f"Bearer {self.access_token}", "accept-language": "de_DE"}
            api_response = requests.get("https://api.fitbit.com/1/user/-/profile.json",
                                    headers=request_header)
            if api_response.ok:
                logging.info("API access successful.")
                logging.info(api_response.json())
                return api_response.json()
            elif api_response.status_code == 401:
                logging.info("Token pair invalid. Refreshing...")
                self.get_valid_access_token()
            else:
                break
        raise RuntimeError(
                f"API call failed even after refreshing token pair \
                    (HTTP {api_response.status_code}): {api_response.text}"
            )
    

def main():
    tabea_fitbit = FitBitClient.from_file()
    # tabea_fitbit = FitBitClient.from_auth_code()
    tabea_fitbit.data_access()


if __name__=='__main__':
    main()
This Readme is supposed to be a mix of a logbook and a cookbook.

# 1. Get a valid access/refresh token pair
- First, you send a request for an authorization code to the Fitbit API via the browser. Use the following URL and replace the Client ID with your own:
https://www.fitbit.com/oauth2/authorize?client_id=ABC123&response_type=code&scope=activity%20heartrate%20location%20nutrition%20oxygen_saturation%20profile%20respiratory_rate%20settings%20sleep%20social%20temperature%20weight
- You should see a window opening where you can login and allow the access to the requested data.
- After that, it will show that the page could not be loaded, but that is okay. Just copy the code from the URL (should look like this: http://localhost:8080/?code=a13d12e15637a08254d042fe6fd9a350e4468434#_=_). The code in this case would be a13d12e15637a08254d042fe6fd9a350e4468434
- Now you can use the function "get_first_token_pair" to get your first pair of access and refresh tokens. It will automatically get saved in "tokens.json". For that you need the code from above, your redirect_uri (here: http://localhost:8080) and your client_id (redirect_uri and client_id should already be saved in ".env". Normally, the function will be able to run if you just enter the authorization code. The rest should be loaded by the "dotenv" package.

# 2. get_valid_access_token function



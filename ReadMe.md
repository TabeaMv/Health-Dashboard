This Readme is supposed to be a mix of a logbook and a cookbook.

# 1. Get a valid access/refresh token pair
- First, you send a request for an authorization code to the Fitbit API via the browser. Use the following URL and replace the Client ID with your own. You may also modify the scope:
https://www.fitbit.com/oauth2/authorize?client_id=ABC123&response_type=code&scope=activity%20heartrate%20location%20nutrition%20oxygen_saturation%20profile%20respiratory_rate%20settings%20sleep%20social%20temperature%20weight
- You should see a window opening where you can login and allow the access to the requested data.
- After that, it will show that the page could not be loaded because the redirect URI does not exist atm, but that is okay. Just copy the code from the URL (should look like this: http://localhost:8080/?code=a13d12e15637a08254d042fe6fd9a350e4468434#_=_). The code in this case would be a13d12e15637a08254d042fe6fd9a350e4468434
- Depending on if you need a new token pair or have an existing token pair, you can modify the setup function that gets called in the script when creating the object. The rest of information should be automatically loaded.
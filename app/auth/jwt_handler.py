#This file is responsible for signing,encoding,decoding and returning JWTs.
import time # Time module is responsible for setting an expiration limit for the tokens.because every jwt or token has an expiry date or expiry time,whwre it becomes invalid at some point.
from jose import jwt
import jwt
#Jwtmodule responsile for encoding and decoding generated token strings.
from dotenv import load_dotenv
import os

JWT_SECRET=os.getenv("secret")
JSWT_ALGORITHM=os.getenv("Algorithm")


#this function returns generated tokens

def token_response(token:str):
    return{ "access token": token}

def signJWT(userId: str):
    payload={
        "userId":userId,
        "Expire_time":time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JSWT_ALGORITHM)

    return token_response(token)

def decode(token:str):
    try:
        decode_token=jwt.decode(token, JWT_SECRET, algorithm = JSWT_ALGORITHM)
        return decode_token if decode_token['expires']>=time.time() else None
    except:
        return {}
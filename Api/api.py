from fastapi import FastAPI, Depends, Request
from pydantic import BaseModel
import string
import secrets
import base64
from .cipher import encoder, decryptor
from fastapi.security import HTTPBasic, HTTPBasicCredentials

class Message(BaseModel):
    Content: str

app = FastAPI()

security = HTTPBasic()



@app.post("/encode/")
async def encode_message(request: Request,message: Message, credentials: HTTPBasicCredentials = Depends(security)):
    print(request.headers)
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "1234")
    if not (correct_username and correct_password):
        message.Content = 'Not Authorized'
    else:
        try:
            letter_list = [string.printable.index(x) for x in message.Content]
            encoded_message = encoder(letter_list)
            encoded_message_bytes = (b''.join([bytes([x]) for x in encoded_message]))
            encoded = base64.b64encode(encoded_message_bytes)
            message.Content = encoded
        except Exception:
            message.Content = 'Invalid Input'

    return message


@app.post("/decode/")
async def decode_message(message: Message, credentials: HTTPBasicCredentials = Depends(security)):

    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "1234")
    if not (correct_username and correct_password):
        message.Content = 'Not Authorized'
    else:
        try:
            decoded_base64 = base64.b64decode(message.Content)
            decoded_list = decryptor([x for x in decoded_base64])
            message.Content = ''.join([string.printable[index] for index in decoded_list])
        except Exception:
            message.Content = 'Invalid Input'

    return message
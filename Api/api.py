from fastapi import FastAPI, Depends
from pydantic import BaseModel
import string
import base64
import json
from cipher import encoder, decryptor
from fastapi.security import HTTPBasic, HTTPBasicCredentials

class Message(BaseModel):
    Content: str

app = FastAPI()

security = HTTPBasic()


@app.get("/users/me")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {"username": 'user', "password": '1234'}



@app.post("/encode/")
async def encode_message(message: Message):
    letter_list = [string.printable.index(x) for x in message.Content]
    encoded_message = encoder(letter_list)
    encoded_message_bytes = (b''.join([bytes([x]) for x in encoded_message]))
    encoded = base64.b64encode(encoded_message_bytes)
    message.Content = encoded

    return message


@app.post("/decode/")
async def decode_message(message: Message):
    decoded_base64 = base64.b64decode(message.Content)
    decoded_list = decryptor([x for x in decoded_base64])
    message.Content = ''.join([string.printable[index] for index in decoded_list])

    return message
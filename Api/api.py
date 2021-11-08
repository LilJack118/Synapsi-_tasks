from fastapi import FastAPI
from pydantic import BaseModel
import string
import base64
import json
from cipher import encoder, decryptor


class Item(BaseModel):
    Message: str

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/encode/")
async def create(item: Item):
    letter_list = [string.printable.index(x) for x in item.Message]
    encoded_message = encoder(letter_list)
    encoded_message_bytes = (b''.join([(x).to_bytes(2, byteorder='big') for x in encoded_message]))
    encoded = base64.b64encode(encoded_message_bytes)
    item.Message = encoded

    return item


@app.post("/decode/")
async def create(item: Item):
    decoded_base64 = base64.b64decode(item.Message)
    decoded_list = decryptor(decoded_base64)
    decoded_message = ''
    for letter_index in decoded_list:
        decoded_message +=string.printable[letter_index]
    print(decoded_list)

    return item
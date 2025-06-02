#!/usr/bin/env python3
from flask import Flask, request, jsonify
import gostcrypto
import os

app = Flask(__name__)

with open("flag.txt", "rb") as f:
    flag = f.read()

key, iv = os.urandom(32), os.urandom(8)
cipher = gostcrypto.gostcipher.new(
    "kuznechik", key, gostcrypto.gostcipher.MODE_CTR, init_vect=iv
)

@app.route('/', methods=['GET'])
def get_flag():
    with open("/flag.txt", "rb") as f:
        flag = f.read()

    key, iv = os.urandom(32), os.urandom(8)
    cipher = gostcrypto.gostcipher.new(
        "kuznechik", key, gostcrypto.gostcipher.MODE_CTR, init_vect=iv
    )

    print(f"It's almost Halloween, time to get sp00{cipher.encrypt(flag).hex()}00ky 👻!")

    while True:
        print(cipher.encrypt(bytes.fromhex(input())).hex())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('LISTEN_PORT', 8000)))

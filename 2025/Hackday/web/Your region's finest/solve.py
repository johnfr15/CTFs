import base64
import string
import requests
import hmac
import hashlib
import base64
import random

URL = "http://challenges.hackday.fr:58990"

HEADER = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
PAYLOAD = "eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNzkxMDA1MiwianRpIjoiNzZhOWY0ZjgtZjg4My00NGE4LTgzZWUtMmI2N2QxZTRmZGJkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImRzc2Rmc2ZzZGZzZGYiLCJuYmYiOjE3Mzc5MTAwNTIsImV4cCI6MTczNzkxMDk1MiwiZmF2b3JpdGVfcHJvZHVjdCI6bnVsbH0"
UP = 1737615823


def create_hmacsha256_signature(secret_key: str):
    """Create HMACSHA256 signature using secret key, header and payload."""
    # Concatenate base64Url encoded header and payload
    message = HEADER + "." + PAYLOAD
    # Create HMAC with SHA256
    signature = hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()

    return  base64.urlsafe_b64encode(bytes.fromhex(signature)).decode().rstrip("=")



def find_pid():
    good_sig = "Be1Eqln8Q04javKhCXWA-va79WqWKE57J9toD92GYr8"

    for pid in range(0, 100):
        random.seed(UP + pid)

        dummy = "".join(random.choice(string.printable) for _ in range(32))
        secret = "".join(random.choice(string.printable) for _ in range(32))

        sig = create_hmacsha256_signature( secret )
    
        if sig == good_sig:
            print("Found pid: ", pid)
            break
        if pid % 1000000 == 0:
            print("pid: ", pid)



def cratf_jwt(PID: int):
    random.seed(UP + PID)
    dummy = "".join(random.choice(string.printable) for _ in range(32))
    secret = "".join(random.choice(string.printable) for _ in range(32))
    
    signature = create_hmacsha256_signature( secret )

    return HEADER + "." + PAYLOAD + "." + signature


if __name__ == "__main__":
    find_pid()

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import json
import base64

class Node:
    def __init__(self):
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.public_key = self.private_key.public_key()
        self.address = self.get_public_key_string()
        self.money = 500

    def get_public_key_string(self):
        """ Returns the public key as a unique string identifier (address). """
        return base64.b64encode(self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )).decode()
    def sign_transaction(self, transaction):
        """ Signs a transaction with the private key. """
        transaction_data = json.dumps({
            "sender": transaction.sender,
            "recipient": transaction.recipient,
            "amount": transaction.amount
        }, sort_keys=True).encode()
        
        return base64.b64encode(self.private_key.sign(
            transaction_data,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256(),
        )).decode()

    def verify_signature(self,transaction, signature):
        """ Verifies a transaction signature using the sender's public key. """
        transaction_data = json.dumps({
            "sender": transaction.sender,
            "recipient": transaction.recipient,
            "amount": transaction.amount
        }, sort_keys=True).encode()

        try:
            self.public_key.verify(
                base64.b64decode(signature),
                transaction_data,
                padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256(),
            )
            return True
        except Exception as e:
            return False

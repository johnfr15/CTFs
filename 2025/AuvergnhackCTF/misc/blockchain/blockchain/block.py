import hashlib
import time
from collections import OrderedDict

class Block:
    def __init__(self, index, transactions, previous_hash, timestamp=None,nonce=0):
        self.index = index
        self.timestamp = timestamp if timestamp else time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(data.encode()).hexdigest()

    def to_od(self):
        od = OrderedDict([
            ('index', self.index),
            ('timestamp', self.timestamp),
            ('transactions', ([self.transaction_to_od(trans) for trans in self.transactions])),
            ('previous_hash', self.previous_hash),
            ('nonce', self.nonce),
        ])

        return od


    def transaction_to_od(self, transaction):
        try:
            to_od= OrderedDict([
            ('sender', transaction["sender"]),
            ('recipient', transaction["recipient"]),
            ('amount', transaction["amount"]),
            ("signature",transaction["signature"])
            ])
        except:
            to_od = trans.to_od()
        return to_od

    def __repr__(self):
        return f"Block(index={self.index}, timestamp={self.timestamp}, transactions={self.transactions}, previous_hash={self.previous_hash}, nonce={self.nonce}, hash={self.hash} )"


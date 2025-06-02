from web3 import Web3
from solcx import compile_files, install_solc

# Make sure the correct version of solc is installed
install_solc('0.8.25')

class SetupContract:
    ABI: dict
    BYTECODE: str
    SOURCE_CODE: str

    private_key: str
    ownerAddress: str
    web3: Web3
    Setup = None
    contractAddress: str

    ###################################################
    #                                                 #
    #                     INIT                        #
    #                                                 #
    ###################################################
    def __init__(self, ownerAddress: str, private_key: str, rpc: str, contract_address: str = None):
        self.ownerAddress = ownerAddress
        self.private_key = private_key
        self.web3 = Web3(Web3.HTTPProvider(rpc))
        
        # Compile the Setup contract and its dependencies
        compiled_sol = compile_files(
            ['./src/Setup.sol', './src/Coin.sol', './src/ArcadeMachine.sol'],
            output_values=['abi', 'bin'],
            solc_version='0.8.25'
        )
        
        contract_interface = compiled_sol['src/Setup.sol:Setup']
        self.ABI = contract_interface['abi']
        self.BYTECODE = contract_interface['bin']

        # If a contract address is provided, attach to it
        if contract_address:
            self.attach(contract_address)

    ###################################################
    #                                                 #
    #                    PUBLIC                       #
    #                                                 #
    ###################################################
    def deploy(self):
        nonce = self.web3.eth.get_transaction_count(self.ownerAddress)
        transaction = {
            'from': self.ownerAddress,
            'value': self.web3.to_wei(20, 'ether'),
            'gas': 8000000,
            'gasPrice': self.web3.to_wei('20', 'gwei'),
            'nonce': nonce
        }

        contract = self.web3.eth.contract(abi=self.ABI, bytecode=self.BYTECODE)
        transaction['data'] = contract.constructor().build_transaction(transaction)['data']

        signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f'Transaction sent: {tx_hash.hex()}')
        
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Contract deployed at address: {tx_receipt.contractAddress}')

        self.Setup = self.web3.eth.contract(address=tx_receipt.contractAddress, abi=self.ABI)
        self.contractAddress = tx_receipt.contractAddress

    def attach(self, contract_address: str):
        self.Setup = self.web3.eth.contract(address=contract_address, abi=self.ABI)
        self.contractAddress = contract_address
        print(f'Attached to contract at address: {contract_address}')

    def register(self):
        try:
            if not self._is_deployed():
                raise Exception("Setup contract not deployed yet")
            
            transaction = self.Setup.functions.register().build_transaction({
                'from': self.ownerAddress,
                'gas': 8000000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Transaction sent: {tx_hash.hex()}')
        except Exception as e:
            print(f'Error registering player: {e}')

    def is_solved(self) -> bool:
        try:
            if not self._is_deployed():
                raise Exception("Setup contract not deployed yet")

            solved = self.Setup.functions.isSolved().call()
            return solved
        except Exception as e:
            print(f'Error checking if solved: {e}')
            return False

    def get_coin_address(self) -> str:
        try:
            if not self._is_deployed():
                raise Exception("Setup contract not deployed yet")

            coin_address = self.Setup.functions.coin().call()
            return coin_address
        except Exception as e:
            print(f'Error reading coin address: {e}')
            return None

    def get_arcade_machine_address(self) -> str:
        try:
            if not self._is_deployed():
                raise Exception("Setup contract not deployed yet")

            arcade_machine_address = self.Setup.functions.arcadeMachine().call()
            return arcade_machine_address
        except Exception as e:
            print(f'Error reading arcade machine address: {e}')
            return None

    def get_player_address(self) -> str:
        try:
            if not self._is_deployed():
                raise Exception("Setup contract not deployed yet")

            player_address = self.Setup.functions.player().call()
            return player_address
        except Exception as e:
            print(f'Error reading player address: {e}')
            return None

    ###################################################
    #                                                 #
    #                   INTERNAL                      #
    #                                                 #
    ###################################################
    def _is_deployed(self) -> bool:
        return self.Setup is not None

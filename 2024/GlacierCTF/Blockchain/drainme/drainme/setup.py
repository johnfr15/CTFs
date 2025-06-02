from web3 import Web3
from solcx import compile_source


class SetupContract:
    ABI: dict
    BYTECODE: str
    SOURCE_CODE: str

    private_key: str
    ownerAddress: str
    web3: dict
    Setup = None
    contractAddress: str
    TARGET_address: str
    SB_address: str

    ###################################################
    #                     INIT                        #
    ###################################################
    def __init__(self, ownerAddress: str, private_key: str, rpc: str):
        self.ownerAddress = ownerAddress
        self.private_key = private_key
        self.web3 = Web3(Web3.HTTPProvider(rpc))
        
        # Read and compile the Setup contract
        with open('./Setup.sol', 'r') as file:
            self.SOURCE_CODE = file.read()

        # Compile the contract to get ABI and Bytecode
        compiled_sol = compile_source(self.SOURCE_CODE, solc_version="0.8.18")
        contract_interface = compiled_sol['<stdin>:Setup']
        self.ABI = contract_interface['abi']
        self.BYTECODE = contract_interface['bin']

    ###################################################
    #                    PUBLIC                       #
    ###################################################
    def deploy(self, initial_funds: int):
        """Deploy the Setup contract with initial funds."""
        try:
            nonce = self.web3.eth.get_transaction_count(self.ownerAddress)
            transaction = {
                'from': self.ownerAddress,
                'gas': 8000000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'value': initial_funds,
                'nonce': nonce
            }

            contract = self.web3.eth.contract(abi=self.ABI, bytecode=self.BYTECODE)
            transaction['data'] = contract.constructor().build_transaction(transaction)['data']

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Deployment transaction sent, waiting for receipt...')
            tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)

            self.Setup = self.web3.eth.contract(address=tx_receipt.contractAddress, abi=self.ABI)
            self.contractAddress = tx_receipt.contractAddress
            print(f'Setup contract deployed at: {self.contractAddress}')

            # Fetch the TARGET and SB addresses
            self.TARGET_address = self.Setup.functions.TARGET().call()
            self.SB_address = self.Setup.functions.SB().call()
            print(f'TARGET (ChallengeContract) deployed at: {self.TARGET_address}')
            print(f'SharesBuyer deployed at: {self.SB_address}')

        except Exception as e:
            print(f'Error during deployment: {e}')

    def attach(self, contract_address: str):
        """Attach to an existing Setup contract."""
        try:
            self.contractAddress = contract_address
            self.Setup = self.web3.eth.contract(address=self.contractAddress, abi=self.ABI)

            # Fetch the TARGET and SB addresses
            self.TARGET_address = self.Setup.functions.TARGET().call()
            self.SB_address = self.Setup.functions.SB().call()
            print(f'Setup contract attached at: {self.contractAddress}')
            print(f'TARGET (ChallengeContract) deployed at: {self.TARGET_address}')
            print(f'SharesBuyer deployed at: {self.SB_address}')
        except Exception as e:
            print(f'Error attaching to contract: {e}')

    def is_solved(self) -> bool:
        """Check if the challenge is solved."""
        try:
            if not self._is_attached():
                raise Exception("Setup contract not attached yet.")
            return self.Setup.functions.isSolved().call()
        except Exception as e:
            print(f'Error checking challenge solution: {e}')
            return False

    ###################################################
    #                   INTERNAL                      #
    ###################################################
    def _is_attached(self) -> bool:
        """Check if the Setup contract is attached."""
        return self.Setup is not None

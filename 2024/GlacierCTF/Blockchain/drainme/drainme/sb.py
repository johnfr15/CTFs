from web3 import Web3
from solcx import compile_source


class SharesBuyer:
    ABI: dict
    BYTECODE: str
    SOURCE_CODE: str

    private_key: str
    ownerAddress: str
    web3: dict
    SharesBuyer = None
    contractAddress: str

    ###################################################
    #                     INIT                        #
    ###################################################
    def __init__(self, ownerAddress: str, private_key: str, rpc: str):
        self.ownerAddress = ownerAddress
        self.private_key = private_key
        self.web3 = Web3(Web3.HTTPProvider(rpc))
        
        # Read and compile the SharesBuyer contract
        with open('./SB.sol', 'r') as file:
            self.SOURCE_CODE = file.read()

        # Compile the contract to get ABI and Bytecode
        compiled_sol = compile_source(self.SOURCE_CODE, solc_version="0.8.18")
        contract_interface = compiled_sol['<stdin>:SharesBuyer']
        self.ABI = contract_interface['abi']
        self.BYTECODE = contract_interface['bin']

    ###################################################
    #                    PUBLIC                       #
    ###################################################
    def deploy(self, target_address: str):
        """Deploy the SharesBuyer contract with the target contract address."""
        try:
            nonce = self.web3.eth.get_transaction_count(self.ownerAddress)
            transaction = {
                'from': self.ownerAddress,
                'gas': 8000000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': nonce
            }

            contract = self.web3.eth.contract(abi=self.ABI, bytecode=self.BYTECODE)
            transaction['data'] = contract.constructor(target_address).build_transaction(transaction)['data']

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Deployment transaction sent, waiting for receipt...')
            tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)

            self.SharesBuyer = self.web3.eth.contract(address=tx_receipt.contractAddress, abi=self.ABI)
            self.contractAddress = tx_receipt.contractAddress
            print(f'SharesBuyer contract deployed at: {self.contractAddress}')

        except Exception as e:
            print(f'Error during deployment: {e}')

    def attach(self, contract_address: str):
        """Attach to an existing SharesBuyer contract."""
        try:
            self.contractAddress = contract_address
            self.SharesBuyer = self.web3.eth.contract(address=self.contractAddress, abi=self.ABI)
            print(f'SharesBuyer contract attached at: {self.contractAddress}')
        except Exception as e:
            print(f'Error attaching to contract: {e}')

    def buy_shares(self):
        """Call the buyShares() function on the SharesBuyer contract."""
        try:
            if not self._is_attached():
                raise Exception("SharesBuyer contract not attached yet.")
            
            transaction = self.SharesBuyer.functions.buyShares().build_transaction({
                'from': self.ownerAddress,
                'gas': 3000000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Transaction to buy shares executed successfully.')
        except Exception as e:
            print(f'Error calling buyShares(): {e}')

    ###################################################
    #                   INTERNAL                      #
    ###################################################
    def _is_attached(self) -> bool:
        """Check if the SharesBuyer contract is attached."""
        return self.SharesBuyer is not None

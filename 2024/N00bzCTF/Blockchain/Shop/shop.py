from web3 import Web3
from solcx import compile_source

class ShopContract:
    ABI: dict
    BYTECODE: str
    SOURCE_CODE: str

    private_key: str
    owner_address: str
    web3: dict
    Shop = None
    contractAddress: str





    ###################################################
    #                                                 #
    #                     INIT                        #
    #                                                 #
    ###################################################
    def __init__(self, owner_address: str, private_key: str, rpc: str):
        self.owner_address = owner_address
        self.private_key = private_key
        self.web3 = Web3(Web3.HTTPProvider(rpc))
        
        # Read and compile the Shop contract
        with open('./contract/Shop.sol', 'r') as file:
            self.SOURCE_CODE = file.read()

        # Compile the contract to get ABI
        compiled_sol = compile_source(self.SOURCE_CODE, solc_version="0.6.0")
        contract_interface = compiled_sol['<stdin>:Shop']
        
        # Get ABI and Bytecode
        self.ABI = contract_interface['abi']
        self.BYTECODE = contract_interface['bin']






    ###################################################
    #                                                 #
    #                    PUBLIC                       #
    #                                                 #
    ###################################################
    """
        Build and deploy the Shop contract
    """
    def attach(self, shopAddress: str):        
        self.Shop = self.web3.eth.contract(address=shopAddress, abi=self.ABI)
        self.contractAddress = shopAddress



    """
        Buy an item through the Shop contract
    """
    def buy(self, item: int, quantity: int, value: int):
        try:
            if not self._is_deployed():
                raise Exception("Shop not deployed yet")
            
            transaction = self.Shop.functions.buy(item, quantity).build_transaction({
                'from': self.owner_address,
                'value': value,
                'nonce': self.web3.eth.get_transaction_count(self.owner_address)
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)

            print('Buy transaction sent successfully!')
        except Exception as e:
            print(f'Error sending buy transaction: {e}')



    """
        Check if the challenge is solved
    """
    def is_solved(self):
        try:
            if not self._is_deployed():
                raise Exception("Shop not deployed yet")
            
            result = self.Shop.functions.isChallSolved().call()
            print(f'Challenge solved: {result}')
            return result
        except Exception as e:
            print(f'Error checking challenge status: {e}')
            return False





    ###################################################
    #                                                 #
    #                   INTERNAL                      #
    #                                                 #
    ###################################################

    def _is_deployed(self) -> bool:
        return self.Shop is not None

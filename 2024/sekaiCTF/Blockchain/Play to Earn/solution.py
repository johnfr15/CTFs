# uuid:           18a70472-16fc-4380-b5a9-4739d67f32d5
# rpc endpoint:   https://play-to-earn.chals.sekai.team/18a70472-16fc-4380-b5a9-4739d67f32d5
# private key:    0x3463c1712429bbf22a65ed135d756477636c248d464cd6a689e9bc88cf03aec5
# your address:   0x875Db7cc7eBf9c5311b06198fE919973cBE88D67
# setup contract: 0x44849b3fC0850b8EB1595217701241D9D8304d4a

from web3 import Web3
from solcx import install_solc, compile_files
from setup import SetupContract
from malicious import MaliciousContract
from coin import CoinContract

# Install a specific version of solc
install_solc('0.8.25')




# Contract details
RPC = "https://play-to-earn.chals.sekai.team/8e60ffec-318a-496e-b5c8-bd362889544d"
PRIVATE_KEY = "0x9f9b7d1e1bd42bf6501392e52545f502f50cc5500094dc4c2d941eda297e4c82"
WALLET_ADDRESS = "0x41369D30c058A545a967983F2E3542434749032F"
SETUP_ADDRESS = "0xb4411AecDf6ab56e002BF7bFD26796c40903828d"






def get_balance(walletAddress: str):
    web3 = Web3(Web3.HTTPProvider(RPC))
    # Get the balance
    balance_wei = web3.eth.get_balance(walletAddress)
    # Convert balance to Ether
    balance_eth = web3.from_wei(balance_wei, 'ether')

    return balance_eth

def print_balances(walletAddress, setupAddress, coinAddress, arcadeAddress):
    print(f'My balance                    => {get_balance(walletAddress)} ETH')
    print(f'Setup Contract balance        => {get_balance(setupAddress)} ETH')
    print(f'Coin Contract balance         => {get_balance(coinAddress)} ETH')
    print(f'Arcade Contract balance       => {get_balance(arcadeAddress)} ETH')






if __name__ == '__main__':
    web3 = Web3(Web3.HTTPProvider(RPC))
    s = SetupContract(ownerAddress=WALLET_ADDRESS, private_key=PRIVATE_KEY, rpc=RPC, contract_address=SETUP_ADDRESS)
    COIN_ADDRESS = s.get_coin_address()
    ARCADE_ADDRESS = s.get_arcade_machine_address()
    ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"

    c = CoinContract(ownerAddress=WALLET_ADDRESS, private_key=PRIVATE_KEY, rpc=RPC, contract_address=COIN_ADDRESS)
    m = MaliciousContract(WALLET_ADDRESS, PRIVATE_KEY, RPC, COIN_ADDRESS, ARCADE_ADDRESS, SETUP_ADDRESS)
    # m.attach("0xbE1FD87AB00362a84a27D0072E2715943ab3f131")


    print("ZERO: ", get_balance(ZERO_ADDRESS))
    print_balances(WALLET_ADDRESS, SETUP_ADDRESS, COIN_ADDRESS, ARCADE_ADDRESS)
    print()

    m.deploy()
    # m.withdraw(
    # print()


    # print_balances(WALLET_ADDRESS, SETUP_ADDRESS, COIN_ADDRESS, ARCADE_ADDRESS)

    # # Check if the challenge is solved
    # is_solved = s.is_solved()
    # print(f'Challenge solved: {is_solved}')

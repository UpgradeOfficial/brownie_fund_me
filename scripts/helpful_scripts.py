import imp
from brownie import network, accounts, config,  MockV3Aggregator
from web3 import Web3
DECIMAL = 8
STARTING_PRICE = 2 * 10 ** 10 #  Web3.toWei(STARTING_PRICE, "ether")
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache-local']
FORKED_BLOCKCHAIN_ENVIRONMENTS = ['mainnet-fork-dev', 'mainnet-fork']

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        mock_aggregator = MockV3Aggregator.deploy(DECIMAL, STARTING_PRICE, {"from": get_account()})
    print("Mocks Deployed!")
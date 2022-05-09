from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

DECIMAL = 8
STARTING_PRICE = 20000000000

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The Active Network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        mock_aggregator = MockV3Aggregator.deploy(
            DECIMAL, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}
        )
    price_feed_address = MockV3Aggregator[-1].address
    print("Mocks Deployed!")

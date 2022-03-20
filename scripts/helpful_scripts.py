from brownie import accounts, network, config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "hardhat",
    "development",
    "ganache-local",
    "ganache-gui",
    "mainnet-fork",
]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
ETH_AMOUNT_DEPOSIT = 0.05;


def get_account(index=None, id=None):
    # accounts[0]
    # accounts.add(key)
    # accounts.load(id)
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]

    return accounts.add(config["wallets"]["from_key"])

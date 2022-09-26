from brownie import MultiSigWallet
from scripts.helpful_scripts import get_account

account1 = "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"
account2 = "0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2"


def deploy_Multi_Sign_Contract():
    account = get_account()
    multi_sign_wallet = MultiSigWallet.deploy(
        [account1, account2], 2, {"from": account}, publish_source="True"
    )
    print(multi_sign_wallet)


def main():
    deploy_Multi_Sign_Contract()

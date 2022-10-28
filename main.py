import time
from account import Account
from client import FaucetClient, RestClient
from common import FAUCET_URL, NODE_URL

if __name__ == "__main__":
    rest_client = RestClient(NODE_URL)
    faucet_client = FaucetClient(FAUCET_URL, rest_client)  # <:!:section_1

    alice = Account.load_my_account()
    print("\n=== Addresses ===")
    print(f"Alice: {alice.address()}")
    b = alice.address()

    print("\n=== Initial Balances ===")
    print(f"Alice: {rest_client.account_balance(alice.address())}")


    t = 1
    i = 1
    print("\n=== Начинаю минтить ===")
    while True:
        try:
            number = rest_client.get_number()
            txn_hash = rest_client.mint1(alice, number)
            rest_client.wait_for_transaction(txn_hash)
            txn_hash = rest_client.mint(alice, number)
            rest_client.wait_for_transaction(txn_hash)
            print(f"Mint + {i} + #{number}")
            i = i + 1
        except:
            time.sleep(10)
            print(f"Ошибка блокчейна #{t}")
            t = t + 1

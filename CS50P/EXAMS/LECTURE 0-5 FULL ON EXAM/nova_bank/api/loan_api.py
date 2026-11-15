import json
import os
import sys
import requests

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import tools_transfer

url_trans = "https://6ac4b98154a61668c5f62368.mockapi.io/api/saburabu/mini_banking/transactions"
url_account = "https://6ac4b98154a61668c5f62368.mockapi.io/api/saburabu/mini_banking/accounts"
url_loan = "https://6ad13d1aaddc5b5cb142dd1f.mockapi.io/sabur_nova_bank/transactions_loan_nova_bank"


def get_loan_limit():
    user = tools_transfer.load_user()
    if not user:
        sys.exit("USER NOT FOUND! KINDLY RESTART THE APP AND LOGIN")

    user_id = user["id"]
    loan_check_response = None

    # Make API Requests
    response = requests.get(f"{url_account}/{user_id}", timeout=10)
    received_response = requests.get(
        url_trans, timeout=10, params={"recipient_id": user_id}
    )
    sent_response = requests.get(
        url_trans, timeout=10, params={"sender_id": user_id}
    )

    try:
        loan_check_response = requests.get(url_loan, timeout=15, params={"recipient_id": user_id})
        loan_ok = (loan_check_response.status_code == 200)
    except requests.exceptions.RequestException as http_error:
        raise requests.RequestException(f"{http_error}: REQUEST FAILED!")
    except Exception as error:
        print(error)

    loan_ok = True

    # Correct syntax for status validation
    if (
        response.status_code == 200
        and received_response.status_code == 200
        and sent_response.status_code == 200
        and loan_ok
    ):

        account_data = response.json()
        received_txs = received_response.json()  # This returns a list
        sent_txs = sent_response.json()  # This returns a list
        loan_history = loan_ok.json()

        balance = account_data["account_balance"]

        # Safely loop through transaction lists and calculate totals
        total_received = sum(tx.get("amount", 0) for tx in received_txs)
        total_sent = sum(tx.get("amount", 0) for tx in sent_txs)

        print(
            f"Balance: {balance} | Total Received: {total_received} | Total Sent: {total_sent}"
        )
    else:
        print("Failed to fetch records from server\nTRY AGAIN CHECK YOUR CREDENTIALS.")


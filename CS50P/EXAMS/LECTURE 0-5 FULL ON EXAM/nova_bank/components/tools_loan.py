import json
import datetime
import requests
import base64
from io import BytesIO
from pathlib import Path
from zoneinfo import ZoneInfo
from PIL import Image, ImageDraw, ImageFont

# API Endpoints matching your setup
# API Endpoints matching your setup
URL_ACCOUNT = "https://6ac4b98154a61668c5f62368.mockapi.io/api/saburabu/mini_banking/accounts"
URL_TRANS = "https://6ac4b98154a61668c5f62368.mockapi.io/api/saburabu/mini_banking/transactions"
URL_LOAN = "https://6ad13d1aaddc5b5cb142dd1f.mockapi.io/sabur_nova_bank/loan_nova_bank"

class LoanError(Exception):
    pass

def load_user():
    """Helper to load the local session."""
    candidates = (Path.cwd() / "user.json", Path(__file__).resolve().parent / "user.json")
    for path in candidates:
        if path.is_file():
            with path.open("r", encoding="utf-8") as file:
                return json.load(file)
    raise FileNotFoundError("user.json session file not found.")

def generate_loan_receipt_base64(user_id, amount, date_str, repayment_due):
    """Generates an image receipt for a loan and returns its Base64 encoding string."""
    # Create an image canvas (Width: 400px, Height: 500px)
    img = Image.new("RGB", (400, 500), color="#FFFFFF")
    draw = ImageDraw.Draw(img)
    
    # Simple layout decoration lines
    draw.rectangle([10, 10, 390, 490], outline="#4A90E2", width=3)
    
    # Title Text
    draw.text((120, 30), "NOVA MICROFINANCE", fill="#1F2937")
    draw.text((140, 50), "LOAN DISBURSEMENT", fill="#4A90E2")
    draw.line([30, 80, 370, 80], fill="#E5E7EB", width=2)
    
    # Details Body
    draw.text((40, 110), f"Account ID:   {user_id}", fill="#374151")
    draw.text((40, 150), f"Amount:       NGN {amount:,.2f}", fill="#10B981")
    draw.text((40, 190), f"Interest:     5%", fill="#374151")
    draw.text((40, 230), f"Date Issued:  {date_str}", fill="#374151")
    draw.text((40, 270), f"Due Date:     {repayment_due}", fill="#EF4444")
    
    draw.line([30, 330, 370, 330], fill="#E5E7EB", width=2)
    draw.text((70, 360), "Thank you for banking with Nova!", fill="#6B7280")
    
    # Compress and encode image bytes into a data URL pattern string
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{img_str}"

def evaluate_loan_eligibility(user_id):
    """Calculates creditworthiness limit benchmarks."""
    try:
        loan_res = requests.get(URL_LOAN, timeout=10, params={"accountId": str(user_id)})
        if loan_res.status_code == 200:
            active_loans = loan_res.json()
            if any(loan.get("status") == "OUTSTANDING" for loan in active_loans):
                return False, 0, "You have an active outstanding loan that must be paid back first."
        
        tx_res = requests.get(URL_TRANS, timeout=10)
        if tx_res.status_code != 200:
            return False, 0, "Could not verify your transaction history with the server."
            
        all_txs = tx_res.json()
        received_txs = [
            tx for tx in all_txs 
            if str(tx.get("recipient_id")) == str(user_id) or str(tx.get("reciever_id")) == str(user_id)
        ]
        
        total_received = sum(float(tx.get("amount", 0)) for tx in received_txs)
        max_borrow_limit = 10000.0 + (total_received * 0.50)
        return True, max_borrow_limit, "Eligible"
        
    except requests.RequestException as e:
        return False, 0, f"Network check failed: {e}"

def request_loan(amount):
    """Executes the loan offer, generates a digital receipt, updates account balances, and logs to api platforms."""
    try:
        if amount < 1000:
            raise LoanError("Minimum loan request is ₦1,000.")

        user = load_user()
        user_id = user["id"]
        current_balance = user.get("account_balance", 0)

        print("🔍 Evaluating credit files...")
        is_eligible, max_limit, message = evaluate_loan_eligibility(user_id)

        if not is_eligible or amount > max_limit:
            print(f"⚠️ Request Denied: {message if not is_eligible else 'Exceeds limit'}")
            return

        print(f"✅ Approved! Processing ₦{amount:,} loan deposit...")

        new_balance = current_balance + amount
        acc_response = requests.patch(f"{URL_ACCOUNT}/{user_id}", timeout=15, json={"account_balance": new_balance, "balance": new_balance})

        if acc_response.status_code != 200:
            print(f"❌ Failed to credit account.")
            return

        # Handle file profiles locally
        user["account_balance"] = new_balance
        user["balance"] = new_balance
        for path in (Path.cwd() / "user.json", Path(__file__).resolve().parent / "user.json"):
            if path.is_file():
                with path.open("w", encoding="utf-8") as file:
                    json.dump(user, file, indent=4)

        wat_zone = ZoneInfo("Africa/Lagos")
        now_wat = datetime.datetime.now(wat_zone)
        date_issued_str = now_wat.strftime("%d/%m/%Y @ %H:%M:%S WAT")
        due_date_str = (now_wat + datetime.timedelta(days=30)).strftime("%d/%m/%Y")
        
        # 🧾 Call Receipt String Generation Engine
        receipt_b64 = generate_loan_receipt_base64(user_id, amount, now_wat.strftime('%d/%m/%Y'), due_date_str)

        # Post to Loan Database Ledger
        loan_record = {
            "accountId": str(user_id),
            "amount": amount,
            "interest_rate": "5%",
            "repayment_due": due_date_str,
            "status": "OUTSTANDING",
            "date_issued": date_issued_str,
            "receipt_image": receipt_b64
        }
        loan_tx_res = requests.post(URL_LOAN, timeout=15, json=loan_record)
        
        # Post to global activity feeds
        tx_record = {
            "accountId": str(user_id),
            "sender_id": "NOVA_LOAN_DESK",
            "recipient_id": str(user_id),
            "amount": amount,
            "time_stamp": now_wat.isoformat(timespec='milliseconds'),
            "date": date_issued_str,
            "category": {
                "TYPE OF TRANSACTION": "LOAN_DISBURSEMENT",
                "REMARK": "Approved loan with 5% interest",
                "receipt": receipt_b64
            }
        }
        requests.post(URL_TRANS, timeout=15, json=tx_record)

        if loan_tx_res.status_code == 201:
            print(f"🎉 Loan fully disbursed! Receipt embedded successfully.")

    except Exception as error:
        print(f"💥 System Error: {error}")

if __name__ == "__main__":
    request_loan(5000)
"""Helpers for validating Nova Bank transfers and looking up recipients."""
import json
from pathlib import Path
import requests
import base64
import datetime
import io
import random
from zoneinfo import ZoneInfo
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_receipt(sender_name, recipient_name, recipient_account, amount, remark="None"):
    """Generates a professional banking PDF receipt and returns it as a Base64 string."""
    
    # 1. Initialize an in-memory byte buffer structure
    pdf_buffer = io.BytesIO() 
    
    # 2. Build your document structure targeting our memory buffer container instead of a string path
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter, title="Nova Bank Receipt") 
    styles = getSampleStyleSheet() 

    # Custom Clean Core Layout Styles
    title_style = ParagraphStyle(
        'RTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=24,
        textColor=colors.HexColor('#0F172A'), spaceAfter=4, alignment=1
    ) 
    subtitle_style = ParagraphStyle(
        'RSub', parent=styles['Normal'], fontName='Helvetica', fontSize=10,
        textColor=colors.HexColor('#64748B'), spaceAfter=20, alignment=1
    ) 
    amount_style = ParagraphStyle(
        'RAmount', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=22,
        textColor=colors.HexColor('#10B981'), alignment=1, spaceAfter=15
    ) 
    status_style = ParagraphStyle(
        'RStatus', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10,
        textColor=colors.HexColor('#047857'), alignment=1
    ) 
    label_style = ParagraphStyle(
        'RLabel', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=11,
        textColor=colors.HexColor('#475569')
    ) 
    value_style = ParagraphStyle(
        'RValue', parent=styles['Normal'], fontName='Helvetica', fontSize=11,
        textColor=colors.HexColor('#0F172A'), alignment=2
    ) 

    story = [] 

    # Title & Subtitle Visual Frame Headers
    story.append(Spacer(1, 20)) 
    story.append(Paragraph("🏦 NOVA BANK", title_style)) 
    story.append(Paragraph("TRANSACTION RECEIPT", subtitle_style)) 
    story.append(Spacer(1, 10)) 

    # Formatted Transaction Amount
    story.append(Paragraph(f"₦{amount:,.2f}", amount_style)) 

    # Successful Transaction Status Badge Block
    status_table = Table([[Paragraph("SUCCESSFUL", status_style)]], colWidths=[110], rowHeights=[24]) 
    status_table.setStyle(TableStyle([ 
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#D1FAE5')), 
        ('ALIGN', (0,0), (-1,-1), 'CENTER'), 
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'), 
        ('BOTTOMPADDING', (0,0), (-1,-1), 6), 
    ])) 
    story.append(status_table) 
    story.append(Spacer(1, 30)) 

    # Core Transaction Metadata Rows
    ref_number = f"NB-{random.randint(10000000, 99999999)}-TX" 
    
    # Clean WAT Time configuration layout
    wat_zone = ZoneInfo("Africa/Lagos")
    current_time = datetime.datetime.now(wat_zone).strftime("%d/%m/%Y @ %H:%M:%S WAT")
    
    data = [ 
        [Paragraph("Transaction Type", label_style), Paragraph("Local Transfer", value_style)], 
        [Paragraph("Sender Name", label_style), Paragraph(sender_name, value_style)], 
        [Paragraph("Recipient Name", label_style), Paragraph(recipient_name, value_style)], 
        [Paragraph("Recipient Account", label_style), Paragraph(str(recipient_account), value_style)], 
        [Paragraph("Transaction Reference", label_style), Paragraph(ref_number, value_style)], 
        [Paragraph("Date & Time", label_style), Paragraph(current_time, value_style)], 
        [Paragraph("Remark", label_style), Paragraph(str(remark), value_style)], # Added Remark Row
    ] 

    # Note: rowHeights updated to [32]*7 to match the 7 data rows perfectly
    details_table = Table(data, colWidths=[180, 240], rowHeights=[32]*7) 
    details_table.setStyle(TableStyle([ 
        ('LINEBELOW', (0,0), (-1,-2), 0.5, colors.HexColor('#E2E8F0')), 
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'), 
    ])) 
    story.append(details_table) 
    story.append(Spacer(1, 40)) 

    # Standard Bottom Footnote Disclaimer Text
    disclaimer_style = ParagraphStyle('Disc', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=8, textColor=colors.HexColor('#94A3B8'), alignment=1) 
    story.append(Paragraph("This is an automatically generated receipt. No signature required.", disclaimer_style)) 

    # 3. Build structural elements directly inside your active buffer string
    doc.build(story) 
    
    # Move reading pointer cursor line back down to index start zero
    pdf_buffer.seek(0) 
    pdf_bytes = pdf_buffer.getvalue() 

    # 5. Converts the binary bytes into a text string and returns it
    pdf_base64_string = base64.b64encode(pdf_bytes).decode("utf-8")
    return pdf_base64_string


url = "https://6ac4b98154a61668c5f62368.mockapi.io/api/saburabu/mini_banking/accounts"
transactions_url = "https://6ac4b98154a61668c5f62368.mockapi.io/api/saburabu/mini_banking/transactions"

class accountdoesnotexist(Exception):
    """Raised when no account matches the supplied account number."""


class InvalidTransfer(Exception):
    """Raised when a transfer amount is invalid."""


def load_user():
    """Load the active user's JSON profile without relying on the shell's cwd."""

    candidates = (Path.cwd() / "user.json", Path(__file__).resolve().parent / "user.json")
    for path in candidates:
        if path.is_file():
            with path.open("r", encoding="utf-8") as file:
                user = json.load(file)
            if not isinstance(user, dict):
                raise ValueError(f"{path} must contain a JSON object for the active user.")
            return user
    raise FileNotFoundError(
        "user.json was not found. Sign in first so the active user profile can be saved."
    )


def account_number_confirmer(account_number):
    """Return (account_id, account_number) for an exact recipient match.

    Raises accountdoesnotexist when no exact match exists, and propagates clear
    network/API errors rather than silently returning None.
    """
    if account_number is None or not str(account_number).strip():
        raise accountdoesnotexist("Enter a valid account number and try again.")

    requested_number = str(account_number).strip()
    try:
        response = requests.get(
            url,
            timeout=10,
            params={"account_number": requested_number},
        )
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.Timeout as exc:
        raise ConnectionError("The banking server timed out. Please try again.") from exc
    except requests.exceptions.RequestException as exc:
        raise ConnectionError(f"Could not contact the banking server: {exc}") from exc
    except ValueError as exc:
        raise RuntimeError("The banking server returned invalid JSON.") from exc

    if isinstance(data, dict):
        accounts = [data]
    elif isinstance(data, list):
        accounts = data
    else:
        raise RuntimeError("Unexpected response from the banking API.")

    # Do not assume data[0] is the right account: confirm the exact number.
    for account in accounts:
        if not isinstance(account, dict):
            continue
        returned_number = account.get("account_number")
        if returned_number is not None and str(returned_number).strip() == requested_number:
            account_id = account.get("id")
            account_balance = account.get("account_balance")
            account_name = account.get("full_name")
            if account_id is None:
                raise RuntimeError("The matching account record has no account ID.")
            return account_id, returned_number, account_balance, account_name

    raise accountdoesnotexist(
        "Account number does not exist. Check the number and try again."
    )


def invalid_transfer(amount):
    """Validate amount against the active user's balance.

    Returns True for a valid amount. Raises InvalidTransfer for invalid amounts
    instead of silently reaching the end of the function and returning None.
    """
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise InvalidTransfer("Transfer amount must be a number.")

    if amount < 1000:
        raise InvalidTransfer("Minimum transfer amount is ₦1,000.")

    user = load_user()
    balance = user.get("account_balance")
    if isinstance(balance, bool) or not isinstance(balance, (int, float)):
        raise ValueError("The active user's account balance is missing or invalid.")

    if amount > balance:
        raise InvalidTransfer(
            "Transfer amount is greater than your account balance. Try again."
        )

    return True

def transfer(amount, account_number, remark):
    try:
        # Phase 1: Pre-flight Safety Checks
        invalid_transfer(amount)
        
        # Load active session sender profile info details
        user = load_user()
        sender_balance = user.get("account_balance")
        sender_id = user.get("id")
        sender_name = user.get("full_name")
        
        # Pull profile verification components for the target recipient array row
        recipient_id, recipient_acc_num, recipient_balance, recipient_name = account_number_confirmer(account_number)
        
        print(f"🔄 Processing transfer of ₦{amount:,} from {sender_name} to {recipient_name}...")

        # Phase 2: Execute Account Debit Balance Change
        new_sender_balance = sender_balance - amount
        debit_url = f"{url}/{sender_id}"
        response_d = requests.patch(debit_url, timeout=15, json={"account_balance": new_sender_balance})
        
        if response_d.status_code == 200:
            print(f"✅ {sender_name} has been debited successfully.")
        else:
            print(f"❌ Sender debit operation failed. Server responded with: {response_d.status_code}")
            return None

        # Phase 3: Execute Account Credit Balance Change
        new_recipient_balance = recipient_balance + amount
        credit_url = f"{url}/{recipient_id}"
        response_c = requests.patch(credit_url, timeout=15, json={"account_balance": new_recipient_balance})

        if response_c.status_code == 200:
            print(f"🎉 {recipient_name} has successfully received the transfer!")

            transaction = generate_receipt(sender_name=sender_name, recipient_name=recipient_name, recipient_account=account_number, amount=amount, remark=remark)
            
            # Update the balance property inside your active dictionary
            user['account_balance'] = new_sender_balance
            
            candidates = (Path.cwd() / "user.json", Path(__file__).resolve().parent / "user.json")
            for path in candidates:
                if path.is_file():
                    with path.open("w", encoding="utf-8") as file: 
                        json.dump(user, file, indent=4)
                        print(f"✅ LOCAL ACCOUNT BALANCE HAS BEEN UPDATED TO ₦{new_sender_balance:,}")
            return transaction, sender_id, recipient_id, amount
        else:
            print(f"❌ Recipient credit operation failed. Server responded with: {response_c.status_code}")
            return None

    except InvalidTransfer as e:
        print(f"⚠️ Transfer Blocked: {e}")
    except FileNotFoundError as e:
        print(f"📂 Session Error: {e}")
    except ConnectionError as e:
        print(f"🔌 Network Error: {e}")
    except Exception as e:
        print(f"💥 An unexpected error occurred: {e}")


def transaction_reciept(amount, account_number, remark):

    transfer_result = transfer(amount, account_number, remark)
    
    if not transfer_result:
        print("❌ Transaction aborted due to internal transfer errors.")
        return

    transaction, sender_id, recipient_id, transferred_amount = transfer_result

    # Standardized WAT Handling Configuration
    wat_zone = ZoneInfo("Africa/Lagos")
    now_wat = datetime.datetime.now(wat_zone)
    receipt_timestamp = now_wat.strftime("%d/%m/%Y @ %H:%M:%S %Z")
    database_timestamp = now_wat.isoformat(timespec='milliseconds')

    print("Transaction Time: ", receipt_timestamp)


    transaction_query = {
        "accountId": sender_id,  
        "sender_id": sender_id,
        "recipient_id": recipient_id,
        "amount": transferred_amount,
        "time_stamp": database_timestamp,
        "date": receipt_timestamp,
        "receipt_pdf": transaction,
        "category": {
            "TYPE OF TRANSACTION": "TRANSFER",
            "REMARK": remark
        }
    }

    try:
        response = requests.post(transactions_url, timeout=15, json=transaction_query)
        if response.status_code == 201:
            print("🎉 Receipt Uploaded Successfully to DATABASE!")
        else:
            print(f"❌ Database rejected entry layout. Status code: {response.status_code} | Info: {response.text}")
    except requests.exceptions.RequestException as error_log:
        print(f"🔌 A network error occurred while uploading: {error_log}")


transfer(amount=1500, account_number=8408209445, remark="Test Transfer")  # Example call for testing

"""" OMO THIS SHIII SHARP DIE!!!!!!!!!"""
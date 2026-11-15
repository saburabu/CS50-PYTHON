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

# Endpoints
url = "https://6ac4b98154a61668c5f62368.mockapi.io/api/saburabu/mini_banking/accounts"
transactions_url = "https://6ac4b98154a61668c5f62368.mockapi.io/api/saburabu/mini_banking/transactions"

class INVALIDAMOUNTERROR(Exception):
    pass


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


def amount_validate(amount):
    if amount < 1000:
        raise INVALIDAMOUNTERROR("AMOUNT MUST BE GREATER THAN 1000")
    return amount


def generate_deposit_receipt(account_name, account_number, amount):
    """Generates a professional banking PDF receipt for a deposit and returns it as a Base64 string."""
    pdf_buffer = io.BytesIO() 
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter, title="Nova Bank Deposit Receipt") 
    styles = getSampleStyleSheet() 

    # Typography & Branding Layout Styles
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

    story = [
        Spacer(1, 20),
        Paragraph("🏦 NOVA BANK", title_style),
        Paragraph("DEPOSIT RECEIPT", subtitle_style),
        Spacer(1, 10),
        Paragraph(f"₦{amount:,.2f}", amount_style)
    ]

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
    ref_number = f"NB-{random.randint(10000000, 99999999)}-DEP" 
    wat_zone = ZoneInfo("Africa/Lagos")
    current_time = datetime.datetime.now(wat_zone).strftime("%d/%m/%Y @ %H:%M:%S WAT")
    
    data = [ 
        [Paragraph("Transaction Type", label_style), Paragraph("Cash Deposit", value_style)], 
        [Paragraph("Account Name", label_style), Paragraph(account_name, value_style)], 
        [Paragraph("Account Number", label_style), Paragraph(str(account_number), value_style)], 
        [Paragraph("Transaction Reference", label_style), Paragraph(ref_number, value_style)], 
        [Paragraph("Date & Time", label_style), Paragraph(current_time, value_style)], 
    ] 

    details_table = Table(data, colWidths=[180, 240], rowHeights=[32]*5) 
    details_table.setStyle(TableStyle([ 
        ('LINEBELOW', (0,0), (-1,-2), 0.5, colors.HexColor('#E2E8F0')), 
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'), 
    ])) 
    story.append(details_table) 
    story.append(Spacer(1, 40)) 

    disclaimer_style = ParagraphStyle('Disc', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=8, textColor=colors.HexColor('#94A3B8'), alignment=1) 
    story.append(Paragraph("This is an automatically generated receipt. No signature required.", disclaimer_style)) 

    # Build PDF
    doc.build(story) 
    pdf_buffer.seek(0) 
    pdf_bytes = pdf_buffer.getvalue() 


    return base64.b64encode(pdf_bytes).decode("utf-8")


def deposit(amount):
    try:
        deposit_amount = amount_validate(amount)
        user = load_user()
        
        if not isinstance(user, dict):
            print("USER CREDENTIALS ARE INVALID")
            return

        user_id = user['id']
        user_name = user.get("full_name")
        user_acc_num = user.get("account_number")
        user_balance = user.get("account_balance")
        final_amount = user_balance + deposit_amount

        # Send transaction update to MockAPI accounts endpoint
        response = requests.patch(f"{url}/{user_id}", timeout=15, json={"account_balance": final_amount})

        if response.status_code == 200:
            print("FINALIZING DEPOSIT!")

            # Compile professional receipt data payload string
            pdf_string = generate_deposit_receipt(account_name=user_name, account_number=user_acc_num, amount=deposit_amount)

            # Update Local File Session State Balance Configuration
            user["account_balance"] = final_amount
            candidates = (Path.cwd() / "user.json", Path(__file__).resolve().parent / "user.json")
            for path in candidates:
                if path.is_file():
                    with path.open("w", encoding="utf-8") as file:
                        json.dump(user, file, indent=4)

            print("DEPOSIT CONFIRMED AND SUCCESSFUL")

            # Time Generation Layout Constants
            wat_zone = ZoneInfo("Africa/Lagos")
            now_wat = datetime.datetime.now(wat_zone)
            receipt_timestamp = now_wat.strftime("%d/%m/%Y @ %H:%M:%S %Z")
            database_timestamp = now_wat.isoformat(timespec='milliseconds')

            # Create entry targeting relational database transactions schema
            transaction_query = {
                "accountId": user_id,  # Link entry to account owner id
                "sender_id": "CASH_DEPOSIT",
                "recipient_id": user_id,
                "amount": deposit_amount,
                "time_stamp": database_timestamp,
                "date": receipt_timestamp,
                "receipt_pdf": pdf_string,
                "category": {
                    "TYPE OF TRANSACTION": "DEPOSIT",
                    "REMARK": "Account cash top up deposit"
                }
            }

            # Upload transaction receipt entry data directly into MockAPI transactions collection
            try:
                tx_response = requests.post(transactions_url, timeout=15, json=transaction_query)
                if tx_response.status_code == 201:
                    print("🎉 Deposit Receipt Uploaded Successfully to DATABASE!")
                else:
                    print(f"❌ Database rejected entry registry. Code: {tx_response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"🔌 A network error occurred while updating backend transaction database: {e}")

        else:
            print(f"❌ Server rejection error occurred during deposit operation. Status: {response.status_code}")

    except INVALIDAMOUNTERROR as error:
        print(f"⚠️ Validation Blocked: {error}")
    except FileNotFoundError as error:
        print(f"📂 Session Error: {error}")
    except Exception as error:
        print(f"💥 An unexpected error occurred: {error}")
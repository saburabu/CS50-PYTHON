import io
import os
import json
import base64
import random
import datetime
import requests
from zoneinfo import ZoneInfo
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


BASE_URL = "https://6ac4b98154a61668c5f62368.mockapi.io/api/saburabu/mini_banking"
accounts_url = f"{BASE_URL}/accounts"
transactions_url = f"{BASE_URL}/transactions"


class INVALIDAMOUNTERROR(Exception): 
    pass


def amount_validate(amount):
    if amount < 1000:
        raise INVALIDAMOUNTERROR("AMOUNT MUST BE GREATER THAN 1000")
    return amount

def generate_withdrawal_receipt(user_name, account_id, amount, new_balance):
    """Generates a professional banking withdrawal PDF receipt matching Nova Bank design parameters."""
    pdf_buffer = io.BytesIO() 
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter, title="Nova Bank Withdrawal Receipt") 
    styles = getSampleStyleSheet() 

    # Clean Core Typography Hierarchy Rules
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
        textColor=colors.HexColor('#EF4444'), alignment=1, spaceAfter=15  # Red accent for debit/withdrawal
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

    # Structural Flow Framework Elements
    story.append(Spacer(1, 20)) 
    story.append(Paragraph("🏦 NOVA BANK", title_style)) 
    story.append(Paragraph("TRANSACTION RECEIPT", subtitle_style)) 
    story.append(Spacer(1, 10)) 

    # Value Formatting Context
    story.append(Paragraph(f"₦{amount:,.2f}", amount_style)) 

    # Execution State Validation Pill Visual
    status_table = Table([[Paragraph("SUCCESSFUL", status_style)]], colWidths=[110], rowHeights=[24]) 
    status_table.setStyle(TableStyle([ 
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#D1FAE5')), 
        ('ALIGN', (0,0), (-1,-1), 'CENTER'), 
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'), 
        ('BOTTOMPADDING', (0,0), (-1,-1), 6), 
    ])) 
    story.append(status_table) 
    story.append(Spacer(1, 30)) 

    # Unique Reference Sequence Parameters
    ref_number = f"NB-{random.randint(10000000, 99999999)}-WD" 
    
    # Regional Date Parsing Configuration
    wat_zone = ZoneInfo("Africa/Lagos")
    current_time = datetime.datetime.now(wat_zone).strftime("%d/%m/%Y @ %H:%M:%S WAT")
    
    data = [ 
        [Paragraph("Transaction Type", label_style), Paragraph("Cash Withdrawal", value_style)], 
        [Paragraph("Account Holder", label_style), Paragraph(user_name, value_style)], 
        [Paragraph("Account Reference ID", label_style), Paragraph(str(account_id), value_style)], 
        [Paragraph("Transaction Reference", label_style), Paragraph(ref_number, value_style)], 
        [Paragraph("Date & Time", label_style), Paragraph(current_time, value_style)], 
        [Paragraph("Available Balance", label_style), Paragraph(f"₦{new_balance:,.2f}", value_style)], 
    ] 

    details_table = Table(data, colWidths=[180, 240], rowHeights=[32]*6) 
    details_table.setStyle(TableStyle([ 
        ('LINEBELOW', (0,0), (-1,-2), 0.5, colors.HexColor('#E2E8F0')), 
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'), 
    ])) 
    story.append(details_table) 
    story.append(Spacer(1, 40)) 

    disclaimer_style = ParagraphStyle('Disc', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=8, textColor=colors.HexColor('#94A3B8'), alignment=1) 
    story.append(Paragraph("This is an automatically generated receipt. No signature required.", disclaimer_style)) 

    doc.build(story) 
    pdf_buffer.seek(0) 
    return base64.b64encode(pdf_buffer.getvalue()).decode("utf-8")


def withdraw(amount):
    try:
        withdraw_amount = amount_validate(amount)
        # Import your active session component securely
        import tools_transfer 
        user = tools_transfer.load_user()
        
        if not user:
            print("FAILURE OCCURRED WHEN VALIDATING USER!!")
            return

        # Handle structural key differences between your mock apps ('balance' vs 'account_balance')
        balance = user.get('account_balance') or user.get('balance', 0)
        
        if withdraw_amount > balance:
            print("⚠️ Withdrawal Blocked: Insufficient Balance.")
            return

        new_balance = balance - withdraw_amount
        
        response = requests.patch(
            f"{accounts_url}/{user['id']}", 
            timeout=10, 
            json={"account_balance": new_balance, "balance": new_balance}
        )
        
        if response.status_code == 200:
            print(f"✅ {user['full_name']} successfully withdrew ₦{withdraw_amount:,}\nNEW BALANCE: ₦{new_balance:,}")
            
            # Generate receipt binary text block frame string
            pdf_string = generate_withdrawal_receipt(
                user_name=user['full_name'], 
                account_id=user['id'], 
                amount=withdraw_amount, 
                new_balance=new_balance
            )
            
            # Optional: Post back transactions structure if database upload is required
            wat_zone = ZoneInfo("Africa/Lagos")
            now_wat = datetime.datetime.now(wat_zone)
            
            transaction_query = {
                "accountId": user['id'],  
                "amount": withdraw_amount,
                "time_stamp": now_wat.isoformat(timespec='milliseconds'),
                "date": now_wat.strftime("%d/%m/%Y @ %H:%M:%S %Z"),
                "receipt_pdf": pdf_string,
                "category": {
                    "TYPE OF TRANSACTION": "WITHDRAWAL",
                    "REMARK": "ATM/Cash Withdrawal"
                }
            }
            
            requests.post(transactions_url, timeout=15, json=transaction_query)
            print("🎉 Withdrawal Receipt Uploaded Successfully to DATABASE!")
            return pdf_string

    except INVALIDAMOUNTERROR as error:
        print(f"⚠️ Validation Error: {error}")
    except requests.RequestException as error:
        print(f"🔌 Network Error: {error}")
    except Exception as a:
        print(f"💥 Unexpected Error occurred: {a}")

withdraw(2000)
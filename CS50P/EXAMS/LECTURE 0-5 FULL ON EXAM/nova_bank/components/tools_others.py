import requests
import json
import time
import base64
from io import BytesIO
from PIL import Image, ImageDraw

VT_PUBLIC_KEY = "PK_651949af38847ea653ff093ec6af36053ed6d2e006a"
VT_SECRET_KEY = "SK_91997acef358a2c147a21bb9e397bfdd8f8daaabdda"
BASE_URL = "https://vtpass.com"
URL_TRANS = "https://6ac4b98154a61668c5f62368.mockapi.io/api/saburabu/mini_banking/transactions"

def _get_headers():
    return {
        "api-key": "f6007d571f3ea36304a057dd1be67bf4",
        "public-key": VT_PUBLIC_KEY,
        "secret-key": VT_SECRET_KEY,
        "Content-Type": "application/json"
    }

def _generate_request_id():
    current_time = time.strftime("%Y%m%d%H%M%S")
    ms = str(int(time.time() * 1000.0))[-3:]
    return f"{current_time}{ms}"

def generate_utility_receipt_base64(service_name, target, amount, req_id):
    """Generates an image canvas card for utility expenses and outputs Base64 string."""
    img = Image.new("RGB", (400, 450), color="#FFFFFF")
    draw = ImageDraw.Draw(img)
    
    # Outer frame
    draw.rectangle([10, 10, 390, 440], outline="#10B981", width=3)
    
    # Header
    draw.text((130, 30), "VTPASS UTILITY PLAN", fill="#1F2937")
    draw.line([30, 70, 370, 70], fill="#E5E7EB", width=2)
    
    # Details Content
    draw.text((40, 100), f"Service Type: {service_name.upper()}", fill="#374151")
    draw.text((40, 140), f"Recipient:    {target}", fill="#374151")
    draw.text((40, 180), f"Amount Paid:  NGN {amount:,.2f}", fill="#10B981")
    draw.text((40, 220), f"Reference ID: {req_id}", fill="#6B7280")
    
    draw.line([30, 280, 370, 280], fill="#E5E7EB", width=2)
    draw.text((90, 320), "Transaction Successfully Processed", fill="#10B981")
    
    # Convert image format mapping array to String arrays
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{img_str}"

def sync_transaction_to_ledger(account_id, amount, category, remark, receipt_b64):
    """Logs the utility transaction out to the global MockAPI architecture ledger."""
    payload = {
        "accountId": str(account_id),
        "sender_id": str(account_id),
        "recipient_id": "VTPASS_DISPATCH",
        "amount": amount,
        "date": time.strftime("%d/%m/%Y @ %H:%M:%S"),
        "category": {
            "TYPE OF TRANSACTION": category,
            "REMARK": remark,
            "receipt": receipt_b64
        }
    }
    try:
        requests.post(URL_TRANS, json=payload, timeout=10)
    except requests.RequestException as e:
        print(f"Logging mirror skipped: {e}")

# ==========================================
# 1. AIRTIME SUBSCRIPTION
# ==========================================
def purchase_airtime(account_id: str, phone_number: str, amount: int, network: str = "mtn") -> dict:
    endpoint = f"{BASE_URL}/pay"
    request_id = _generate_request_id()
    
    payload = {
        "request_id": request_id,
        "serviceID": network,
        "amount": amount,
        "phone": phone_number
    }
    
    response = requests.post(endpoint, headers=_get_headers(), json=payload).json()
    
    # If VTpass signals operational success (code '000'), compile and log the receipt bundle
    if response.get("code") == "000":
        receipt_b64 = generate_utility_receipt_base64(network, phone_number, amount, request_id)
        sync_transaction_to_ledger(account_id, amount, "AIRTIME_PURCHASE", f"Airtime topup for {phone_number}", receipt_b64)
        
    return response

# ==========================================
# 2. ELECTRICITY BILLS
# ==========================================
def purchase_electricity_token(account_id: str, meter_number: str, amount: int, phone_number: str, disco_provider: str = "ikedc", meter_type: str = "prepaid") -> dict:
    endpoint = f"{BASE_URL}/pay"
    request_id = _generate_request_id()
    
    payload = {
        "request_id": request_id,
        "serviceID": disco_provider,
        "billersCode": meter_number,
        "variation_code": meter_type,
        "amount": amount,
        "phone": phone_number
    }
    
    response = requests.post(endpoint, headers=_get_headers(), json=payload).json()
    
    if response.get("code") == "000":
        receipt_b64 = generate_utility_receipt_base64(disco_provider, meter_number, amount, request_id)
        sync_transaction_to_ledger(account_id, amount, "ELECTRICITY_BILL", f"Power token purchase for meter {meter_number}", receipt_b64)
        
    return response



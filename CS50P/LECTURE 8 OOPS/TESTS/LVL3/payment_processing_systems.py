class CardPayment:
    def __init__(self, card_holder: str, card_number: str):
        self.card_holder = card_holder
        self.card_number = card_number

    def pay(self, amount: float):
        # Mask all digits except the last 4 for security
        masked_card = f"**** **** **** {self.card_number[-4:]}"
        print(f"[Card Payment] Charging ₦{amount:,.2f} to {self.card_holder}'s card ({masked_card})...")
        print("-> Card payment approved!\n")


class BankTransfer:
    def __init__(self, bank_name: str, account_number: str):
        self.bank_name = bank_name
        self.account_number = account_number

    def pay(self, amount: float):
        print(f"[Bank Transfer] Initiating transfer of ₦{amount:,.2f} via {self.bank_name} (Acct: {self.account_number})...")
        print("-> Transfer confirmed and settled!\n")


class WalletPayment:
    def __init__(self, username: str, balance: float):
        self.username = username
        self.balance = balance

    def pay(self, amount: float):
        print(f"[Wallet Payment] Attempting to deduct ₦{amount:,.2f} from @{self.username}'s wallet...")
        if self.balance >= amount:
            self.balance -= amount
            print(f"-> Payment successful! Remaining wallet balance: ₦{self.balance:,.2f}\n")
        else:
            print(f"-> Payment failed! Insufficient funds (Available: ₦{self.balance:,.2f}).\n")


# --- THE POLYMORPHIC FUNCTION ---
def process_payment(payment_method, amount: float):
    """
    Receives ANY payment object and triggers its pay() method.
    It does not care what class the object belongs to, as long as it has .pay().
    """
    payment_method.pay(amount)

// 1. Just the data layout
struct BankAccount {
    account_holder: String,
    account_number: String,
    balance: f64, // 64-bit float for currency
}

// 2. Just the behaviors / methods
impl BankAccount {
    // Constructor (Like your Python __init__)
    fn new(holder: String, number: String, initial_balance: f64) -> Self {
        BankAccount {
            account_holder: holder,
            account_number: number,
            balance: initial_balance,
        }
    }

    // Deposit method
    fn deposit(&mut self, amount: f64) {
        if amount > 0.0 {
            self.balance += amount;
            println!("Amount deposited: ₦{amount}. Final balance: ₦{}", self.balance);
        }
    }
}

fn main() {
    let mut account = BankAccount::new(
        String::from("Abu Sabur Osimua"), 
        String::from("0123456789"), 
        50000.0
    );
    account.deposit(25000.0);
}

#Currency Calculator
amount = float(input("Enter the amount in your currency: "))
exchange_rate = float(input("Enter the exchange rate: "))
currency_name = str(input("Enter the name of your currency: "))
# where the conversion is calculated and returned
def convert_currency(amount, rate):
    converted_amount = amount * rate
    return converted_amount
#where the conversion is calculated and printed
converted_amount = convert_currency(amount, exchange_rate)
print(f"{amount} {currency_name} is equal to {converted_amount}")
#Mobile Data Usage Calculator
user = input("Enter your username: ")
daily_usage = float(input("Enter the amount of data used daily (in GB): "))
days = float(input("Enter the number of days used!: "))
price_per_gb = float(input("Enter the price per GB: "))

def calculate_data_usage(user, daily_usage, days, price_per_gb):
    total_usage = daily_usage * days
    total_cost = total_usage * price_per_gb
    return total_usage, total_cost

total_usage, total_cost = calculate_data_usage(user, daily_usage, days, price_per_gb)
user = user.strip().title()
print("===============================")
print(f"User: {user}")
print(f"Daily Usage: {daily_usage} GB")
print(f"Days Used: {days}")
print(f"Total Data Usage: {total_usage:.2f} GB")
print(f"Total Cost: ${total_cost:.2f}")
print("===============================")

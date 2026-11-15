# FUNCTION DESIGN
CN = input("Enter customer name: ")
MN = input("Enter movie name: ")
TP = float(input("Enter ticket price: "))
NOT = int(input("Enter number of tickets: "))

def calculate_total(TP, NOT):
    total = TP * NOT
    return total

CN = CN.strip().title()
print("===================================")
print("          MOVIE TICKET RECEIPT      ")
print("===================================")
print(f"Customer Name: {CN}")
print(f"Movie Name: {MN}")
print(f"Ticket Price: ${TP:.2f}")
print(f"Number of Tickets: {NOT}")


def create_message(CN, MN, total):
    return f"hello, {CN} the ticket for {MN} costs ${total:.2f}"


total_cost = calculate_total(TP, NOT)
message = create_message(CN, MN, total_cost)
print(message)










def change(price, amount):
    price = price - amount
    return price

price = 100
new_price = change(price, 25)

print(price)
print(new_price)

#Why aren't both printed values the same?
# when we defined the function change which does price = price - amount and returns the value of price
# and in line 5 price was assigned a value of 100 and in line 6 there is a new variable new_price = change(price, 25)
# in line 6 as you can see amount was given a value which the value of amount will be price = 100 - 25 = 75
# so when we print out price and new_price we get different values
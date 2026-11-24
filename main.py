print("Event Price Tracking")
print("----------------------")
ticketprice = float(input("What is the price of ticket? "))
membership = str(input("Are you member? (Yes/No) "))
tickets = int(input ("How many tickets do you have? "))
price = ticketprice * tickets
if membership == "Yes" :
    price = price - (0.1*price)
else:
    price = price

if price > 1000 and membership == "No":
    price = price - (0.2*price)

print("price of ticket is ", price)
print("-----------------------------------------")
print("-------Ticketing Pricing Software------")
print("-----------------------------------------")

print("Please enter your age :")
Age = int(input())

if (Age<=5):
    print("Your Ticket is free")
elif (Age>5 and Age<=18):
    print("Your Ticket Price is 900 Rupees")
elif (Age>18 and Age<=40):
    print("Your Ticket Price is 1200 Rupees")
else:
    print("Your Ticket Price is 500 Rupees")

print("-----------------------------------------")
print("-------Thank You------")
print("-----------------------------------------")

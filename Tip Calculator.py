a=float(input("Please enter total bill amount: "))
b=int(input("Enter number of people to split the bill between: "))
t=float(input("Enter the tip amount: "))
tip=1+(t/100)
s=(a/b)*tip
total=round(s,2)
print(f"Each person should pay ${total}.")

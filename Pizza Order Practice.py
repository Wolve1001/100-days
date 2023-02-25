print("Welcome to Python Pizza Deliveries!")
s = input("What size pizza do you want? S, M, or L ")
p = input("Do you want pepperoni? Y or N ")
c = input("Do you want extra cheese? Y or N ")
t=0
if s == 'S':
    t=t+15
    if p == 'Y':
        t=t+2
elif s == 'M':
    t=t+20
    if p == 'Y':
        t=t+3
elif s == 'L':
    t=t+25
    if p == 'Y':
        t=t+3
if c == 'Y':
    t=t+1
print(f"Your final bill is: ${t}")

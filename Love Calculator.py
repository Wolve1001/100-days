print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").upper()
name2 = input("What is their name? \n").upper()
n=name1+name2
t=n.count("T")
r=n.count("R")
u=n.count("U")
e=n.count("E")
ten=str(t+r+u+e)
L=n.count("L")
O=n.count("O")
V=n.count("V")
E=n.count("E")
one=str(L+O+V+E)
s=int(ten+one)
if s<10 or s>90:
    print(f"Your score is {s}, you go together like coke and mentos.")
elif 40<s<50:
    print(f"Your score is {s}, you are alright together.")
else:
    print(f"Your score is {s}.")

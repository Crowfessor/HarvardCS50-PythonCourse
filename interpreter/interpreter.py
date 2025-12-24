x, y, z = input("Enter the expression : ").split(" ")

if y == "+":
    finalized = float (x) + float(z)
    print(finalized)
elif y == "-":
    finalized = float (x) - float(z)
    print(finalized)
elif y == "/":
    finalized = float (x) / float(z)
    print(finalized)
elif y == "*":
    finalized = float (x) * float(z)
    print(finalized)


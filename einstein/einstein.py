c = 300000000
#E = m * c**2

def main():
    m = int(input("Input the mass please: "))
    print("E= ", calc(m))

def calc(m):
    return m* (c**2)

main()

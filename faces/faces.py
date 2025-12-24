def main():
    mystr = input("This is a faces converter: ")
    print(mystr)
    mystr = convert(mystr)
    print(mystr)

def convert(mystr):
    mystr = mystr.replace(":)", "🙂")
    mystr = mystr.replace(":(","🙁")
    return mystr

main()

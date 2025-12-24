import sys



if len(sys.argv) == 2 and sys.argv[1][-2:] == "py":
    try:
        with open(sys.argv[1]) as file:
            olines = 0
            for line in file:
                if not line.lstrip().startswith("#") and line.lstrip() != '':
                    olines += 1
        print(olines)
    except FileNotFoundError:
        sys.exit("File does not exist")
elif sys.argv[1][-2:] != "py":
    sys.exit("Not a python file")
elif len(sys.argv) < 2:
    sys.exit("Too few command-şine arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

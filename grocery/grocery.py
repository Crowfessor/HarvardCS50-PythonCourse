grocery_list={}


while True:
    try:
        groceries=input().upper()
    except EOFError:
        print()
        break
    if groceries.upper() in grocery_list:
        grocery_list[groceries.upper()] += 1
    else:
        grocery_list[groceries.upper()] = 1

for groceries in grocery_list.keys():
    print(grocery_list[groceries], groceries)

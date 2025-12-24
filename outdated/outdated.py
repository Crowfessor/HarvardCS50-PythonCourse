months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]




while True:
        user_input= input("Date: ").rstrip()
        if "/" in user_input:
            month,day,year = user_input.split("/")
        elif "," in user_input:
            user_input = user_input.replace(",","")
            month,day,year = user_input.split(" ")
            if month in months:
                 month = months.index(month)+1

        try:
            if int(month) > 12 or int(day)>31:
                continue
            else:
                break
        except ValueError:
             continue


print(year+ '-' + f"{int(month):02}" + '-' f"{int(day):02}")


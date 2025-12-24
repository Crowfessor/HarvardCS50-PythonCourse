def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_without_dollar = float(d.replace('$',''))
    return d_without_dollar


def percent_to_float(p):
    percent_without_percentagesign = float(p.replace('%','')) / 100
    return percent_without_percentagesign


main()

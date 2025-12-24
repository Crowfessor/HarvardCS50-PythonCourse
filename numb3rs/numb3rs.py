import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = (
        r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\."
        r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\."
        r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\."
        r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"
        )
    valid = re.search(pattern , ip)
    if valid :
        for i in range(1,5):
            if int(valid.group(i))> 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()

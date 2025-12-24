import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert_hours(h, am_pm):
    h = int(h)
    if am_pm == "PM" and h != 12:
        return h + 12
    if am_pm == "AM" and h == 12:
        return 0
    return h


def convert(s):
    matches = re.search(
        r"^(?P<h1>\d{1,2})(?::(?P<m1>\d{2}))? (?P<am_pm1>AM|PM) to "
        r"(?P<h2>\d{1,2})(?::(?P<m2>\d{2}))? (?P<am_pm2>AM|PM)$",
        s
    )

    if matches is None:
        raise ValueError

    h1 = matches.group("h1")
    h2 = matches.group("h2")
    m1 = matches.group("m1")
    m2 = matches.group("m2")
    am_pm1 = matches.group("am_pm1")
    am_pm2 = matches.group("am_pm2")

    # Saat aralığı kontrolü
    if not (1 <= int(h1) <= 12 and 1 <= int(h2) <= 12):
        raise ValueError

    # Dakikaları normalize et
    m1 = int(m1) if m1 is not None else 0
    m2 = int(m2) if m2 is not None else 0

    if not (0 <= m1 <= 59 and 0 <= m2 <= 59):
        raise ValueError

    # Saatleri 24 saat formatına çevir
    h1 = convert_hours(h1, am_pm1)
    h2 = convert_hours(h2, am_pm2)

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


if __name__ == "__main__":
    main()

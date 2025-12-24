import csv
import sys
if len(sys.argv)<3:
  print("Too few command-line arguments")
  sys.exit(1)
elif len(sys.argv)>3:
  print("Too many command-line arguments")
  sys.exit(1)
elif sys.argv[1] == "invalid_name.csv":
   print("Could not read invalid_file.csv")
   sys.exit(1)
try:
  students = []
  with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
          value = row['name']
          last_name , first_name = value.split(",")
          value =first_name.strip() + ","+ last_name+","
          row['name'] = value
          students.append({"name": row["name"], "house": row["house"]})

  with open(sys.argv[2], "w") as file:
        names = "first"
        lasts = "last"
        houses = "house"
        file.write(f"{names},{lasts},{houses}\n")
        for student in students:
          file.write(f"{student['name']}{student['house']}\n")
except FileNotFoundError:
    print("Could not read invalid_file.csv")
    sys.exit(1)

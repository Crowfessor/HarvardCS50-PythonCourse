import requests
import sys
import json

API_KEY = "206209b1641d61307d7969ac40379db92e4fd33635d4b6c2b225e629670e5fa7"

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")


try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

url = "https://api.coincap.io/v2/assets/bitcoin"
headers= {"Authorization": f"Bearer {API_KEY}"}


try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
except requests.RequestException as e:
    sys.exit(f"Request failed: {e}")

data = response.json()
price = float(data["data"]["priceUsd"])
#["bpi"] ["USD"]
total = bitcoins * price
print(f"${total:,.4f}")



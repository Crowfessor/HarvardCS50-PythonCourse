fruits = {
    'apple': 130,
    'avocado': 50,
    'cantaloupe':110,
    'grapefruit': 130,
    'grapes': 50,
    'sweet cherries': 100,
    'kiwifruit': 90,
    'pear': 100
}

fruit = input("Item: ").lower()

if fruit in fruits:
    print("Calories: ", fruits[fruit])

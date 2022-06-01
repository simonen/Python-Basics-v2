product = input()
prod_type = ""

if product == "banana" or product == "apple" or product == "kiwi" or product == "cherry" or product == "cherry" or \
    product == "lemon" or product == "grapes":
    prod_type = "fruit"
elif product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot":
    prod_type = "vegetable"
else:
    prod_type = "unknown"

print(prod_type)
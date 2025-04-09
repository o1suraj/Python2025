products = [
    {"name": "Ktm", "price": 19000},
    {"name": "BMW", "price": 18000},
]
 
carrier =[
    {"namecompany":"National post","Fees": 5},
    {" DHL Express":"National Express","Fees": 10},
] 
# we do a loop to display all the products
for index, product in enumerate(products):
    print(f"For {product["name"]} press {index}")

# us ea input to get user choice
while True:
 user_product_index = input("Enter the choice num: \n")
try:
    user_product_index = int(user_product_index)
    # we need to check if the numbers is greater or equal than 0 and less than number of products
    if user_product_index >= 0 and user_product_index < len(products):
             break
    else:
        print("This product does not exist")
except ValueError:
    print("Please enter num only")

user_product = product[user_product_index]    
print("Burger 10 dollar Press 1")
print("Pizza is 12 dollar")
print("Sushi 15 dollar press 3")
Meal_Desired = int(input("Enter the choice no"))
Meal_Quantity = int(input("Enter the Quantity"))

if (Meal_Desired == 1):
    price = 10
elif(Meal_Desired == 2):
    price = 12
elif(Meal_Desired == 3):
    price = 15
else :
    print("thats not in the menu")

Total_price = price * Meal_Quantity
print (Total_price)
if (Total_price >= 100 and Total_price < 200):
    Discount = 10/100
elif (Total_price > 200):
    Discount = 20/100
else :
    Discount = 1
    
    
    
Price_with_Discount = Total_price * Discount
print(f"Total price = {Total_price}") 
print(f"Total price after discount = {Price_with_Discount}")  
print(f"Discount%={Discount}")      
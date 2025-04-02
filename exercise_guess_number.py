import random
my_num = random.randint(0, 100)

while True:
    guess_num = int(input("Enter you guess"))
    if guess_num > my_num:
        print(f"Try smaller num than {guess_num}")
        

    elif guess_num < my_num:  
        print(f"Try bigger num than {guess_num}")
        

    else:
        print("You Won") 
        break




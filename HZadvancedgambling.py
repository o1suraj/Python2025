user = {}
usernum_max = 0
while True:
    data = int(input("Enter the num "))
    if usernum_max < 7 and data != data in user:
        usernum_max += 1
        user.add(data)
    elif data == data in user:
        print("The no exists try another")
    else:
        print("All nums are done")
        
win = {10,35,32,41,43,45,50}
Won = user.intersection(win)
win_length = len(won)
if win_length == 3:
    print("You won $4")
elif win_length == 4:
    print("You won $15")
elif win_length == 5:
    print("You won $200")  
elif win_length == 6:
    print("You won $30000")      
elif win_length == 7:
    print("You won $5 000 000")
else :
    print("Try again.Better luck next time")    
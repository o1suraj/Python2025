Max_attempt = 5
Attempt_no = 0
while True:
    if Attempt_no < Max_attempt:
        capital = input("Enter the capital of Japan\n")
        Attempt_no += 1
        if (capital!="Tokyo" and capital!="tokyo"):
            print(f"You have remain attempt  {Max_attempt-Attempt_no}")
            
        else: 
            print("You are correct")  
            break  
    else:
        print("Limit try finished")
        break
variable_total = 0
data = 0
while True:
   try: 
    data = int(input("Enter the num"))
    if data != 0:
        variable_total = variable_total + data
        
    else:
        print (variable_total)
        break    
   except ValueError:
      print("The value is wrong") 
print(f"Variable total is {variable_total}")    
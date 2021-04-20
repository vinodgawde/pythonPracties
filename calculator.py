# write a program program which will keep adding a stream of num  inputted by user. adding stops as soon as user process q key on the keyboard
sum=0
while(True): #loop
    userInput=input("enter the price = ")
    if (userInput != 'q'):
        sum=sum+int(userInput)
        print(f"order total so far {sum} \n")
    else:
        print("total bill is =",sum,"\nThanks to shopping with us.")
        break
    
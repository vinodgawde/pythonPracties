with open('currency.txt') as f:
    lines=f.readlines()

currencyDict = {}
for line in lines:
    parsed=line.split("\t") #convert string to list
    currencyDict[parsed[0]]=parsed[1]

amount = int(input("Enter amount \n"))
print("Enter the name of currency you want to convet this amount to ? \n""Avilable option\n")
[print(item) for item in currencyDict.keys()]
currency = input("Plz enter one of this value\n")
print(f"{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}")
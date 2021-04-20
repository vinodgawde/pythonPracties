# calculate the factorial of given number

'''num=int(input("enter the number\n"))
for i in range(1,num+1):
    factorial=factorial * i
    print(factorial)
    i=i+1'''

def factorial(number):
    if (number==0 or number==1):
        return 1
    else:
        return number * factorial(number-1)

def factorialTrailingZeros(number):
    #i=5
    #num!=num//i.num//i*i....
    i=5
    count=0
    while(number//i!=0):
        count += int(number/i)
        i=i*5
    return count

if __name__ == '__main__':
    number=int(input("enter the number \n"))
    #fact=factorial(number)
    #print(f"factorial is {fact}")
    print(factorialTrailingZeros(number))
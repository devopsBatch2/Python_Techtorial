






print ("User enter a number")
num = int(input())

#I have to start checking from possible divisors
#What is the smaller number that you can divide the non prime numbers other than 1?
is_prime = True
posible_divisor = 2
while posible_divisor < num:
    if num % posible_divisor == 0:
    #When this if statement gets executed it means given number is not prime
    #Whenever this if statement gets executed I dont to have chek rest of the 
    #possible divisors to understand if it is a prime
    #How can I tell the code given number is not prime?
        is_prime =False
        break
    posible_divisor += 1
       # print("it is not a prime")
if is_prime:

    print("This is a prime number")
else:
    print("This not a prime number")



    


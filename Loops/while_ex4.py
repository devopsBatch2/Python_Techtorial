
#Ask user to enter a integer number and print out all the divisors of given integer number
# 6------> divisors of 6 =1,2,3,6
#10 = 1,2,7,10
#14==1,2,7,14

#Posible dividers of given number
#starts from 1 --> ends at the fiven number itself

print("Enter integer number")
num = int(input())
possible_divisor = 1

s = ""

while possible_divisor <= num:
    #since we have the posible divisor , but we are not sure 
    #if we can divide the number or not
    #How can i understand if_posible dividsor is 0 it means posible_divisor

    if num % possible_divisor == 0:
        s+= str(possible_divisor)+", "
    possible_divisor += 1

print(s.removesuffix(", ") , "are the dividsors of the number")
        #print(f"{possible_divior}  is a divisor of the number)
  

  

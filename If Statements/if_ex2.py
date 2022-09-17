
#Ask user the enter a positive integer nimber 
#check if ithe givern mumber is within 2 of a multiple 0f 10
# if it within 2 of a miltiple 10 print 
# Your number is within 2 of a  multiplin 10
#if not print your number didn't match the executed requirement

#10  - 20 - 30-  40-   50 --50 on

#If the user gives 21 -->  your number  is within 2 0f a multiple 10
#If the user gives 43 --> your number   is within  0f a multiple 10
#f the user gives 39 -->  your number  is within 2 0f a multiple 10
#If the user gives 23 --> your number   is within 2 0f a multiple 10

# 9 --> 




print("Enter a positive integer number")
num = int(input())

remainder = num%10

if remainder >= 8 or remainder <= 2:
   print("Your number is within 2 of a multiple  10")
else:
    print("Your number didn't match the expected requirement")


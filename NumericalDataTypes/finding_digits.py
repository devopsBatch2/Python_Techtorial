
from unicodedata import digit


a = 123
 # find the multiplication of digits of the number a
# number a will always have three digit number
 # 2 * 3 * 4 =24
 # when we find remainder with 10. it will give us the last digit of the number
#when I divdde the number by 10 it will remive the last sigit



#integer division will give us onky the integer part of the division
#for example
#21/5 is 4.20 but if I use integer division operator
# 
 


last_digit= a % 10  #gives 3
print (last_digit)
#following line will remove the last digit of a variable

a = a // 10     #removes 3
middle_digit = a %10
a = a //10
first_digit = a%10

multiplication = last_digit*middle_digit*first_digit
print ("multiplication result of all digit is" ,multiplication)

# b =34
# print(b%10)

# c = 67
# print(c % 10)

# d = 105 
# print(d %10)

# e = 1273
# print(e % 10)
















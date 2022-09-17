
nums =[1,2,10,11,13,17,21,26]

#from the given list find sum of all the even numbers
sum = 0
sum_odd = 0
for number in nums:
    if number % 2 == 0:
        sum += number
    else:
        sum_odd += number
print("Sum of all the even numbers from list is",sum)
print("Sum of all the odd numbers  is",sum_odd)


#Ask user to give you two integer number
#Find the sum of these two integer number
# If sum of these two integer is smaller than 10
#print sum of these two number is 10
#if sum of these two number is between 10 --19 inclisive
#print sum of these two number is 20
#For all other conditions
#print the actual sum of these two number
 
print("Enter two integer number")
num1 = int(input())

print("Enter second number")
num2 = int(input())

sum = num1 + num2

if sum<10:
    print("sum of these two numbers is 10")
elif sum>=10 and sum<=19:
    print("sum of these the two numbers is 20")
else:
    print("sum of these two nimbers is {sum}")














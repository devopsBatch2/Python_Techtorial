

print ("Enter a number")
num1 = int(input())

print("enter a number smaller than first one")
num2 = int(input())

copyOfnum2 = num2
num2 = num2 + 1
sum = 0
while num2 < num1:
    sum += num2
   # print("in the loop" ,num2)
    num2 = num2 + 1
print(f"Sum of the numbers between {num1} and {copyOfnum2} is {sum}")
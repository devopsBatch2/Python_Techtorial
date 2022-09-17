

num1 = 5
num2 = 7

if num1 < num2:
    print(f"{num1} is less than {num2}")
#

if num2<num1:
    print(f"{num2} is less than {num1}")

is_num2_bigger = num2>num1

if is_num2_bigger:
    print("num2 is bigger than num1")

# Ask user to enter a string
# If user enters a string with all lower print you entered correct cases

print("Enter a string")
str = input()
is_lower = str.islower()

if is_lower:
    print("You entered correct cases")
    print("because you entered all lower")#line 1 and line 2 is inside the if statement so they depend on condition
print("you enterd a string") # for any case executed this lane , because this statement out of the if ccondition
    
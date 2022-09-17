
#When we want to reuse the piece of code or algoritm
# we create functions and reuse them

#syntax of creating a method is -------> def method_name

def print_name():
    print("Techtorial.")

#Methods only work when they got called
print_name()

#Let's create a method for greeting
# It will take user's name as argument and will print
# Hello User'sName

def print_greeting(name):
    print(f"Hello {name} ZAK")

print("Enter your name")
user_name = input()
print_greeting(user_name)

print(type(print_greeting(user_name)))
print(type(user_name.lower()))

def get_greeting(name):
    return f"Hello {name}"

    # Methods includes what is indented but it is recomended to leave
    # 2 lines of space after thelast line of method
print(type(get_greeting("John")))
greeting1  = get_greeting ("John")
print("Type of greeting is" ,greeting1)
print(greeting1)

print(get_greeting ("Max"))
print(get_greeting("Sofi"))
print(get_greeting ("Stevie"))

#Create a method to find sum of given two integers
# GIven means the method will take it as parameter
# Add an if statement in this method so it will print error occured
# If type of num1 or type of num2 is not float or integer

def sum(num1,num2):
    addition  = num1 + num2
    s      = str(type(addition))
    if "int" in s or "float" in s:
        return addition
    else:
        return "An error occured."

print(sum("A","B"))
print(sum(1,3))

def sum2(*nums):
    sum = 0
    for element in nums:
        sum += element
    return sum
print(sum2(1,5,6,8,9))




  
   # print("")

    #return num1 + num2
#print (type(type (4)))


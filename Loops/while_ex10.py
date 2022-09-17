#Ask user enter  a string
#If the given string contains any duplicated letter 
#print string has duplicated letter
#otherwisw print string consists of unique letters

print("Enter a string")
str = input()

#we should check for each letter , if there is duplicate
index = 0
while index < len(str):
    if str.count(str[index])>1:
        is_unique = False
        break
    index += 1

if is_unique:
    
    print("String consists of unique letters")

else:
    print("String has duplicated letters ")
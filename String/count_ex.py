print("Enter first string")
str1 = input()

print("Enter second string")
str2 = input()


# If the first string doesnt contain the second string

count_of_second = str1.count(str2)
#print(count_of_second)
is_contain = bool(count_of_second)
print(is_contain)
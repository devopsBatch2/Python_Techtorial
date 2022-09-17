
print("Enter a text with x'es")
str = input()

first_ch = str[0]
last_ch = str[-1]
middle_str = str[1:-1]
middle_str = middle_str.replace("x","")

print(first_ch+middle_str+last_ch)








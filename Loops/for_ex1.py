
# ask user a given string dublicate ech letter in given string
#input abc
#output aabbcc
#input def
#output ddeeff

import abc


print("Enter a string")
str = input()

duplicated = ""

for l in str:
    duplicated = duplicated + l
    print ("This print shows evolution of the suplicated" , duplicated)
    duplicated = duplicated + l
    print ("This print shows evolution of the suplicated" , duplicated)
print(duplicated)

#for l in str:
#    str += l
#print(str)



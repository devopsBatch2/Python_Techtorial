
#Using in operator we can check specified



list =[1,2,3,4,5]

if 2 in list:
    print("2 is in the list")

if 11 in list:
    print ("11 is in the list.")

    #not in operator we will check if the specified value is not in the 
    #iterable objects

if 6 not in list:
    print (6, "is not in the list")

print ("Enter a random digit")
digit = int(input())

if digit in list:
    print("You have won a prize")

elif digit not in list:
    print ("maybe, next time.")

# IN operator can be used for every iterable object


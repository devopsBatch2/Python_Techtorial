
fruits = ("strawberry","apple","orange","banana") # parantesis ---> tuple
                                                #{}-----> set
                                                #[]-------> list

print(fruits)

print(type(fruits))

print(fruits.index("apple"))
print(fruits.count("orange"))
# Accesing the elemets of atuple

# WE can use index numbers as we did with list
#getting the third element ffrom tuple

print(fruits[2])

# Using for loop with tuples 
for element in fruits:
    print(element)

# from this tuple pirnt out first fruit name 
# that has odd length .If there is no fruit with odd length print odd length coudn't be found

# I have to check length of each  fruits until i encounter a odd one
#fruits = ("strawberry","apple","orange","banana","orange")
odd_fruit = ""
for fruit  in fruits:
    if len(fruit) % 2 != 0:
        # I have found odd length
        odd_fruit = fruit
        break

if odd_fruit!="":
    print("First odd fruit is ", odd_fruit)
else:
    print("First odd length fruit  is not found" )
   
        
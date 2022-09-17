
s = set()

print(type(s))
print(s)
s.add("new value")

print(s)

s = {}

print(type(s))

# Using set() function we can convert lists in to set
# how we can remove the duplicates from the list below?

list = ["s","s",2,2,4,5,7,3,6,3,2]

set1 = set(list)
print(set1)
print(type(set1))

# clear()
set1.clear()
print(set1)
print(type(set1))

#copy method
list = ["s","s",2,2,4,5,7,3,6,3,2]

set1 = set(list)
print("from line 31", set1)

set2 =  set1.copy()

print("set 2 from line 35" , set2)
print(type(set2))






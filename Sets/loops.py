

# Is set objects is iterable ?
# set object are iterable
s1 = { "new","value2","value3","value4"}

# Sets don't have index numbers

for element in s1:
    print(element)

str = "Python"
s2 = set(str)
print(s2)
print(str)


print(str[0])
print(str[-2])
print(str[-4])

index = 0
while index < len(str):
    print(str[index])
    index+=1
for x in str:
    print(x)

for elemment in s2:
    print(element)
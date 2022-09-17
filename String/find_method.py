
s = "Python"
print(s.find('y')) #1

print(s.find('o')) #4

s1 = "Java"
print(s1.find("va")) #2

print(s1.find('al')) #-1

print(s1.find("z"))  # -1
# index of first a present in the string

print(s1.find('J')) #0 

print(s1.rfind("a"))  # 3 because index of last a present in the string

# index of last a present in the string means same as highest indec numver of a

#I want to find indec of second a present in the string 'a'
#I can find the lowest index for a true

lowest_a = s1.find("a")

s1_newVersion = s1[lowest_a + 1:]

index_of_second_a = s1_newVersion.find("a")

print(f"index of second a is {index_of_second_a}")
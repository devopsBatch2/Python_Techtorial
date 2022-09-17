
# There are some methods we can compare two set with each other

s1 = {1,7,9,3}

s2 = {2,7,9,5}

# difference method will get the elements present
# in set, that is not present in the other set

print(s1.difference(s2))

print(s2.difference(s1))

print(type(s2.difference(s1)))

# intersection

s1 = {1,7,9,3}
s2 = {2,7,9,5}

print(s1.intersection(s2))
print(type(s1.intersection(s2)))


# Issubset
# It checks given set is present in the other set or not

set = {1,2,3,4,5}
set2 = {2,3,4}

print(set2.issubset(set))

# Issuperset
# It checks if the set is a superset of the given set

print(set.issuperset(set2))
print(set2.issuperset(set))

# update
# Intersection_update -- it will remove all the elements that are not present in the other set

s1 = {1,2,3}

s2 ={2,3}
s1.intersection_update(s2)
print(s1)

# difference_update

s1 = {1,2,3}

s2 ={2,3}
s1.difference_update(s2)
print(s1)
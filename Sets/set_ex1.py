# Given two lists a,b .Check if two lists have at least one common elements
from subprocess import list2cmdline


list1 = [1, 2, 3, 4, 5]

list2 = [5, 6, 7, 8, 9]

# Checks if two lists have 
# at least one elements common in them.

set1 = set(list1)
set2 = set(list2)

common_elements =set1.intersection(set2)

# if len(common_elements) >=1:
#     print("True")
# else:
#     print("False")

is_there_common = len(common_elements) >= 1

print(is_there_common)

nums = [1,2,3,1,2,3,4,2,2,2]


# Remove all the number '2's from this list

# for number in nums:
#     if number ==2:
#         nums.remove(number)

# print(nums)

count = 0
for number in  nums:
    if number ==2:
        count+=1
print(count)

for i in range(count):
    nums.remove(2)
print(nums)





nums = [1,2,3,1,2,3,4,2,2,2]

newlist = nums.copy()

for number in newlist:
    if number == 2:
        nums.remove(2)
print(nums)
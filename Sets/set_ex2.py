
s = {2,2,3,4,5,7}
s2 = {4,10,2,5,44}

#find out min number from the s and
# multiply with the max number of s2
min = 0
# In the first iteration of the loop I should
# change the value of the min but later on I should only change 
# it when the min is bigger tahn number
# in the loop below how can I understand it is the first iteration 

count_of_iteration = 0
for number in s:
    if count_of_iteration == 0:
        min = number
                     # number I should ask from ZALKAR
    if number < min:
            #if code comes to tis line it means min is bigger than number
            min = number
    count_of_iteration += 1
print(min)

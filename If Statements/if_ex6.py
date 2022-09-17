
#In the factory we need to crate a programm that can
#find if we can do the shipment and if we can do the shipment
#it will tell use how many small package we should ship
#first we ned to get total kilogramm of the shipment
#to reach this totall kilogramm of shipment we can use small and big packages
#every  big is  packages 5 kilogrammand every small packages is a1 kilogramm
#WE have limited amount of small and big packages
#Ask user how many big and how many small packages they have
#Ask user what is the totall goal kilogramm of the shipment
#Print weather they can sheap , if they can ship print how many 


















print ("Enter the kilogramm we need ship")
goal_ship = int(input())

print("Enter amount of small packages you have")
count_of_small = int(input())

print("Enter amount of big packages you have")
count_of_big = int(input())

needed_big_packages =goal_ship // 5

# If I dont have enough big packages to  reach goal kilogramm
#can 
if needed_big_packages<=count_of_big:
    #How many small package i need
    needed_small_packages = goal_ship%5
    if needed_small_packages <= count_of_small:
        print(f"I can do the sipment an di need  {needed_small_packages} amount of small package")
    else:
        print("I cannot do the shipment")
else:
    kilogramm_i_have = count_of_big * 5;
    left_goal = goal_ship - kilogramm_i_have

    if left_goal <= count_of_small:
        print(f"I can do the shipment and i need {left_goal} amount of small boxes")
    else:
        print("I cannot do  the shipment")























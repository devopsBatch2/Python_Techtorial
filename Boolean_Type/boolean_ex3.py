
#Veera wants to lose 10 pounds in one month
#There miltuple conditions to lose 10 pounds in a month
#Veera needs to  walk 10000 steps daily or needs to run at least 4 miles a day
#and addition to those , Veera needs eat less tahn 1500 calories daily
#We should create a programm to calculate if Veera can loose weight or not




walking_steps = 500
running_distance = 4
daily_calory = 1500

can_loose_waigth = (walking_steps >= 10000 or running_distance >= 4) and daily_calory < 1500

print ("Veera can loose waigth" , can_loose_waigth)



##from sre_constants import IN


speed_limit_IN, speed_limit_others =70,55

print("What speed are you traveling at the moment ")
speed_of_driver = int(input())

print("What state are you in at the  moment")
state_in = input()

is_in_IN = state_in =="IN"

ten_percent_up_IN = speed_limit_IN + speed_limit_IN * 10/100

ten_percent_up_Others = speed_limit_others + speed_limit_others*10/100

if is_in_IN and speed_of_driver<=speed_limit_IN:
    print("You are driving safe!")

elif is_in_IN and speed_of_driver>speed_limit_IN and speed_of_driver<=ten_percent_up_IN:
    print("Yellow WARNING")

elif is_in_IN and speed_of_driver > ten_percent_up_IN:
    print("$150 and 5 points")

elif not is_in_IN and speed_of_driver<speed_limit_others:
    print("You are driving safe")

elif not is_in_IN and speed_of_driver > speed_limit_others and speed_of_driver<=ten_percent_up_Others:
    print("CITATION")

elif not is_in_IN and speed_of_driver>ten_percent_up_Others:
    print("$100")
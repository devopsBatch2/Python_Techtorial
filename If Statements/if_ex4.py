
print("What season are in")
season = input()

print("How hot is the weater ")
w = int(input())

#if user enters 
if season.lower()== "summer":
    #if this line is getting executed if season is summer.
    if w<= 80 and w>=60:
        print("You can take the baby out")
    else:
        print("You should't take the baby out")
elif season.lower() == "winter":
    if w > -20:
        print("the babies can go out.")
    else:
        print("You should't take the baby out")


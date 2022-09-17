
#Ask user enter the date in format of  month/day/year 
                                       # mm/dd/yyy
#Convert given date like following examples
#03/06/2017         ----->March 6, 2017

#07/10/2022         
 #                   ------->July 10,2022

print("Enter a date in format of month/day/year, mm/dd/y")

date = int(input())
#first two character of the given date will give you the enumber of the month

month = date[0:2]
day   = date[3:5]
year  = date[-4:]

day = day.removeprefix("0")

if month == "01":
    print(f"January{day},{year}")
elif month =="02":
    print(f"February{day},{year}")
elif month =="03":
    print(f"March{day},{year}")
elif month =="04":
     print(f"April{day},{year}")
elif month =="05":
     print(f"May{day},{year}")
elif month =="06":
     print(f"June{day},{year}")
elif month =="07":
     print(f"July{day},{year}")
elif month =="08":
     print(f"August{day},{year}")
elif month =="09":
     print(f"September{day},{year}")
elif month =="010":
     print(f"October{day},{year}")
elif month =="11":
     print(f"Nowember{day},{year}")
elif month =="12":
     print(f"December{day},{year}")


#isalpha() method 
# it only returns true when all character of the string is letters

s = "This is text"
print(s.isalpha())

#False and the reason for that is space are not considered as letters

s = s.replace(" ","")
print(s.isalpha)




#isnumeric only returns true when 

s1 = "777-777-777"
print(s1.isnumeric())  #False because - is not a nkumeric type

print(s1.replace("-","").isnumeric()) #true

s1 = "77777berdgfh3"
print(s1.isnumeric())

#isalnum checks if the all string consist of letters ansd numbers
s1 = "777-777-777"
print(s1.isalnum())  #false

s2 = "string"
s3 ="77777777"
s4 = "478errit874iu"
print(s2.isalnum())
print(s2.isnumeric())
print(s2.isalpha())
######################################################################################
print(s3.isalnum())
print(s3.isnumeric())
print(s3.isalpha())

##################################################################################

print(s4.isalnum())
print(s4.isnumeric())
print(s4.isalpha())


#prefix -> will remove from the begining of the string
#suffix --> 

s = "Hello Python"



print(s.removesuffix("Python"))

print(s.removeprefix("Hello"))

#From the given websites string , print only the domain name of the website

web_site = input()
domain_name = web_site.removeprefix("www").removesuffix(".com")

print(domain_name)

str = "hello world"
print(str.removeprefix("el"))


 
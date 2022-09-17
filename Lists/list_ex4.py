
# Create a programm that will ask user ten full name
# After you  get 10 full name create email version of given 10
# name and store it inside list and print
# enter fullname
# John WIck
# enter full name
# MAx White


full_names = []
emails = []

for i in range(10):
    print("Enter a full name")
    f_name = input()
    full_names.append(f_name)
    f_name = f_name.replace(" ", "").lower()+ "@gmail.com"
    emails.append(f_name)

print(full_names)
print(emails)


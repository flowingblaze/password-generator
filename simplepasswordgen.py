import random

# welcomes user
print('Welcome to a Password Generator!')  

# what the generator will draw from to make the password
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVQXYZ!@#$%^&**())_)' 

# number of passwords the user wants to make
number = input('Amount of passwords to create: ') 
number = int(number) 

# the length of the requested passwords
length = input('Wanted password length: ') 
length = int(number) 

print('here are your passwords: ') 

# creating the passwords
for pwd in range(number): 
    passwords = '' 
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
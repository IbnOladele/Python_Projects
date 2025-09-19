#input password
password = input("insert password: ")       #define password to accept user input

#length checker
def password_length(user_input):      #a function to check the length of password
    if len(user_input) >= 8:
        return True
    else:
        return False
password_length(password)       #calling the function

def has_uppercase(user_input):        #a function to check if password has uppercase letters
    if any(i.isupper() for i in user_input):        #loop to check for uppercase letters
        return True
    else:
        return False
has_uppercase(password)         #calling the function

def has_special_characters(user_input):        #a function to check if password has special characters
    if any(i in "!@#$%^&*()-_+=<>?{}[]|:;\"'`~" for i in user_input):       #loop to check for special characters
        return True
    else:
        return False
has_special_characters(password)        #a function to check if password has numbers

def has_digits(user_input):
    if any(i.isdigit() for i in user_input):        #loop to check for numbers
        return True
    else:
        return False
has_digits(password)     #calling the function

#Loop to check password strength
if password_length(password) and has_uppercase(password) and has_special_characters(password) and has_digits(password) == True:     #conditions for strong password
   print(f"Password Strength: Strong")
elif password_length(password) or has_uppercase(password) or has_special_characters(password) or has_digits(password) == True:      #conditions for medium password
    print(f"Password Strength: Medium")
    if not password_length(password):       #check password length
        print("password is too short, try again!")
    elif not has_uppercase(password):       #check for uppercase
        print("password is weak, must contain at least one uppercase letter")
    elif not has_special_characters(password):      #check for special characters
        print("password is weak, must contain at least one special character")
    elif not has_digits(password):      #check for numbers
        print("password is weak, must contain at least one number")
else:
    print(f"Password strength: Weak")       #when all conditions fail, password is weak

print(password)     #Display password

#adding this comment to create a difference in the versions

import string
import getpass

def check_pwd():
    password = getpass.getpass("Enter Password: ")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count +=1
        elif char in string.digits:
            num_count += 1
        else:
            special_count +=1

    if lower_count >= 1:
        strength +=1
    if upper_count >= 1:
        strength +=1
    if num_count >= 1:
        strength +=1
    if special_count>=1:
        strength +=1

    if strength == 1:
        remarks = " Very Weak Password"
    elif strength == 2:
        remarks = "Weak Password"
    elif strength ==3:
        remarks = "Weak Password"
    elif strength == 4:
        remarks = "Hard Password"
    elif strength == 5:
        remarks = "Very Strong password"

    print('Your password has: ')
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{special_count} special characters")

    print(f"Password Strength:{strength}")
    print(f"Hint: {remarks}")

def ask_pwd(another_pwd=False):
    valid = False
    if another_pwd:
        choice=input('Do you want to enter another pwd (y/n): ')
    else:
        choice=input('Type y to check password complexity: ')

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print('Invalid, Try Again')

if __name__ == '__main__':
    ask_pw = ask_pwd()
    while check_pwd:
        check_pwd()
        ask_pw = ask_pwd(True)
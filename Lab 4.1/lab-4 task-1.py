import re

def is_valid_mobile(number):
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, number))

while True:
    mobile = input("Enter a 10-digit mobile number starting with 6, 7, 8, or 9: ")
    if is_valid_mobile(mobile):
        print("Valid mobile number.")
        break
    else:
        print("Invalid mobile number. Please try again.")
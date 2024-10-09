# Temperature Check
temp_c = input("Enter the current temp")
if(int(temp_c) > 30):
    print("it's a hot day")
else:
    print("The weather is cool")

#Password Checker
password = 1234
admin_p = input("Enter the password")
if(int(admin_p) == password):
    print("Access granted")
else:
    print("Access denied")

# Number Comparison
x = int(input("Enter a number"))
y = int(input("Enter another number"))
if(x > y):
    print(x)
elif(y > x):
    print(y)
else:
    print("They are equal")

# Positive, Negative, or Zero
num = int(input("Enter a number"))
if num < 0:
    print("number is negative")
elif num > 0:
    print("number is positive")
elif num == 0:
    print("number is zero")


# Day of the Week
num = int(input("Enter a number between 1 and 7"))
if num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
elif num == 7:
    print("Sunday")
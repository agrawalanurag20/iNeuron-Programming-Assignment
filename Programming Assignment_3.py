# Program 1
# Check if a Number is Positive, Negative or Zero
print("Program # 1 : Check if a Number is Positive, Negative or Zero")
num = int(input("Enter the number: "))
if num == 0:
    print(f"Entered number: {num} is Zero.")
elif num > 0:
    print(f"Entered number: {num} is Positive.")
else:
    print(f"Entered number: {num} is Negative.")
print('*'*5 + 'End' + '*'*5)

# Program 2
# Check if a Number is Odd or Even
print("Program # 2 : Check if a Number is Odd or Even")
num = int(input("Enter the number: "))
if num % 2 == 0:
    print(f"Entered number: {num} is Even.")
else:
    print(f"Entered number: {num} is Odd.")
print('*'*5 + 'End' + '*'*5)

# Program 3
# Check Leap Year
print("Program # 3 : Check Leap Year")
import calendar
yy = int(input("Enter the year in YYYY: "))
if calendar.isleap(yy):
    print(f"Entered year: {yy} is leap year.")
else:
    print(f"Entered year: {yy} is not a leap year.")
print('*'*5 + 'End' + '*'*5)

# Program 4
# Check Prime Number
print("Program # 4 : Check Prime Number")
num = int(input("Enter the number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"Entered number: {num} is not a Prime")
            break
    else:
        print(f"Entered number: {num} is a Prime")
else:
    print(f"Entered number: {num} is not a Prime")
print('*'*5 + 'End' + '*'*5)

# Program 5
# Print all Prime Numbers in an Interval of 1-10000
print("Program # 5 : Print all Prime Numbers in an Interval of 1-10000")
high = int(input("Enter the highest range:"))
num = 2
while num <= high:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(f"{num} is Prime number.")
    num = num + 1
print('*'*5 + 'End' + '*'*5)

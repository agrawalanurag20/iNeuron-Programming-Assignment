# Program 1
# convert kilometers to miles
print("Program # 1 : convert kilometers to miles")
km = float(input("Enter Value in Kilometers: "))
ml = km * 0.621371
print(f"{km} Km is equivalent to {ml} Miles.")
print('*'*5 + 'End' + '*'*5)

# Program 2
# convert Celsius to Fahrenheit
print("Program # 2 : convert Celsius to Fahrenheit")
cl = float(input("Enter Value in Celsius: "))
fh = (cl*9)/5 + 32
print(f"{cl} Celsius is equivalent to {fh} Fahrenheit.")
print('*'*5 + 'End' + '*'*5)

# Program 3
# Display Calender
print("Program # 3 : Display Calendar")
import calendar
yy = int(input("Enter the Year in YY: "))
mm = int(input("Enter the month in MM: "))
if mm < 0 or mm > 12:
    print("Please input correct month.")
elif mm == 0:
    print(calendar.calendar(yy))
else:
    print(calendar.month(yy, mm))
print('*'*5 + 'End' + '*'*5)

# Program 4
# solve quadratic equation
print("Program # 4 : solve quadratic equation")
import cmath
a = 2
b = 4
c = 2
dis = (b ** 2) - (4 * a * c)
root1 = (-b - cmath.sqrt(dis)) / (2 * a)
root2 = (-b + cmath.sqrt(dis)) / (2 * a)
print(f"The roots are : {root1} and {root2}")
print('*'*5 + 'End' + '*'*5)

# Program 5
# swap two variables without temp variable
print("Program # 5 : swap two variables without temp variable")
a = int(input('Enter value for a: '))
b = int(input('Enter value for b: '))
print(f"Value of a:{a} and value of b:{b}")
a,b = b,a
print(f"After swap Value of a:{a} and value of b:{b}")
print('*'*5 + 'End' + '*'*5)
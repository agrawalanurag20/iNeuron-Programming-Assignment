# Program 1
# To display Fibonacci sequence using recursion
print("Program # 1 : To display Fibonacci sequence using recursion")
num = int(input("Fibonacci sequence first (n): "))
def fibseq(n):
    """This recursive function will find out the fibonacci sequence"""
    if n <= 1:
        return n
    else:
        return (fibseq(n-1) + fibseq(n-2))

fib_seq = list()
for i in range(0, num):
    fib_seq.append(fibseq(i))
print(fib_seq)
print('*'*5 + 'End' + '*'*5)

# Program 2
# To Find Factorial of Number Using Recursion
print("Program # 2 : To Find Factorial of Number Using Recursion")
num = int(input("Enter the number: "))
def facto(n):
    """This recursive function will find out the factorial of a number"""
    if n <= 1:
        return (n)
    else:
        return (n * facto(n-1))

print(f"Factorial of number {num} is {facto(num)}")
print('*'*5 + 'End' + '*'*5)

# Program 3
# To calculate your Body Mass Index
print("Program # 3 : to calculate your Body Mass Index")
weigh = float(input("Enter your weight in Kg: "))
heigh = float(input("Enter your height in Cm: "))
def cal_bmi(w,h):
    """This function will find out the Body Mass Index"""
    return (w/ ((h/100)**2))

if heigh <= 0 or weigh <= 0:
    print("Weight and Height must be greater than zero.")
else:
    print(f"Your Body Mass Index is {cal_bmi(weigh,heigh)}")
print('*'*5 + 'End' + '*'*5)

# Program 4
# To calculate the natural logarithm of any number
print("Program # 4 : To calculate the natural logarithm of any number")
import math
num = float(input("Enter the number: "))
if num <= 0:
    print("Please enter value greater than zero.")
else:
    print(f"Natural logarithm of number {num} is {math.log(num)}")
print('*'*5 + 'End' + '*'*5)

# Program 5
# cube sum of first n natural numbers
print("Program # 5 : cube sum of first n natural numbers")
num = int(input("Enter the number: "))
def cube_sum(n):
    """This will return cube sum of first n natural numbers."""
    return (n**2 * (n+1)**2)/4

print(f"Cube sum of first {num} natural number is {cube_sum(num)}")
print('*'*5 + 'End' + '*'*5)
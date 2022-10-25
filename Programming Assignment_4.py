# Program 1
# To Find the Factorial of a Number
print("Program # 1 : To Find the Factorial of a Number")
num = int(input("Enter the number: "))
fact = 1
if num != 0:
    for i in range(1, num+1):
        fact = fact * i
else:
    fact = 0
print(f"Factorial of number {num} is {fact}")
print('*'*5 + 'End' + '*'*5)

# Program 2
# To Display the multiplication Table
print("Program # 2 : To Display the multiplication Table")
num = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")
print('*'*5 + 'End' + '*'*5)

# Program 3
# To Print the Fibonacci sequence
print("Program # 3 : To Print the Fibonacci sequence")
num = int(input("Fibonacci sequence first (n): "))
i = 0
fib_seq = []
while i < num:
    if i == 0 or i == 1:
        fib_seq.append(i)
    else:
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    i = i + 1
print(fib_seq)
print('*'*5 + 'End' + '*'*5)

# Program 4
# To Check Armstrong Number
print("Program # 4 : To Check Armstrong Number")
num = int(input("Enter the number: "))
num_a = str(num)
temp_num = 0
for i in range(0, len(num_a)):
    temp_num = temp_num + int(num_a[i])**len(num_a)
if num == temp_num:
    print(f"Number {num} is Armstrong Number.")
else:
    print(f"Number {num} is not Armstrong Number.")
print('*'*5 + 'End' + '*'*5)

# Program 5
# To Find Armstrong Number in an Interval
print("Program # 5 : To Find Armstrong Number in an Interval")
num1 = int(input("Enter start number: "))
num2 = int(input("Enter end number: "))
while num1 <= num2:
    num_a = str(num1)
    temp_num = 0
    for i in range(0, len(num_a)):
        temp_num = temp_num + int(num_a[i])**len(num_a)
    if num1 == temp_num:
        print(f"Armstrong Number : {num1}")
    num1 = num1 + 1
print('*'*5 + 'End' + '*'*5)

# Program 6
# To Find the Sum of Natural Numbers
print("Program # 6 : To Find the Sum of Natural Numbers")
num1 = int(input("Enter start number: "))
num2 = int(input("Enter end number: "))
sum = 0
for i in range(num1, num2+1):
    sum = sum + i
print(f"Sum of natural numbers between {num1} and {num2} is {sum}")
print('*'*5 + 'End' + '*'*5)
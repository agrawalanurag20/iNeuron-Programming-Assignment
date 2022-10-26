# Program 1
# To Find LCM
print("Program # 1 : To Find LCM")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    greater_num = num1
else:
    greater_num = num2
i = greater_num
while(True):
    if (greater_num % num1 == 0) and (greater_num % num2 == 0):
        lcm = greater_num
        break
    else:
        greater_num = greater_num + i

print(f"L.C.M. of numbers {num1} and {num2} is {lcm}")
print('*'*5 + 'End' + '*'*5)

# Program 2
# To Find HCF
print("Program # 2 : To Find HCF")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 < num2:
    smaller_num = num1
else:
    smaller_num = num2
i = smaller_num
j = 2
while (True):
    if (num1 % smaller_num == 0) and (num2 % smaller_num == 0):
        hcf = smaller_num
        break
    else:
        smaller_num = i / j
        j = j + 1

print(f"H.C.F. of numbers {num1} and {num2} is {hcf}")
print('*'*5 + 'End' + '*'*5)

# Program 3
# To Convert Decimal to Binary, Octal and Hexadecimal
print("Program # 3 : To Convert Decimal to Binary, Octal and Hexadecimal")
num = int(input("Enter the number: "))
temp = num
bin_value = ''
while temp > 0:
    bin_value = str(temp % 2) + bin_value
    temp = temp // 2
print(f"Binary Value of {num} : 0b{bin_value}")
print(bin(num))

temp = num
oct_value = ''
while temp > 0:
    oct_value = str(temp % 8) + oct_value
    temp = temp // 8
print(f"Octal Value of {num} : 0o{oct_value}")
print(oct(num))

temp = num
dec_lst = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
hex_lst = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
hex_value = ''
while temp > 0:
    temp_hex = str(temp % 16)
    idx = dec_lst.index(temp_hex)
    temp_hex = hex_lst[idx]
    hex_value = temp_hex + hex_value
    temp = temp // 16
print(f"Hexadecimal Value of {num} : 0x{hex_value}")
print(hex(num))
print('*'*5 + 'End' + '*'*5)

# Program 4
# To Find ASCII value of a character
print("Program # 4 : To Find ASCII value of a character")
char = input("Enter the character: ")
if len(char) > 1:
    print("Please enter single length character.")
else:
    asc_value = ord(char)
    print(f"ASCII value of character '{char}' : {asc_value}")
print('*'*5 + 'End' + '*'*5)

# Program 5
# To Make a Simple Calculator with 4 basic mathematical operations
print("Program # 5 : To Make a Simple Calculator with 4 basic mathematical operations")
while(True):
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    char = input("Enter A, S, M, D for Add, Sub, Mul, Div and E for Exit: ")
    if char == 'A':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif char == 'S':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif char == 'M':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif char == 'D':
        print(f"{num1} / {num2} = {num1 / num2}")
    elif char == 'E':
        break
    else:
        print("Please give correct input.")
print('*'*5 + 'End' + '*'*5)

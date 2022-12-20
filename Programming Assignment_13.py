# Program 1
#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H], C=50 and H=30
import math
def calc_fun(num):
    num1 = 0
    if type(num) == int:
        num1 = int(math.sqrt((2*50*num)/30))
    return num1

inp1 = input("Enter values in comma separated:")
val1 = list(inp1.split(','))
print(f"output : {list(map(calc_fun,list(map(lambda a: int(a), val1))))}")
print('*'*5 + 'End' + '*'*5)

# Program 2
#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
#element value in the i-th row and j-th column of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,¡Y-1.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
l1 = list()
l2 = list()
for i in range(0,num1):
    l1 = list()
    for j in range(0,num2):
        l1.append(i*j)
    l2.append(l1)

print(f"output: {l2}")
print('*'*5 + 'End' + '*'*5)

# Program 3
#Write a program that accepts a comma separated sequence of words as input and prints the
#words in a comma-separated sequence after sorting them alphabetically.
inp1 = input("Enter words in comma separated:")
val1 = list(inp1.split(','))
val2=list()
val2=sorted(val1)
for i in range(0,len(val2)):
    if i == len(val2)-1:
        print(val2[i],end='\n')
    else:
        print(f"{val2[i]},",end='')
print('*'*5 + 'End' + '*'*5)

# Program 4
#Write a program that accepts a sequence of whitespace separated words as input and prints
#the words after removing all duplicate words and sorting them alphanumerically.
inp1 = input("Enter words with space separated:")
val1 = list(set(inp1.split(' ')))
val2 = sorted(val1)
for i in range(0,len(val2)):
    if i == len(val2)-1:
        print(val2[i],end='\n')
    else:
        print(f"{val2[i]} ",end='')
print('*'*5 + 'End' + '*'*5)

# Program 5
#Write a program that accepts a sentence and calculate the number of letters and digits.
inp1 = input("Enter the string:")
lett_tst = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digi_tst = '0123456789'
no_letters = 0
no_digits = 0
for i in range(0, len(inp1)):
    if lett_tst.find(inp1[i]) != -1:
        no_letters = no_letters + 1
    if digi_tst.find(inp1[i]) != -1:
        no_digits = no_digits + 1

print(f"LETTERS {no_letters}, DIGITS {no_digits}")
print('*'*5 + 'End' + '*'*5)

# Program 6
#A website requires the users to input username and password to register. Write a program to
#check the validity of password input by users.
inp1 = input("Enter the password comma separated:")
val1 = list(inp1.split(','))
lett_caps_tst = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lett_smal_tst = 'abcdefghijklmnopqrstuvwxyz'
digi_tst = '0123456789'
char_tst = '$#@'
valid_pswd = list()
for i in range(0, len(val1)):
    caps_flg = 'N'
    smal_flg = 'N'
    digi_flg = 'N'
    char_flg = 'N'
    if len(val1[i]) >= 6 and len(val1[i]) <= 12:
        for j in range(0, len(val1[i])):
            if val1[i][j] in lett_caps_tst:
                caps_flg = 'Y'
            if val1[i][j] in lett_smal_tst:
                smal_flg = 'Y'
            if val1[i][j] in digi_tst:
                digi_flg = 'Y'
            if val1[i][j] in char_tst:
                char_flg = 'Y'
        if caps_flg == 'Y' and smal_flg == 'Y' and digi_flg == 'Y' and char_flg == 'Y':
            valid_pswd.append(val1[i])

print("valid passwords :",end='')
for i in range(0,len(valid_pswd)):
    if i == len(valid_pswd)-1:
        print(valid_pswd[i],end='\n')
    else:
        print(f"{valid_pswd[i]},",end='')
print('*'*5 + 'End' + '*'*5)
# Program 1
# To check if the given number is a Disarium Number
print("Program # 1 : To check if the given number is a Disarium Number")
num = int(input("Enter the number: "))
num_a = str(num)
temp_num = 0
for i in range(0, len(num_a)):
    temp_num = temp_num + int(num_a[i])**(i+1)
if num == temp_num:
    print(f"Number {num} is Disarium Number.")
else:
    print(f"Number {num} is not Disarium Number.")
print('*'*5 + 'End' + '*'*5)

# Program 2
# To print all disarium numbers between 1 to 100
print("Program # 2 : To print all disarium numbers between 1 to 100")
dis_num = list()
for i in range(1, 101):
    num_a = str(i)
    temp_num = 0
    for j in range(0, len(num_a)):
        temp_num = temp_num + int(num_a[j])**(j+1)
    if i == temp_num:
        dis_num.append(i)
print(f"Disarium Numbers between 1 to 100 are {dis_num}.")
print('*'*5 + 'End' + '*'*5)

# Program 3
# To check if the given number is Happy Number
print("Program # 3 : To check if the given number is Happy Number")
def ishappynum(n):
    num_a = str(n)
    val = 0
    for i in range(0, len(num_a)):
        val = val + int(num_a[i])**2
    return val

num = int(input("Enter the number: "))
res = num
if num > 0:
    while res != 1 and res != 4:
        res = ishappynum(res)
    if res == 1:
        print(f"Number {num} is a Happy Number.")
    elif res == 4:
        print(f"Number {num} is not a Happy Number.")
else:
    print("Enter number greater than zero.")
print('*'*5 + 'End' + '*'*5)

# Program 4
# To print all happy numbers between 1 and 100
print("Program # 4 : To print all happy numbers between 1 and 100")
def ishappynum(n):
    num_a = str(n)
    val = 0
    for i in range(0, len(num_a)):
        val = val + int(num_a[i])**2
    return val

num = 1
happy_num = list()
while num <= 100:
    res = num
    while res != 1 and res != 4:
        res = ishappynum(res)
    if res == 1:
        happy_num.append(num)
    num = num + 1
print(f"All Happy numbers between 1 and 100 are {happy_num}.")
print('*'*5 + 'End' + '*'*5)

# Program 5
# To determine whether the given number is a Harshad Number
print("Program # 5 : To determine whether the given number is a Harshad Number")
def isharshadnum(n):
    num_a = str(n)
    val = 0
    for i in range(0, len(num_a)):
        val = val + int(num_a[i])
    if n % val == 0:
        return True
    else:
        return False

num = int(input("Enter the number: "))
res = num
if num > 0:
    if isharshadnum(num):
        print(f"Number {num} is a Harshad Number.")
    else:
        print(f"Number {num} is not a Harshad Number.")
else:
    print("Enter number greater than zero.")
print('*'*5 + 'End' + '*'*5)

# Program 6
# To print all pronic numbers between 1 and 100
print("Program # 6 : To print all pronic numbers between 1 and 100")
def ispronicnum(n):
    pronic_flag = False
    for i in range(1, n+1):
        if n == i * (i+1):
            pronic_flag = True
            break
    return pronic_flag

num = 1
pronic_num = list()
while num <= 100:
    if ispronicnum(num):
        pronic_num.append(num)
    num = num + 1
print(f"All pronic numbers between 1 and 100 are {pronic_num}.")
print('*'*5 + 'End' + '*'*5)







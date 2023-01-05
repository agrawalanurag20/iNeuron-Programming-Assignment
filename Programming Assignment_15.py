# Program 1
#Please write a program using generator to print the numbers which can be divisible by 5 and
#7 between 0 and n in comma separated form while n is input by console.
class gen_num:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def gen_number(self):
        for i in range(self.num1,self.num2):
            if i % 7 == 0 and i % 5 == 0:
                yield i

num_limit = int(input("Enter the number: "))
c1 = gen_num(0,num_limit+1)
c2 = c1.gen_number()
print(c2.__next__(),end='')
while True:
    try:
        print(',',c2.__next__(),sep='',end='')
    except:
        print("")
        break

print('*'*5 + 'End' + '*'*5)

#Program 2
#Please write a program using generator to print the even numbers between 0 and n in comma
#separated form while n is input by console.
class even_num:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def even_number(self):
        for i in range(self.num1,self.num2):
            if i % 2 == 0:
                yield i

num_limit = int(input("Enter the number: "))
c1 = even_num(0,num_limit+1)
c2 = c1.even_number()
print(c2.__next__(),end='')
while True:
    try:
        print(',',c2.__next__(),sep='',end='')
    except:
        print("")
        break

print('*'*5 + 'End' + '*'*5)

# Program 3
#Please write a program using list comprehension to print the Fibonacci Sequence in comma
#separated form with a given n input by console.
num = int(input("Enter the number: "))
i = 0
fib_seq = []
while i <= num:
    if i == 0 or i == 1:
        fib_seq.append(i)
    else:
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    i = i + 1

for j in range(0,len(fib_seq)):
    if j == len(fib_seq) - 1:
        print(fib_seq[j], end='\n')
    else:
        print(fib_seq[j],end=',')

print('*'*5 + 'End' + '*'*5)

# Program 4
#Assuming that we have some email addresses in the "username@companyname.com" format,
#please write program to print the user name of a given email address. Both user names and
#company names are composed of letters only.
str1 = input("Enter Email address: ")
str2 = str1[0:str1.find('@')]
print(f"Name is: {str2}")

print('*'*5 + 'End' + '*'*5)

# Program 5
#Define a class named Shape and its subclass Square. The Square class has an init function
#which takes a length as argument. Both classes have a area function which can print the area
#of the shape where Shape's area is 0 by default.
class shape:
    def area(self):
        print("Shape Area is: ", 0)

class square(shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        print("Sqaure Area is: ", self.length**2)

sh1 = shape()
sq1 = square(5)
sh1.area()
sq1.area()

print('*'*5 + 'End' + '*'*5)
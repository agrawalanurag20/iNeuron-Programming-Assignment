# Program 1
#Define a class with a generator which can iterate the numbers, which are divisible by
#7, between a given range 0 and n.
class gen_num:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def gen_number(self):
        for i in range(self.num1,self.num2):
            if i % 7 == 0:
                yield i

c1 = gen_num(0,141)
c2 = c1.gen_number()
for i in c2:
    print(i)
print('*'*5 + 'End' + '*'*5)

# Program 2
#Write a program to compute the frequency of the words from the input. The output
#should output after sorting the key alphanumerically.
inp1 = ''
for i in range (2):
    if i == 0:
        inp1 += input("Enter the string: ") + "\n"
    else:
        inp1 += input() + "\n"
l1 = sorted(list(inp1.split()))
s1 = sorted(set(inp1.split()))
for i in s1:
    print(i,":",l1.count(i))

print('*'*5 + 'End' + '*'*5)

# Program 3
#Define a class Person and its two child classes: Male and Female. All classes have a
#method &quot;getGender&quot; which can print &quot;Male&quot; for Male class and &quot;Female&quot; for Female
#class.
class Person:
    def __init__(self,gender):
        self.gender = gender
    def getGender(self):
        print("Gender is: ", self.gender)

class Male(Person):
    def __init__(self,gender,age):
        super().__init__(gender)
        self.age = age
    def getAge(self):
        print("Age is: ", self.age)
class Female(Person):
    def __init__(self,gender,age):
        super().__init__(gender)
        self.age = age
    def getAge(self):
        print("Age is: ", self.age)

m1 = Male('male',21)
f1 = Female('Female',24)
m1.getGender()
m1.getAge()
f1.getGender()
f1.getAge()
print('*'*5 + 'End' + '*'*5)

# Program 4
#Please write a program to generate all sentences where subject is in ["I","You"] and
#verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
sub1 = ["I", "You"]
verb1 = ["Play", "Love"]
obj1 = ["Hockey", "Football"]
for i in sub1:
    for j in verb1:
        for k in obj1:
            print(i,j,k)

print('*'*5 + 'End' + '*'*5)

# Program 5
#Please write a program to compress and decompress the string "hello world!hello
#world!hello world!hello world!".
import zlib
text="hello world!hello world!hello world!hello world!"
comp=zlib.compress(text.encode())
print("Compressed: ", comp)
decomp=zlib.decompress(comp).decode()
print("Decompressed: ", decomp)
print('*'*5 + 'End' + '*'*5)

# Program 6
#Please write a binary search function which searches an item in a sorted list. The
#function should return the index of element to be searched in the list.
lst = [2,6,8,9,12,23,25,28,34,45,56,78,89]
def bin_search(elem,lst):
    str = 0
    end = len(lst)
    count = 1
    while True:
        idx = (str + end) / 2
        if idx < 0 or idx > (len(lst) - 1) or count > len(lst):
            idx = -1
            break
        else:
            idx = int(idx)

        if elem == lst[idx]:
            break
        elif elem > lst[idx]:
            str = idx + 1
        elif elem < lst[idx]:
            end = idx - 1

        count += 1
    return idx

search_elm = 23

found_idx = bin_search(search_elm,lst)
if found_idx == -1:
    print("Element not found.")
else:
    print(f"Element {search_elm} found at index {found_idx}")

print('*'*5 + 'End' + '*'*5)
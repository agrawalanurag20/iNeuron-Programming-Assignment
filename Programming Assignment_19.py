# Program 1
#Create a function that takes a string and returns a string in which each character is repeated
#once.
def double_char(str1):
    tmp_str = ""
    for i in str1:
        tmp_str = tmp_str + i*2
    return tmp_str

print(double_char("Hello World!"))
print('*'*5 + 'End' + '*'*5)

# Program 2
#Create a function that reverses a boolean value and returns the string "boolean expected"
#if another variable type is given.
def reverse(bool1):
    if type(bool1) == bool:
        if bool1:
            return False
        else:
            return True
    else:
        return "boolean expected"
    return bool1

print(reverse(False))
print('*'*5 + 'End' + '*'*5)

# Program 3
#Create a function that returns the thickness (in meters) of a piece of paper after folding it n
#number of times. The paper starts off with a thickness of 0.5mm.
def num_layers(n):
    i = 1
    tmp_thick = 0.5
    while i <= n:
        tmp_thick = tmp_thick * 2
        i = i + 1
    return (tmp_thick/1000)

print(num_layers(21),"m")
print('*'*5 + 'End' + '*'*5)

# Program 4
#Create a function that takes a single string as argument and returns an ordered list containing
#the indices of all capital letters in the string.
def index_of_caps(str1):
    tmp_lst = list()
    for i in str1:
        if i.isupper():
            tmp_lst.append(str1.index(i))
    return tmp_lst

print(index_of_caps("eQuINoX"))
print('*'*5 + 'End' + '*'*5)

# Program 5
#Using list comprehensions, create a function that finds all even numbers from 1 to the given
#number.
def find_even_nums(n):
    tmp_lst = list()
    i = 1
    while i <= n:
        if i % 2 == 0:
            tmp_lst.append(i)
        i = i + 1
    return tmp_lst

print(find_even_nums(8))
print('*'*5 + 'End' + '*'*5)


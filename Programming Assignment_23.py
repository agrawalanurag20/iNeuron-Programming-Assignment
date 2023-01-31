# Program 1
#Create a function that takes a number as an argument and returns True or False depending
#on whether the number is symmetrical or not. A number is symmetrical when it is the same as
#its reverse.
def is_symmetrical(n):
    if type(n) == int:
        tmp_str = str(n)
        if tmp_str[0: len(tmp_str)] == tmp_str[-1::-1]:
            return True
        else:
            return False
    else:
        return False

print(is_symmetrical(1112111))
print('*'*5 + 'End' + '*'*5)

# Program 2
#Given a string of numbers separated by a comma and space, return the product of the
#numbers.
def multiply_nums(str1):
    tmp_lst = list(str1.split(', '))
    tmp_product = 1
    for i in tmp_lst:
        try:
            tmp_product = tmp_product * int(i)
        except:
            return "Wrong input"
    return tmp_product

print(multiply_nums("1, 2, 3, 4"))
print('*'*5 + 'End' + '*'*5)

# Program 3
#Create a function that squares every digit of a number.
def square_digits(n):
    if type(n) == int:
        tmp_str = str(n)
        tmp_square = ''
        for i in tmp_str:
            tmp_square = tmp_square + str(int(i)**2)
        return int(tmp_square)
    else:
        return "wrong input"

print(square_digits(2483))
print('*'*5 + 'End' + '*'*5)

# Program 4
#Create a function that sorts a list and removes all duplicate items from it.
def setify(lst1):
    tmp_set = set(sorted(lst1))
    return list(tmp_set)

print(setify([1,3,3,5,5,4,4,4]))
print('*'*5 + 'End' + '*'*5)

# Program 5
#Create a function that returns the mean of all digits.
def mean(n):
   if type(n) == int:
       tmp_str = str(n)
       tmp_sum = 0
       for i in range(0,len(tmp_str)):
           tmp_sum = tmp_sum + int(tmp_str[i])
       tmp_mean = tmp_sum / (i + 1)
       return int(tmp_mean)
   else:
       return "wrong input"

print(mean(512))
print('*'*5 + 'End' + '*'*5)

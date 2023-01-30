# Program 1
#Create a function that takes a list of strings and integers, and filters out the list so that it
#returns a list of integers only.
def filter_list(lst1):
    tmp_lst = list()
    for i in lst1:
        if type(i) == int:
            tmp_lst.append(i)
    return tmp_lst

print(filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]))
print('*'*5 + 'End' + '*'*5)

# Program 2
#Given a list of numbers, create a function which returns the list but with each element&#39;s
#index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the
#number at index 1, etc...
def add_indexes(lst1):
    tmp_lst = list()
    for i in range(0,len(lst1)):
        tmp_lst.append((lst1[i]) + i)
    return tmp_lst

print(add_indexes([5, 4, 3, 2, 1]))
print('*'*5 + 'End' + '*'*5)

# Program 3
#Create a function that takes the height and radius of a cone as arguments and returns the
#volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.
def cone_volume(h,r):
    tmp_vol = 0
    tmp_vol = round(((22/7) * (r**2) * (h/3)),2)
    return tmp_vol

print(cone_volume(3,2))
print('*'*5 + 'End' + '*'*5)

# Program 4
#Write a function that gives the number of dots with its corresponding triangle number of the
#sequence.
def triangle(n):
    i = 1
    tmp_dots = 0
    while i <= n:
        tmp_dots = tmp_dots + i
        i = i + 1
    return tmp_dots

print(triangle(6))
print('*'*5 + 'End' + '*'*5)

# Program 5
#Create a function that takes a list of numbers between 1 and 10 (excluding one number) and
#returns the missing number.
def missing_num(lst1):
    tmp_lst = [1,2,3,4,5,6,7,8,9,10]
    for i in tmp_lst:
        if i not in lst1:
            return i
    return 0

print(missing_num([7,8,4,3,1,9,2,6,5]))
print('*'*5 + 'End' + '*'*5)
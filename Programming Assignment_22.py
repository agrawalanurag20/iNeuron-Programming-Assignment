# Program 1
#Return an ordered list with numbers in the range that are divisible by the third parameter n.
#Return an empty list if there are no numbers that are divisible by n.
def list_operation(x, y, n):
    tmp_lst = list()
    for i in range(x,y+1):
        if i % n == 0:
            tmp_lst.append(i)
    return tmp_lst

print(list_operation(3,12,3))
print('*'*5 + 'End' + '*'*5)

# Program 2
#Create a function that takes in two lists and returns True if the second list follows the first list
#by one element, and False otherwise. In other words, determine if the second list is the first
#list shifted to the right by 1.
def simon_says(lst1, lst2):
    if len(lst1) < 2 or len(lst2) < 2 or len(lst1) != len(lst2):
        return "Wrong input"
    else:
        flag = True
        for i in range(0, len(lst1)-1):
            if lst1[i] == lst2[i+1]:
                pass
            else:
                flag = False
                break
        return flag

print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))
print('*'*5 + 'End' + '*'*5)

# Program 3
#A group of friends have decided to start a secret society. The name will be the first letter of
#each of their names, sorted in alphabetical order.
#Create a function that takes in a list of names and returns the name of the secret society.
def society_name(lst1):
    tmp_name = ''
    tmp_lst = list()
    for i in lst1:
        tmp_lst.append(i[0])
    tmp_lst.sort()
    for i in tmp_lst:
        tmp_name = tmp_name + i
    return tmp_name

print(society_name(["Harry", "Newt", "Luna", "Cho"]))
print('*'*5 + 'End' + '*'*5)

# Program 4
#An isogram is a word that has no duplicate letters. Create a function that takes a string and
#returns either True or False depending on whether or not it's an "isogram".
def is_isogram(str1):
    tmp_set = set(str1.upper())
    if len(str1) == len(tmp_set):
        return True
    else:
        return False

print(is_isogram("Consecutive"))
print('*'*5 + 'End' + '*'*5)

# Program 5
#Create a function that takes a string and returns True or False, depending on whether the
#characters are in order or not.
def is_in_order(str1):
    tmp_str = ''
    tmp_lst = list(str1)
    tmp_lst.sort()
    for i in tmp_lst:
        tmp_str = tmp_str + i
    if tmp_str == str1:
        return True
    else:
        return False

print(is_in_order("edabit"))
print('*'*5 + 'End' + '*'*5)

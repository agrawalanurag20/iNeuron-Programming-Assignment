# Program 1
#Create a function that takes a list of non-negative integers and strings and return a new list
#without the strings.
def filter_list(lst1):
    if type(lst1) == list:
        tmp_lst = list()
        for i in lst1:
            if type(i) == int:
                tmp_lst.append(i)
    return tmp_lst

print(filter_list([1,10,3,"a","b",6,"p",23,"24",890]))
print('*'*5 + 'End' + '*'*5)

# Program 2
#The &quot;Reverser&quot; takes a string as input and returns that string in reverse order, with the
#opposite case.
def reverser(str1):
    str1 = str1[::-1]
    str2 = ""
    for i in range(0,len(str1)):
        if str1[i].islower():
            str2 = str2 + str1[i].upper()
        elif str1[i].isupper():
            str2 = str2 + str1[i].lower()
        else:
            str2 = str2 + str1[i]
    return str2

print(reverser("Hello World"))
print('*'*5 + 'End' + '*'*5)

# Program 3
#Your task is to unpack the list writeyourcodehere into three variables, being first,
#middle, and last, with middle being everything in between the first and last element. Then
#print all three variables.
tst_lst = ['w','r','i','t','e','y','o','u','r','c','o','d','e','h','e','r','e']
first = tst_lst[0]
middle = tst_lst[1:-1]
last = tst_lst[-1]
print(first)
print(middle)
print(last)
print('*'*5 + 'End' + '*'*5)

# Program 4
#Write a function that calculates the factorial of a number recursively.
def facto(n):
    if n <= 1:
        return 1
    else:
        return (n * facto(n - 1))

print(facto(5))
print('*'*5 + 'End' + '*'*5)

# Program 5
#Write a function that moves all elements of one type to the end of the list.
def move_to_end(lst,n):
    tmp_lst = list()
    for i in lst:
        if i == n:
            tmp_lst.append(i)
        else:
            try:
                idx = tmp_lst.index(n)
                tmp_lst.insert(idx, i)
            except:
                tmp_lst.append(i)

    return tmp_lst

print(move_to_end([9,8,1,3,2,1,4,4,1],1))
print('*'*5 + 'End' + '*'*5)
# Program 1
#Create a function that takes three integer arguments (a, b, c) and returns the amount of
#integers which are of equal value.
def equal(n1,n2,n3):
   if n1 == n2 == n3:
       return 3
   elif n1 == n2 or n1 == n3 or n2 == n3:
       return 2
   else:
       return 0

print(equal(3,4,3))
print('*'*5 + 'End' + '*'*5)

# Program 2
#Write a function that converts a dictionary into a list of keys-values tuples.
def dict_to_list(dict1):
    tmp_lst = sorted(list(dict1.keys()))
    tmp_lst1 = list()
    tmp_tup = tuple()
    for i in tmp_lst:
        tmp_tup = i,dict1.get(i)
        tmp_lst1.append(tmp_tup)
    return tmp_lst1

print(dict_to_list({
"likes": 2,
"dislikes": 3,
"followers": 10
}))
print('*'*5 + 'End' + '*'*5)

# Program 3
#Write a function that creates a dictionary with each (key, value) pair being the (lower case,
#upper case) versions of a letter, respectively.
def mapping(lst1):
    tmp_dict = dict()
    tmp_dict1 = dict()
    for i in lst1:
        tmp_dict= {i:i.upper()}
        tmp_dict1.update(tmp_dict)

    return tmp_dict1

print(mapping(["a","v","y","z"]))
print('*'*5 + 'End' + '*'*5)

# Program 4
#Write a function, that replaces all vowels in a string with a specified vowel.
def vow_replace(str1, str2):
    tmp_vow = 'aeiou'
    for i in str1:
        if i in tmp_vow:
             str1 = str1.replace(i,str2)
    return str1

print(vow_replace("stuffed jalapeno poppers", "e"))
print('*'*5 + 'End' + '*'*5)

# Program 5
#Create a function that takes a string as input and capitalizes a letter if its ASCII code is even
#and returns its lower case version if its ASCII code is odd.
def ascii_capitalize(str1):
    tmp_str = ''
    for i in str1:
        if i.isalpha():
            if ord(i) % 2 == 0:
                tmp_str = tmp_str + i.upper()
            else:
                tmp_str = tmp_str + i.lower()
        else:
            tmp_str = tmp_str + i
    return tmp_str

print(ascii_capitalize("THE LITTLE MERMAID"))
print('*'*5 + 'End' + '*'*5)


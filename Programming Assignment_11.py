# Program 1
# To find words which are greater than given length k
print("Program # 1 : To find words which are greater than given length k")
l_words = ["orange", "mango", "apple", "papaya", "watermelon"]
num = int(input("Enter the number to compare: "))
new_word = []
for i in l_words:
    if len(i) > num:
        new_word.append(i)
print(f"Given list {l_words} has words {new_word} greater than length {num}.")
print('*'*5 + 'End' + '*'*5)

# Program 2
# For removing i-th character from a string
print("Program # 2 : For removing i-th character from a string")
s_test = "this is test string to remove i-th character."
num = int(input("Enter the number to remove: "))
s_test = s_test[0:num-1] + s_test[num:len(s_test)-1]
print(f"After removing {num}th char : {s_test}.")
print('*'*5 + 'End' + '*'*5)

# Program 3
# Program to split and join a string?
print("Program # 3 : Program to split and join a string")
s_test = "this-is-test-string-to-split-and-join-a-string"
print(f"Result : {s_test.split('-')}.")
print('*'*5 + 'End' + '*'*5)

# Program 4
# To check if a given string is binary string or not
print("Program # 4 : To check if a given string is binary string or not")
s_test = input("Enter the string :")
b = set(s_test)
s = {'0', '1'}
if b == s or b == {'0'} or b == {'1'}:
    print(f"Entered string {s_test} is binary.")
else:
    print(f"Entered string {s_test} is not binary.")
print('*'*5 + 'End' + '*'*5)

# Program 5
# To find uncommon words from two Strings
print("Program # 5 : To find uncommon words from two Strings")
s_test1 = "this is first string to check uncommon words."
s_test2 = "this is second string to find uncommon words."
b1 = set(s_test1.split())
b2 = set(s_test2.split())
s = b1.symmetric_difference(b2)
print(f"Uncommon words in the given two string are : {s}")
print('*'*5 + 'End' + '*'*5)

# Program 6
# To find all duplicate characters in string
print("Program # 6 : To find all duplicate characters in string")
s_test = "this string is to find all duplicates in string."
d_duplicate = dict()
for i in s_test:
    if s_test.count(i) > 1:
        if i not in d_duplicate.keys():
            d_duplicate[i] = s_test.count(i)
print(f"All duplicate characters in the string are :{d_duplicate}")
print('*'*5 + 'End' + '*'*5)

# Program 7
# To check if a string contains any special character
print("Program # 7 : To check if a string contains any special character")
s_test = input("Enter the string : ")
special_char = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '/')
special_flg = False
for i in s_test:
    if i in special_char:
        special_flg = True
        break
if special_flg == True:
    print("String contains special character.")
else:
    print("String does not contain special character.")
print('*'*5 + 'End' + '*'*5)
# Program 1
# To find sum of elements in list
print("Program # 1 : To find sum of elements in list")
l = [4,7,9,10,45,3,87,45.7,67.2,2]
l_sum = 0
for i in l:
    l_sum = l_sum + i
print(f"Sum of the list is: {l_sum}")
print('*'*5 + 'End' + '*'*5)

# Program 2
# To Multiply all numbers in the list
print("Program # 2 : To Multiply all numbers in the list")
l = [4,7,"abc",9,2.5,"wer"]
l_mul = 1
for i in range(0, len(l)):
    if type(l[i]) == int or type(l[i]) == float:
        l_mul = l_mul * l[i]
print(f"Multiply of all numbers of the list is: {l_mul}")
print('*'*5 + 'End' + '*'*5)

# Program 3
# To find smallest number in a list
print("Program # 3 : To find smallest number in a list")
l = [4,7,"abc",9,2.5,"wer"]
l_small = 0
for i in range(0, len(l)):
    if type(l[i]) == int or type(l[i]) == float:
        if l[i] < l_small or l_small == 0:
            l_small = l[i]
print(f"Smallest number of the list is: {l_small}")
print('*'*5 + 'End' + '*'*5)

# Program 4
# To find largest number in a list
print("Program # 4 : To find largest number in a list")
l = [4,7,"abc",9,2.5,"wer"]
l_large = 0
for i in range(0, len(l)):
    if type(l[i]) == int or type(l[i]) == float:
        if l[i] > l_large:
            l_large = l[i]
print(f"Largest number of the list is: {l_large}")
print('*'*5 + 'End' + '*'*5)

# Program 5
# To find second largest number in a list
print("Program # 5 : To find second largest number in a list")
l = [4,7,8,9,2.5,10,23]
l1 = sorted(l)
print(f"Second Largest number of the list {l} is: {l1[len(l1)-2]}")
print('*'*5 + 'End' + '*'*5)

# Program 6
# To find N largest elements from a list
print("Program # 6 : To find N largest elements from a list")
l = [4,7,8,9,2.5,10,23]
l1 = sorted(l,reverse=True)
large_elem = list()
print(f"Given list is : {l}")
n = int(input("Enter the number to find first n largest element: " ))
for i in range(0,n):
    large_elem.append(l1[i])
print(f"{n} largest elements in the list are : {large_elem}")
print('*'*5 + 'End' + '*'*5)

# Program 7
# To print even numbers in a list
print("Program # 7 : To print even numbers in a list")
l = [4,7,8,9,2.5,10,23]
l_even = list()
for i in l:
    if i % 2 == 0:
        l_even.append(i)
print(f"Even numbers in the given list {l} are : {l_even}")
print('*'*5 + 'End' + '*'*5)

# Program 8
# To print odd numbers in a List
print("Program # 8 : To print odd numbers in a List")
l = [4,7,8,9,2.5,10,23]
l_odd = list()
for i in l:
    if i % 2 != 0:
        l_odd.append(i)
print(f"Odd numbers in the given list {l} are : {l_odd}")
print('*'*5 + 'End' + '*'*5)

# Program 9
# To Remove empty List from List
print("Program # 9 : To Remove empty List from List")
l = [4,[],[6,7],7,8,[],9,[9,5,6],[]]
l_temp = list()
for i in range(0, len(l)):
    if l[i] != []:
        l_temp.append(l[i])
print(f"Given list: {l}, after removing empty list : {l_temp}")
print('*'*5 + 'End' + '*'*5)

# Program 10
# To Cloning or Copying a list
print("Program # 10 : To Cloning or Copying a list")
l = [4,[],[6,7],7,8,[],9,[9,5,6],[]]
l_temp = l
print(f"Existing list : {l}")
print(f"New Cloned list : {l_temp}")
print('*'*5 + 'End' + '*'*5)

# Program 11
# To Count occurrences of an element in a list
print("Program # 11 : To Count occurrences of an element in a list")
l = [4,8,7,4,6,5,4,8,2]
count = l.count(4)
print(f"In the given list : {l}, total occurrences of 4 is : {count}")
print('*'*5 + 'End' + '*'*5)
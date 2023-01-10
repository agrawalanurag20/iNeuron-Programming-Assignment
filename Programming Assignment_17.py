# Program 1
#Create a function that takes three arguments a, b, c and returns the sum of the
#numbers that are evenly divided by c from the range a, b inclusive.
def evenly_divisible(a,b,c):
    sum_evnly_divsble = 0
    for i in range(a,b+1):
        if i % c == 0:
            sum_evnly_divsble = sum_evnly_divsble + i
    return sum_evnly_divsble

print(evenly_divisible(1,10,3))
print('*'*5 + 'End' + '*'*5)

# Program 2
#Create a function that returns True if a given inequality expression is correct and
#False otherwise.
def correct_signs(a):
    flg = False
    b = list()
    b= a.split()
    print(b)
    str_pos = 0
    while str_pos <= (len(b) - 3):
        if b[str_pos + 1] == '<':
            if int(b[str_pos]) < int(b[str_pos + 2]):
                flg = True
            else:
                flg = False
        if b[str_pos + 1] == '>':
            if int(b[str_pos]) > int(b[str_pos + 2]):
                flg = True
            else:
                flg = False
        if flg == False:
            break
        else:
            str_pos = str_pos + 2

    return flg

print(correct_signs("1 < 2 < 6 < 9 > 3"))
print('*'*5 + 'End' + '*'*5)

# Program 3
#Create a function that replaces all the vowels in a string with a specified character.
def replace_vowels(str, exp):
    result_str = ''
    for i in str:
        if i in 'aeiou':
            result_str = result_str + exp
        else:
            result_str = result_str + i
    return result_str

print(replace_vowels("minnie mouse", "?"))
print('*'*5 + 'End' + '*'*5)

# Program 4
#Write a function that calculates the factorial of a number recursively.
def facto(n):
    """This recursive function will find out the factorial of a number"""
    if n <= 1:
        return (n)
    else:
        return (n * facto(n-1))

num = int(input("Enter the number: "))
print(f"Factorial of number {num} is {facto(num)}")
print('*'*5 + 'End' + '*'*5)

# Program 5
#Create a function that computes the hamming distance between two strings.
def hamming_distance(str1, str2):
   diff = 0
   for i in range (0, len(str1)):
       if str1[i] != str2[i]:
           diff = diff + 1
   return diff

print(hamming_distance("abcde","bcdef"))
print('*'*5 + 'End' + '*'*5)
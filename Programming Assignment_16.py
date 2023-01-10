# Program 1
#Write a function that stutters a word as if someone is struggling to read it. The
#first two letters are repeated twice with an ellipsis ... and space after each, and then the
#word is pronounced with a question mark ?.
def stutter_tst(letter_tst):
    result_tst = (letter_tst[0:2] + '... ') * 2 + (letter_tst[0:] + '?')
    return result_tst

word_tst = input("Enter the word: ")
print(stutter_tst(word_tst))
print('*'*5 + 'End' + '*'*5)

# Program 2
#Create a function that takes an angle in radians and returns the corresponding
#angle in degrees rounded to one decimal place.
def radian_to_degree(radian_val):
    degree_val = round(radian_val * (180 / (22/7)),1)
    return degree_val

radian_tst = int(input("Enter the value in Radian: "))
print(f"Corresponding angle in degrees : {radian_to_degree(radian_tst)}")
print('*'*5 + 'End' + '*'*5)

# Program 3
#In this challenge, establish if a given integer num is a Curzon number. If 1 plus
#2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon
#number.
def is_curzon_number(num):
    flg = False
    if ((2**num) + 1) % ((2*num) + 1) == 0:
        flg = True
    return flg

num_tst = int(input("Enter the non negative integer: "))
print(f"Is number {num_tst} Curzon : {is_curzon_number(num_tst)}")
print('*'*5 + 'End' + '*'*5)

# Program 4
#Given the side length x find the area of a hexagon.
import math
def area_of_hexagon(lngth):
    area = round(((3 * math.sqrt(3) * (lngth**2)) / 2),1)
    return area

num_tst = int(input("Enter the side of hexagon: "))
print(f"Area of hexagon is : {area_of_hexagon(num_tst)}")
print('*'*5 + 'End' + '*'*5)

# Program 5
#Create a function that returns a base-2 (binary) representation of a base-10
#(decimal) string number.
def binary_val(num_tst):
    temp = num_tst
    bin_value = ''
    while temp > 0:
        bin_value = str(temp % 2) + bin_value
        temp = temp // 2
    return bin_value
num = int(input("Enter the number: "))
print(f"Binary Value of {num} : {binary_val(num)}")
print('*'*5 + 'End' + '*'*5)




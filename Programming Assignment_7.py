# Program 1
# To find sum of array
print("Program # 1 : To find sum of array")
def sum_arr(arr):
    """This function will find out the sum of the array"""
    sum_res = 0
    for i in arr:
        if type(i) == int or type(i) == float:
            sum_res = sum_res + i
    return sum_res

arr_tst = [1, 3.5, 6, 5, 8, 2.1, 3]
print(f"Sum of given array {arr_tst} is : {sum_arr(arr_tst)}")
print('*'*5 + 'End' + '*'*5)

# Program 2
# To find largest element in an array
print("Program # 2 : To find largest element in an array")
def large_arr(arr):
    """This function will find out the largest element in the array"""
    large_elm = 0
    for i in arr:
        if i > large_elm:
            large_elm = i
    return large_elm

arr_tst = [1, 3.5, 10.5, 5, 8, 2.1, 3]
print(f"Largest element in the given array {arr_tst} is : {large_arr(arr_tst)}")
print('*'*5 + 'End' + '*'*5)

# Program 3
# Program for array rotation
print("Program # 3 : Program for array rotation")
def rot_arr(arr, n):
    """This function will rotate the input array by n position to left"""
    rot_res = arr[n:] + arr[0:n]
    return rot_res

arr_tst = [1, 3.5, 10.5, 5, 8, 2.1, 3]
print(f"Given array is : {arr_tst}")
num = int(input("Enter number of position to rotate left : "))
if num == 0 or num >= len(arr_tst):
    print("Input must be greater than Zero and less than array length.")
else:
    print(f"After {num} position left rotate : {rot_arr(arr_tst, num)}")
print('*'*5 + 'End' + '*'*5)

# Program 4
# Split the array and add the first part to the end
print("Program # 4 : Split the array and add the first part to the end")
def splt_arr(arr, n):
    """This function will split the array from given position and add to the end"""
    splt_res = arr[n:] + arr[0:n]
    return splt_res

arr_tst = [1, 3.5, 10.5, 5, 8, 2.1, 3]
print(f"Given array is : {arr_tst}")
num = int(input("Enter number of position to split : "))
if num == 0 or num >= len(arr_tst):
    print("Input must be greater than Zero and less than array length.")
else:
    print(f"After splitting from position {num} and adding to the end: {splt_arr(arr_tst, num)}")
print('*'*5 + 'End' + '*'*5)

# Program 5
# To check if given array is Monotonic
print("Program # 5 : To check if given array is Monotonic")
def mono_arr(arr):
    """This function will check if given array is monotonic"""
    n = len(arr)
    if n == 1:
        return True
    else:
        if all(arr[i] >= arr[i+1] for i in range(0, n-1)) \
                or all(arr[i] <= arr[i+1] for i in range(0, n-1)):
            return True
        else:
            return False

arr_tst = [6, 5, 5, 4, 2, 2, 1]
print(f"Given array is : {arr_tst}")
print(f"Given array {arr_tst} is monotonic : {mono_arr(arr_tst)}")
print('*'*5 + 'End' + '*'*5)
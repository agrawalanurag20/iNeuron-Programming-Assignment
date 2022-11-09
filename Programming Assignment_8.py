# Program 1
# To Add Two Matrices
print("Program # 1 : To Add Two Matrices")
def validate_matrice(l1):
    """This function will validate and return dimension of matrix."""
    len1 = len(l1)
    for i in range(0, len1):
        if i == 0:
            len2 = len(l1[i])
        else:
            if len2 == len(l1[i]):
                continue
            else:
                print("Invalid Matrix.")
                return [0,0]
    return [len1, len2]

def add_matrices(l1,l2):
    """This function will add two Matrices."""
    new_list = list()
    lenth1 = validate_matrice(l1)
    lenth2 = validate_matrice(l2)
    if lenth1 != [0,0] and lenth2 != [0,0]:
        if lenth1 == lenth2:
            for i in range(0, lenth1[0]):
                tmp_list = list()
                for j in range(0,lenth1[1]):
                    tmp_list.append(l1[i][j] + l2[i][j])
                new_list.append(tmp_list)
            print(f"Sum of given Matrices {l1} and {l2} is : {new_list}")
        else:
            print("Matrices are not identical, cannot add.")

mat1 = [[7,5,4],[9,0,3],[4,3,4]]
mat2 = [[1,5,7],[6,9,2],[2,4,3]]
add_matrices(mat1, mat2)
print('*'*5 + 'End' + '*'*5)

# Program 2
# To multiply Two Matrices
print("Program # 2 : To multiply Two Matrices")
def validate_matrice(l1):
    """This function will validate and return dimension of matrix."""
    len1 = len(l1)
    for i in range(0, len1):
        if i == 0:
            len2 = len(l1[i])
        else:
            if len2 == len(l1[i]):
                continue
            else:
                print("Invalid Matrix.")
                return [0,0]
    return [len1, len2]

def mul_matrices(l1,l2):
    """This function will multiply two Matrices."""
    new_list = list()
    lenth1 = validate_matrice(l1)
    lenth2 = validate_matrice(l2)
    if lenth1 != [0,0] and lenth2 != [0,0]:
        if lenth1[1] == lenth2[0]:
            for i in range(0, lenth1[0]):
                tmp_list = list()
                for j in range(0, lenth1[1]):
                    tmp_var = 0
                    for k in range(0,lenth2[1]):
                        tmp_var = (l1[i][j] * l2[j][k])
                        if j == 0:
                            tmp_list.append(tmp_var)
                        else:
                            tmp_list[k] = tmp_list[k] + tmp_var
                new_list.append(tmp_list)
            print(f"Multiplication of given Matrices {l1} and {l2} is : {new_list}")
        else:
            print("Columns in Matrix 1 not equal to Rows in Matrix 2, cannot multiply.")

mat1 = [[7,5,4],[9,0,3],[4,3,4]]
mat2 = [[1,5],[6,9],[3,4]]
mul_matrices(mat1, mat2)
print('*'*5 + 'End' + '*'*5)

# Program 3
# To Transpose a Matrix
print("Program # 3 : To Transpose a Matrix")
def validate_matrice(l1):
    """This function will validate and return dimension of matrix."""
    len1 = len(l1)
    for i in range(0, len1):
        if i == 0:
            len2 = len(l1[i])
        else:
            if len2 == len(l1[i]):
                continue
            else:
                print("Invalid Matrix.")
                return [0,0]
    return [len1, len2]

def trans_matrix(l1):
    """This function will transpose the input Matrix."""
    new_list = list()
    lenth1 = validate_matrice(l1)
    if lenth1 != [0,0]:
       for i in range(0, lenth1[1]):
           tmp_list = list()
           for j in range(0, lenth1[0]):
               tmp_list.append(l1[j][i])
           new_list.append(tmp_list)
       print(f"Transpose of given Matrix {l1} is : {new_list}.")
mat1 = [[7,5,4],[9,0,3],[4,3,4]]
mat2 = [[1,5],[6,9],[3,4]]
mat3 = [[7,5,4,3],[9,0,3,2],[4,3,4,1]]
mat4 = [[1],[6],[3]]
trans_matrix(mat1)
trans_matrix(mat2)
trans_matrix(mat3)
trans_matrix(mat4)
print('*'*5 + 'End' + '*'*5)

# Program 4
# To Sort Words in Alphabetic Order
print("Program # 4 : To Sort Words in Alphabetic Order")
word_list =['pen','book','water','pencil','table','room','basket']
sort_list = sorted(word_list)
print(f"Input list {word_list}, after sorting : {sort_list}")
word_list.sort()
print(f"After in place sorting : {word_list}")
print('*'*5 + 'End' + '*'*5)

# Program 5
# To Remove Punctuation From a String
print("Program # 5 : To to Remove Punctuation From a String")
import string
str_example = "This, exa[mp]le is to ?remove all p(unctuation."
res_string = str_example.translate(str.maketrans('','',string.punctuation))
print(f"Input string : {str_example} - After removing punctuation : {res_string}")
print('*'*5 + 'End' + '*'*5)





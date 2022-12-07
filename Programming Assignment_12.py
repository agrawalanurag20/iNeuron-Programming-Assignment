# Program 1
# To Extract Unique values dictionary values
print("Program # 1 : To Extract Unique values dictionary values")
dict_test = {"key1":"apple", "key2":"mango", "key3":"apple", "key4":123, "key5":789, "key6":123}
print(f"Unique dictionary values are :{set(dict_test.values())}")
print('*'*5 + 'End' + '*'*5)

# Program 2
# To find the sum of all items in a dictionary
print("Program # 2 : to find the sum of all items in a dictionary")
dict_test = {"key1":"apple", "key2":23, "key3":"apple", "key4":123.23, "key5":789, "key6":123}
sum_test = 0
for i in set(dict_test.values()):
    if type(i) == int or type(i) == float:
        sum_test = sum_test + i
print(f"Sum of all items in dictionary : {sum_test}")
print('*'*5 + 'End' + '*'*5)

# Program 3
# To Merging two Dictionaries?
print("Program # 3 : To Merging two Dictionaries")
dict_test1 = {"key1":"apple", "key2":23, "key3":"apple", "key4":123.23, "key5":789, "key6":123}
dict_test2 = {"idx1":"bang", "idx2":"mum", "idx3":456, "idx4":"hyd", "idx5":12}
dict_test1.update(dict_test2)
print(f"Sum of all items in dictionary : {dict_test1}")
print('*'*5 + 'End' + '*'*5)

# Program 4
# To convert key-values list to flat dictionary
print("Program # 4 : to convert key-values list to flat dictionary")
from itertools import product
dict_test1 = {"day_num":[1,2,3,4,5,6,7], "week_day":['mon','tue','wed','thu','fri','sat','sun']}
dict_test2 = dict(zip(dict_test1["day_num"], dict_test1["week_day"]))
print(f"Converted Flat dictionary : {dict_test2}")
print('*'*5 + 'End' + '*'*5)

# Program 5
# To insertion at the beginning in OrderedDict
print("Program # 5 : To insertion at the beginning in OrderedDict")
from collections import OrderedDict
test_dict = OrderedDict([('1', 'val1'), ('2', 'val2'), ('3', 'val3')])
print(f"The dictionary is : {test_dict}")
test_dict.update({'4':'val4'})
test_dict.move_to_end('4', last = False)
print(f"The dictionary after inserting at beginning is : {test_dict}")
print('*'*5 + 'End' + '*'*5)

# Program 6
# to check order of character in string using OrderedDict()
print("Program # 6 : To check order of character in string using OrderedDict()")
from collections import OrderedDict
def check_order(tst_input, tst_pattern):
   tst_dict = OrderedDict.fromkeys(tst_input)
   print(tst_dict)
   pattern_length = 0
   for key,value in tst_dict.items():
      if (key == tst_pattern[pattern_length]):
         pattern_length = pattern_length + 1
      if (pattern_length == (len(tst_pattern))):
         return 'The order of pattern is correct'
   return 'The order of pattern is incorrect'

tst_input = 'To check order'
tst_pattern = 'ch'
print(check_order(tst_input,tst_pattern))
print('*'*5 + 'End' + '*'*5)

# Program 7
# to sort Python Dictionaries by Key or Value
print("Program # 7 : to sort Python Dictionaries by Key or Value")
from itertools import product
tst_dict = {"2":"b", "7":"g", "1":"a", "9":"i", "4":"d", "5":"e"}
sorted_dict = dict(zip(sorted(list(tst_dict.keys())),sorted(list(tst_dict.values()))))
print(f"Sorted dictionary by key is : {sorted_dict}")
print('*'*5 + 'End' + '*'*5)

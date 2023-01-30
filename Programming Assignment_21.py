# Program 1
#Write a function that takes a list and a number as arguments. Add the number to the end of
#the list, then remove the first element of the list. The function should then return the updated
#list.
def next_in_line(lst1, n):
    if len(lst1) > 0:
        lst1.append(n)
        lst1.pop(0)
        return lst1
    else:
        return "No list has been selected"

print(next_in_line([7, 6, 3, 23, 17], 10))
print('*'*5 + 'End' + '*'*5)

# Program 2
#Create the function that takes a list of dictionaries and returns the sum of people's budgets.
def get_budgets(lst1):
    tmp_budget = 0
    for i in range(0, len(lst1)):
        try:
            tmp_budget = tmp_budget + lst1[i].get("budget")
        except:
            tmp_budget = tmp_budget
    return tmp_budget

print(get_budgets([
{ "name": "John", "age": 21, "budget": 23000 },
{ "name": "Steve", "age": 32, "budget": 40000 },
{ "name": "Martin", "age": 16, "budget": 2700 },
{ "name": "Martina", "age": 26},
{ "name": "Martini", "age": 36, "budget": 3700 }
]))
print('*'*5 + 'End' + '*'*5)

# Program 3
#Create a function that takes a string and returns a string with its letters in alphabetical order.
def alphabet_soup(str1):
    tmp_str = ''
    tmp_lst = sorted(list(str1))
    for i in tmp_lst:
        tmp_str = tmp_str + i
    return tmp_str

print(alphabet_soup("javascript"))
print('*'*5 + 'End' + '*'*5)

# Program 4
#Create a function that accepts the principal p, the term in years t, the interest rate r, and the
#number of compounding periods per year n. The function returns the value at the end of term
#rounded to the nearest cent.
def compound_interest(p, t, r, n):
    tmp_val = 0
    i = 1
    while i <= t:
        j = 1
        while j <= n:
            tmp_val = p + ((p*r)/n)
            p = tmp_val
            j = j + 1
        i = i + 1
    return round(tmp_val,2)

print(compound_interest(100000, 20, 0.15, 365))
print('*'*5 + 'End' + '*'*5)

# Program 5
#Write a function that takes a list of elements and returns only the integers.
def return_only_integer(lst1):
    tmp_lst = list()
    for i in lst1:
        if type(i) == int:
            tmp_lst.append(i)
    return tmp_lst

print(return_only_integer(["String", True, 3.3, 1]))
print('*'*5 + 'End' + '*'*5)




# Program 1
#Create a function that takes an integer and returns a list from 1 to the given number, where:
#1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the
#number).
#2. If the number cannot be divided evenly by 4, simply return the number.
def amplify(n):
   if n >= 1:
       i = 1
       tmp_lst = list()
       while i <= n:
           if i % 4 == 0:
               tmp_lst.append(i*10)
           else:
               tmp_lst.append(i)
           i = i + 1
       return tmp_lst
   else:
       return "wrong input"

print(amplify(25))
print('*'*5 + 'End' + '*'*5)

# Program 2
#Create a function that takes a list of numbers and return the number that's unique.
def unique(lst1):
   for i in lst1:
       counter = lst1.count(i)
       if counter == 1:
           return i
   return "No unique number found"

print(unique([0, 0, 0.77, 0, 0]))
print('*'*5 + 'End' + '*'*5)

# Program 3
#Your task is to create a Circle constructor that creates a circle with a radius provided by an
#argument. The circles constructed must have two getters getArea() (PIr^2) and
#getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def getArea(self):
        return ((22/7)*(self.radius**2))
    def getPerimeter(self):
        return (2 * (22/7) * self.radius)

circy = Circle(11)
print(circy.getArea())
print(circy.getPerimeter())
circy2 = Circle(4.44)
print(circy2.getArea())
print(circy2.getPerimeter())
print('*'*5 + 'End' + '*'*5)

# Program 4
#Create a function that takes a list of strings and return a list, sorted from shortest to longest.
def sort_by_length(lst1):
    tmp_lst = list()
    for i in range(0, len(lst1)):
        if i == 0:
            tmp_lst.append(lst1[i])
        else:
            pos = 0
            for j in range(0, len(tmp_lst)):
                if len(lst1[i]) > len(tmp_lst[j]):
                    pos = j + 1
                else:
                    pos = j
                    break
            tmp_lst.insert(pos, lst1[i])
    return tmp_lst

print(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))
print('*'*5 + 'End' + '*'*5)

# Program 5
#Create a function that validates whether three given integers form a Pythagorean triplet. The
#sum of the squares of the two smallest integers must equal the square of the largest number to
#be validated.
def is_triplet(n1, n2, n3):
    tmp_tup = n1,n2,n3
    tmp_lst = sorted(list(tmp_tup))
    if ((tmp_lst[0]**2) + (tmp_lst[1]**2)) == (tmp_lst[2]**2):
        return True
    else:
        return False

print(is_triplet(13, 5, 12))
print('*'*5 + 'End' + '*'*5)

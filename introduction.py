'''
Created on Nov 29, 2016

@author: Gloria
'''
boolean = True
number = 1.1
string = "String can be declared with single or double quotes"
list = ["List can have", 1,2,3,4, "or more types together !"]
tuple = ("Tuple", "can have", 2, "elements !")
dictionary = {'one': 1, 'two': 2, 'three':3}
variable_with_zero_data = None
print "Printed !"
cake = "delicious"

#if 
def if_cake(cake_in):
    if cake == "delicious":
        return "Yes please !"
    elif cake == "okay":
        return "I'll have a small piece."
    else :
        return "No, thank you."
print if_cake(cake)

#loop 
for item in list:
    print "item :",item
total = 0
max_val =  10  
values = []
for i in xrange(20):
     values.append(i)
print "values:",values

i = 0
while (total < max_val):
    total += values[i]
    i += 2
    print "i",i, "values[",i,"] : ",values[i]
print "total :",total

print"\ndivide : "    
def divide(dividend, divisor):
    quotient = dividend / divisor
    remainder = dividend % divisor
    return quotient, remainder
print divide(568,23)

def calculate_stuff(x, y):
    (q, r) = divide(x,y)
    print q, r
calculate_stuff(568, 44)

#Classes
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def birthday(self):
        self.age += 1
        
person = Person("Yoonsu",29)
print person
print "age is ",person.age
print "name is ",person.name
person.birthday()
print "incrased age is ",person.age


test_dict = dict()
test_dict["this"]= 8
test_dict["that"]=9
print test_dict
print "*"*50
"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""
class Classy(object):
    def __init__(self):
        self.items = []
        self.total = 0
#         self.items_dict={}
    def addItem(self, str_input): 
        self.items.append(str_input)
    def getClassiness(self, total = 0):
        self.total = total
        for item in self.items:
            if item =="tophat":
                self.total += 2
#                 total += 2
            elif item == "bowtie":
                self.total += 4
#                 total += 4
            elif item == "monocle":
                self.total += 5
#                 total += 5
        return self.total    
# Test creases
me = Classy()

# Should be 0
print me.getClassiness()

me.addItem("tophat")
# Should be 2
print me.getClassiness()

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print me.getClassiness()

me.addItem("bowtie")
# Should be 15
print me.getClassiness()

print "solutio from Udacity","-"*20
print "Here's the solution:"

class Classy2(object):
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def getClassiness(self):
        classiness = 0
        if len(self.items) > 0:  #udacity added 
            for item in self.items:
                if item == "tophat":
                    classiness += 2
                elif item == "bowtie":
                    classiness += 4
                elif item == "monocle":
                    classiness += 5
        return classiness
# Test creases
me = Classy2()

# Should be 0
print me.getClassiness()

me.addItem("tophat")
# Should be 2
print me.getClassiness()

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print me.getClassiness()

me.addItem("bowtie")
# Should be 15
print me.getClassiness()

#Approximation : some number of computations must be performed for EACH letter in the input.
#Worst case : 

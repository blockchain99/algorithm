'''
Created on Nov 30, 2016

@author: Gloria
'''
# Below are some examples of functions in Python. Look at each and take note of the time efficiency. 
# Then, in the quiz, enter those values using the correct notation. Use approximations wherever possible!

"""input manatees: a list of "manatees", where one manatee is represented by a dictionary
a single manatee has properties like "name", "age", et cetera
n = the number of elements in "manatees"
m = the number of properties per "manatee" (i.e. the number of keys in a manatee dictionary)"""
# manatees_dict = dict()
man1 = {'name':"ys",'age':29,'sex':'male','height':5.9,'weight':120}
man2 = {'name':"ka",'age':25,'sex':'female','height':5.3,'weight':122}
man3 = {'name':"sg",'age':23,'sex':'female','height':5.5,'weight':130}
man4 = {'name':"bk",'age':20,'sex':'male','height':5.7,'weight':150}
manatees_list = [man1, man2, man3, man4]
print "the number of elements in list, manatees(n) :",len(manatees_list)
print "the number of elements(properties) in dictionary, man1(m) :",len(man1)
# We iterate over every manatee in the manatees list with the for loop. 
# Since we're given that manatees has n elements, our code will take approximately O(n) time to run.
def example1(manatees):
    for manatee in manatees:  #
        print manatee['name'] #
print "* example1(manatees_dict): " #
example1(manatees_list)

# We look at two specific properties of a specific manatee. We aren't iterating over anything
#  - just doing constant-time lookups on lists and dictionaries. Thus the code will complete in constant, or O(1), time.
def example2(manatees):
    print manatees[0]['name'] 
    print manatees[0]['age']  
print "* example2(manatees_dict): " 
example2(manatees_list)

# There are two for loops, and nested for loops are a good sign 
# that you need to multiply two runtimes. 
# Here, for every manatee, we check every property. If we had 4 manatees,
# each with 5 properties, then we would need 5+5+5+5 steps. 
#This logic simplifies to the number of manatees times the number of properties, or O(nm).
def example3(manatees):
    for manatee in manatees: #4
        for manatee_property in manatee: #5  -> 4*5 = 20 
            print manatee_property, ": ", manatee[manatee_property] 
print "* example3(manatees_dict): " #1 
example3(manatees_list)

# Again we have nested for loops. This time we're iterating over the manatees list twice
#  - every time we see a manatee, we compare it to every other manatee's age. 
#  We end up with O(nn), or O(n^2) (which is read as "n squared").
def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print oldest_manatee
print "* example4(manatees_dict): "
example4(manatees_list)    
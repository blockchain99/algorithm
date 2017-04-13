'''
Created on Dec 5, 2016

@author: ys
'''
numrows = [1,2,3,4,5]

def print_tes(numrows1):
 for i in range(len(numrows1)):
        if numrows1[i] == 3:   
            return "I found :",i  #at return point,  no  more for loop execute.
        print"i:\n", i
print "result is \n",print_tes(numrows)
print "*"*59

T=[[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]]
print T[0][1]
print"-"*50  
n=1
for i  in xrange(len(T)):
    print T[i][n]
print"-"*50    
n=4
for i  in xrange(len(T)):
    print T[i][n]
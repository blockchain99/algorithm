# -*- coding: utf-8 -*-
import sys
print sys.getdefaultencoding()

''' Bubble sort : naive appraoch : n elements : n-1 iteration * n-1 comparison : (n-1)*(n-1) = n^2 -2n -1 => O(n^2)'''
''' bianry search 25 in following array.
odd number array (7) : choose middle
( 1   3   9   11   15   19   29)  
              1?
            25>11  go to right of 11 
                 ( 15   19   29)
                        2?
                       25>19  go to right of 19
                           (19   29) side by side,but no 25 there, conclude 25 not exit in array
                               3?
                             25<29
******************************************** Iteration : 3
- search 10

             1?                      even number array(8): choose lower side.
[1   2   3   4   5    6    7    8]    
            10>4 
                      2?
                 5    6    7    8]   
                    10>6         
                           3?
                           7    8]
                          10>7 
                                4?
                                8]
                               10>8  : 10 not exit
******************************************* Iteration : 4    
worst case scenario : pick number bigger than any other element in array just like above.
 1?
[16]
30>16, let's take 30 to compare 1 element array 
****************************************** Iteration : 1
 1?
[18   21]
23>18
      2?
      21]
     23>21 , 23 not exit !
***************************************** Iteration : 2     

                 2^0 2^1     2^2             2^3
array_size :  0   1   2   3   4   5   6   7   8  
Iterations :  0   1   2   2   3   3   3   3   4
                 0+1 1+1                     3+1
               log2(1)+1, log2(2)+1     log2(8)+1  
O(1/2 * n) ?                 
So  Iteration is (power of 2) +1  : O([power of 2 exponent] +1)
                                    O(log2(n) +1)  => O(log(n))
                           
'''
"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

#calculate by index not by element value.
def binary_search(input_array, value):  #assume input_array size 8 => index 0,1,2,3,4,5,6,7  <7 is len(input_array)-1 = 8-1=7>
    low = 0   #index for first element 
    high = len(input_array)-1   #index for last element ,7
    while(low <= high):
        mid = (low + high)/2    #middle index of array (0+7)/2 = 3.5  => 3
        if(input_array[mid]== value):
            return mid
        elif(input_array[mid]<value):
            low = mid +1
        else:
            high = mid -1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print 'array {}, value {}, result {}'.format(test_list , test_val1 ,(binary_search(test_list, test_val1)))
# print 'array %s, value %s, result %s' %(test_list , test_val1 ,(binary_search(test_list, test_val1)))
#print "array {0}, value {1}, result{2}".format(test_list , test_val2 ,(binary_search(test_list, test_val2))
print 'array %s, value %d, result %d' %(test_list , test_val2 ,(binary_search(test_list, test_val2)))
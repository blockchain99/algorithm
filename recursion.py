# -*- coding: utf-8 -*-
import sys
from jedi.evaluate.recursion import recursion_decorator
print sys.getdefaultencoding()

''' recursion: pseudo code
function recursive(input):
### base case ### (2) base case : tell when to stop
  if input <= 0
      return input
##################      
  else 
      output = recursive(input - 1)  #(1) while(exit condition): ; code ; code ; code ; code
      return output
      
      
## infinite recursion ##  
function recursive(input):
### base case ### (2) base case : tell when to stop
  if input == 0
      return input
##################      
  else 
      output = recursive(input - 1)  #(1) while(exit condition): ; code ; code ; code ; code
      return output      
 Fibonacci : recursion , example of the sequence:
0,1,1,2,3,5,8,13,21,34...
Step through each value. You start with 0 and 1. 0 + 1 = 1, 
so you add 1 to the sequence. 1 + 1 = 2, so 2 is added. 1 + 2 = 3, so 3. 2 + 3 = 5, et cetera.
'''
########## pseudo code ########
# function getFib(position) {
#   if (position == 0) { return 0; }
#   if (position == 1) { return 1; }
#   var first = 0,
#       second = 1,
#       next = first + second;
#   for (var i = 2; i < position; i++) {
#     first = second;
#     second = next;
#     next = first + second;
#   }
#   return next;
# }
# fib_seq = []
# fib_seq[0] = 0
# fib_seq[1] = 1
# fib_seq[2] = 1
# fib_seq[3] = 2
# fib_seq[4] = 3
# fib_seq[5] = 5
# fib_seq[6] = 8
# fib_seq[7] = 13
# fib_seq[8] = 21
# fib_seq[9] = 34 
   
def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)   
print get_fib(1)   
print get_fib(5)
print get_fib(6)
print get_fib(8)

for i in xrange(10):  #from 0 to 9
    print get_fib(i),
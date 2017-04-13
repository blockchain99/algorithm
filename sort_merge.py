# -*- coding: utf-8 -*-
import sys
print sys.getdefaultencoding()
''' Merge sort efficiency : O(n * log(n)) : n-comparison per step , log(n)-step
    much better than bubble sort O(n*n)=O(n^2), space efficiency is worse than bubble sort,which just sort
    in place,so no need extra array), Merge sort use Auxillary space = O(n) linear(copy the value in an array)'''
    
''' Merge sort : devide and conquor : n elements : n-1 iteration * n-1 comparison : (n-1)*(n-1) = n^2 -2n -1 => O(n^2)
 (  -   -   -   -)- original array
   |    |   |   |    1st : breakup to new array 
  (-)  (-) (-) (-)- new array
                     2nd  back up
-----------------------------------------------
(  8   3    1   7   0   10   2  )
                                  breakup to bunch of array, one element of each
  (8) (3)  (1) (7) (0) (10) (2)                               
         3>1     7>0     10>2     
****************************************  comparison : 3 ( 1 1 1)       
  (-)  (- - )  ( - -)  (-  -)    prepare one element array at head and the rests are two element array                   
  (8)  (1  3)  (0  7)  (2  10)    backup : Notice that (1 3) (0 7) (2 10) already sorted !! 
  (  -  -  -)  (-  -   -   -)    prepare 3 element array, 4 element array
    8 > 1  comparison :1  then    
  (8)  (-  3)   delete 1 then place 1 to first place
   (1  -   -)  (-  -   -   -) 
    8   >  3 comparison :1  then
  (8)  (-  -)   delete 3 then place 3 to 2nd place  
   (1   3  - ) -> automatic fill the rest 8 , so (1  3  8) 
   ( 1  3  8 ) (0   7 ) ( 2   10)    
                0  <  2, compare first element of tow array,   
               (-   7)  (2  10)  delete 0, 0 in 1st place                     
                (0  -   -   -)
                    7  > 2          compare 7 with two element in (2 10) array
               (-   7)  (-  10)     delete 2 then place 2 in 2nd place
               (0   2   -   - ) 
                    7    <  10    compare 7 with 10 
               (-   -)  (-  -)   
               (0    2   7  10)  
  ( 1   3   8) (0    2   7  10)      
  *************************************comparison : 5 ( 2 )( 3 ) 
  1 > 0 : delete 0, 0 go to 1st place
  ( 1   3   8) (-    2   7  10) 
  (0 - - - - - -)
   1              < 2  : delete 1, 1 go to 2nd place
   ( -   3   8) (-    2   7  10)
  (0 1 - - - - -)
         3        >   2 : delete 2 , 2 go to 3rd place
   ( -   3   8) (-    -   7  10)      
   (0 1 2 - - - -)       
         3          <     7  : delete 3 , 3 go to 4th place   
   ( -   -   8) (-    -   7  10)      
   (0 1 2 3 - - -)     
             8      >     7  : delete 7 , 7 go to 5th place
   ( -   -   8) (-    -   -  10)      
   (0 1 2 3 7 - -)       
             8          <    10 : delete 8 , 8 to to 6th, 10 go to 7th place
   ( -   -   8) (-    -   -  10)      
   (0 1 2 3 7 8 10)             
   *************************************comparison : 6 (6)  '''
                       
         
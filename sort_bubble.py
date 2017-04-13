# -*- coding: utf-8 -*-
import sys
print sys.getdefaultencoding()

''' Bubble sort : naive appraoch : n elements : n-1 iteration * n-1 comparison : (n-1)*(n-1) = n^2 -2n -1 => O(n^2)'''
''' sorting 5 elements :  8  /  3 /  1  /  7  /  0   
     1st iteration         8>3(swap)                  comparison |||| (4)= (5-1)out of (5)element
                          3  /  8 /  1  /  7  /  0    
                                 8>1(swap)      
                          3  /  1 /  8  /  7  /  0 
                                       8>7(swap)   
                          3  /  1 /  7  /  8  /  0  
                                            8>0(swap)
                          3  /  1 /  7  /  0  /  (8) 
    ****************************************************************************************                        
     2nd iteration        3  /  1 /  7  /  0  /  8     
                            3>1(swap)                 comparison |||| (4)out of (5)element
                          1  /  3 /  7  /  0  /  8     
                                 3>7(no swap)         
                          1  /  3 /  7  /  0  /  8     
                                       7>0(swap)   
                          1  /  3 /  0  /  7  /  8     
                                             7>8(no swap)     
                          1  /  3 /  0  /  (7  /  8)    
    ***************************************************************************************       
    3rd iteration                                     comparison |||| (4)out of (5)element
                                    ( 3  /  7  /  8 )
    ***************************************************************************************       
    4th iteration(5-1)                                comparison |||| (4)out of (5)element
                         0    (1  /  3   /  7  /  8)      
    *************************************************************************************** '''      
 
              
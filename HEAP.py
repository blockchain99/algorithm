# -*- coding: utf-8 -*-
import sys
print sys.getdefaultencoding()
''' HEAPs : special type of tree, elements are increasing order or decreasing order.so root is max(max heap) or min value.
   : don't need to be binary tree, child can be more than 2.
1) max heap      
                           7
                        /    \   
                       5      3
                    /    |
                   2      1
- Search advantage : quit search immediately if search for element bigger than root. such as 8, which is bigger than 7
-In general, If searching element less than root, such as 6 
 :If node value is bigger than one we are comparing to,  no need to check in sub tree, since we know it is the biggest. 
 (6 > 5, so sub tree of 5, which are 2, 1: no need to check )
2) min heap'''


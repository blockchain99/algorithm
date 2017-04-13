'''
Binary search trees can become unbalanced, actually quite often.
 When a tree is unbalanced the complexity of insert, delete, 
 and lookup operations can get as bad as \O(n)
 
 AVL trees maintain their own balance. The balance can be maintained 
 in one of two ways. Either the height of each node in the tree can 
 be maintained or the balance of each node in the tree can be maintained.
  If maintaining the height, there is a little more work to be done 
  to adjust heights all the way up the tree. If balance is maintained 
  then the code gets a little trickier, 
  but there balances only need to be adjusted up to a pivot node.

In addition, AVL trees can be implemented with recursive or 
iterative insert and delete methods.
'''

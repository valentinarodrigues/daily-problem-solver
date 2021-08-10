Heap Min Max

Priority queue
Heap sort
kth largest/smallest number in a list


## Array representation of binary tree
Left child: 2 * parent's idx 
Right child: 2 * parent's idx + 1
Parent : child's idx/2

        A
      /   \
    B      C
  /  \    /  \
 D   E   F    G

_____________
A B C D E F G
_____________
1 2 3 4 5 6 7



## Full Binary Tree
h - height
                    h+1
Number of nodes - 2    -1 

Examples:
               18               
           /       \  
         15         30  
        /  \        /  \
      40    50    100   40


             18
           /    \   
         15     20    
        /  \       
      40    50   
    /   \
   30   50


               18
            /     \  
          40       30  
                   /  \
                 100   40


## Complete binary tree
Height = min as possible
log(N)
N => number of nodes

A Binary Tree is a Complete Binary Tree if all the levels are completely filled except possibly the last level and the last level has all keys as left as possible 

               18
           /       \  
         15         30  
        /  \        /  \
      40    50    100   40


               18
           /       \  
         15         30  
        /  \        /  \
      40    50    100   40
     /  \   /
    8   7  9 

Insertion: O(log(n)) (Height of the tree) (Elements are inserted at the leave)
Deletion: O(log(n))  (Elements are deleted at the root) (For deleting 1 element)
Creation of a heap: since we insert each element  - nlog(n)
Complete deletion: nlog(n) (Deleting all elements in a heap sort)
Heap sort: Perform deletion and every element deleted will be stored at the free space at the end of the array
Sort: Creation nlog(n) + Deletion nlog(n)
2nlog(n) ~ nlog(n)

Heapify=> 


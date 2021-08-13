Go through an array and print out all of the elements
Determine whether or not a string is a palindrome
Calculate a raised to the power of b
Extra credit: Try implementing the map function (the one that transforms arrays) without using loops

Try Recursion


## Indexing Mistakes
Take care of scenarios of when you increment the index of an array 
Example:
This is what you may want: idx is first incremented and then the value of left and right is computed
    idx+=1
    left = word[idx:]
    right = word[:idx]

This is what you may end up doing: :x:
    left = word[idx:]
    right = word[:idx] 
    idx+=1


Take care of indentation make sure you are returning from the function at the right place
TO REPEAT:
1110. Delete Nodes And Return Forest
951. Flip Equivalent Binary Trees

See for solution like destroying the array in question itself

MATH 101
Ceil of 2 numbers

12
-- = 7.2 => Ceil should be 8 => Ceil(p/k) => ((p-1)//k)+1
7

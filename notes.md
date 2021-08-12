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



Practice Raising Errors
```python
raise ValueError('Value not found in the list')
```

```python
from collections import Counter
list = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(list)
print(cnt[1])
# OUTPUT: 3
```

```python
from collections import defaultdict
# default will be 0
nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
print(nums['three'])
# OUTPUT: 0
```

```python
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)
```

```python
# Python program to demonstrate
# sorted()
  
  
L = ['aaaa', 'bbb', 'cc', 'd']
  
# sorted without key parameter
print(sorted(L))
print()
  
# sorted with key parameter
print(sorted(L, key = len))
```

sort() is a method of list class and can only be used with lists.
Time complexity is nlog(n)
Timsort algorithm

For Max heap => multiply each value by -1 so that we can use it as MaxHeap.


```python
# Reverse iteration
# range(start, stop, step)
# start index is included (from)
# stop index is not included (till)
# step is the difference => for reverse make it -1
for i in range(len(s)-1, -1, -1):
    print(i)
```

```python
# Python code to demonstrate working of 
# nlargest() and nsmallest()
  
# importing "heapq" to implement heap queue
import heapq
  
# initializing list 
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
  
# using heapify() to convert list into heap
heapq.heapify(li1)
  
# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print("The 3 largest numbers in list are : ",end="")
print(heapq.nlargest(3, li1))
  
# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ",end="")
print(heapq.nsmallest(3, li1))
```

[::-1] => reverse a string
k=3
length = 10
cardPoints[0:k] => 0 to 3(excluding) => 0 , 1 , 2
cardPoints[-1:-k-1:-1] => 10, 9, 8 => -1, -2 , -3 (-1 to -4(excluding))

# Initializing an array
```python
x = [0] * n  # n is length of the array
```
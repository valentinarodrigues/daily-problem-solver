#Given an array of integers greater than zero, find if it is possible to split it in two subarrays (without reordering the elements), such that the sum of the two subarrays is the same. Print the two subarrays.

 #Example Usecases
 #Input : Arr[] = [ 1 , 2 , 3 , 4 , 5 , 5  ]
 #Output :  [ 1 2 3 4 ]
 #         [ 5 , 5 ]

 #Input : Arr[] = [ 4, 1, 2, 3 ]
 #Output : [4 1]
 #         [2 3]

# Input : Arr[] = [ 4, 3, 2, 1]
# Output : Not Possible
# [ 1 , 2 , 3 , 4 , 5 , 5, 6 ]

def getSumArray(arr):
  totalLength = len(arr)
  midLength =  mid = int(len(arr)/2)
#   sumLeft =  
  for i in range(midLength):
    if(sum(arr[0:mid]) > sum(arr[mid: totalLength])):
      mid -=1
    elif (sum(arr[mid: totalLength]) > sum(arr[0:mid])):
      mid+=1
    else: 
      return arr[0:mid], arr[mid:totalLength]
  return 'Not possible'

print(getSumArray([ 2, 3, 4, 1 ]))
print(getSumArray([ 1 , 2 , 3 , 4 , 5 , 5  ]))
print(getSumArray([ 1 , 2 , 3 , 4 , 5 , 5, 6 ]))

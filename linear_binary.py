### Searching: Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].
# Do it using linear and binary search techniques

def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1

arr = ['t','u','t','o','r','i','a','l']
x = 'k'
print("element found at index "+str(linearsearch(arr,x)))

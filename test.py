def findPairs(arr1, arr2, x):
  for i in range(0, len(arr1)):
      for j in range(0, len(arr2)):
          if (arr1[i] + arr2[j] == x):
              print(arr1[i], arr2[j])

# Driver code
arr1 = [1, 2, 3, 7, 5, 4]
arr2 = [0, 7, 4, 3, 2, 1]
x = 8
findPairs(arr1, arr2, x)
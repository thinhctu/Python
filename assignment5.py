# Q1 Bubble Sort

# def bubbleSort(arr):
#     for i in range(len(arr)):
#         #last i elements are sorted
#         for j in range(len(arr)-1):
#         # swap if current is larger than the next element
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# print(bubbleSort([5,1,4,2,8]))

# Q2 Selection sort
# def selectionSort(arr):
#     for i in range(len(arr)):
#         #index of minimum value
#         minIndex = i
#         for j in range(i+1,len(arr)):
#             #update index if new min is found
#             if arr[minIndex] > arr[j]:
#                 minIndex = j
#         #swap min to the end
#         arr[minIndex], arr[i] = arr[i],arr[minIndex]
#     return arr

# print(selectionSort([5,1,4,2,8]))

# Q3 Insertion sort
# def insertionSort(arr):
#     for i in range(1,len(arr)):
#         j = i-1
#         value = arr[i]
#         #shift all elements greater than the current value up by 1
#         while j >= 0 and value < arr[j]:
#                 arr[j + 1] = arr[j]
#                 j -= 1
#         arr[j + 1] = value
#         print(arr)
#     return arr
# print(insertionSort([5,1,4,2,8]))

# Q4 Mergesort
# def mergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         left = arr[:mid]
#         right = arr[mid:]
#         #divide the array up until it's one element and sort those
#         mergeSort(left)
#         mergeSort(right)
#         #i and j for the two halves
#         i = j = 0
#         #k for merged list
#         k = 0
#         #append the smaller value and increment the iterator
#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#                 arr[k] = left[i]
#                 i += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#             k += 1
#         # any remaining values in either left or right
#         while i < len(left) or j < len(right):
#             if i < len(left):
#                 arr[k] = left[i]
#                 k += 1
#                 i += 1
#             if j < len(right):
#                 arr[k] = right[j]
#                 k += 1
#                 j += 1
#     return arr

# print(mergeSort([5,1,2,3,4]))

# Q5
# recursive
# def longestSubsequence(s, t):
#     if not s or not t:
#         return 0
#     #if the first character is the same, add 1 to the count and recurse over [1:]
#     elif s[0] == t[0]:
#         return 1 + longestSubsequence(s[1:],t[1:])
#     #if they're different, then compare the second character of s/t with t/s
#     else:
#         return max(longestSubsequence(s[1:], t), longestSubsequence(s,t[1:])) 

# # DP 
# def longestSubsequence1(s,t):
#     m = len(s)
#     n = len(t)
#     #create a matrix size m+1 by n+1
#     matrix = [[0 for i in range(n+1)] for j in range(m+1)]
#     for row in range(1,m+1):
#         for col in range(1,n+1):
#             if s[row - 1] == t[col - 1]:
#                 matrix[row][col] = 1 + matrix[row - 1][col - 1]
#             else:
#                 matrix[row][col] = max(matrix[row][col-1],matrix[row-1][col])
#     return matrix[m][n]

# print(longestSubsequence1('abcd','adcef'))

# Q6 
# def findCombos(s,index=0):
#     if index == len(s) - 1:
#         print("".join(s))
#     for i in range(index, len(s)):
#         # change string to character array
#         letters = [ch for ch in s]
#         # swap elements of the word
#         letters[index], letters[i] = letters[i], letters[index]
#         # recurse until index is the same as length
#         findCombos(letters, index + 1)
    
# findCombos('abc')

#backtracking
# def permute(data, i, length): 
#     if i==length: 
#         print(''.join(data) )
#     else: 
#         for j in range(i,length): 
#             #swap
#             data[i], data[j] = data[j], data[i] 
#             permute(data, i+1, length) 
#             data[i], data[j] = data[j], data[i]  
  

# string = "ABC"
# n = len(string) 
# data = list(string) 
# permute(data, 0, n)

# Q7

# the way to get to n steps is the way to get to n-1 steps + 1 step and n-2 steps + 2 steps
# f(n) = f(n-1) + f(n-2)
# def stairs(n):
#     #base cases
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     #base array for 1 and 2 steps
#     steps = [1,2]
#     #DP for more than 2 steps maintaining constant space    
#     for i in range(2,n):
#         temp = steps[1]
#         steps[1] = steps[0] + steps[1]
#         steps[0] = temp
#     return steps[1]

# Q8
# def pascal(n):
#     #base case
#     output = [[1]]
#     for i in range(1,n):
#         #fill triangle with 1s
#         output.append([1]*(i+1))
#         for j in range(1,i):
#             # set each value as the sum of the numbers above it
#             output[i][j] = output[i-1][j] + output[i-1][j-1]
#     return output

# Q9

# def minMovesUnique(nums):
#     output = 0
#     value = -1
#     #value represents the unique value at each position
#     nums_sorted = sorted(nums)
#     for i in nums_sorted:
#     #unique value
#         if value < i:
#             value = i
#             print(value)
#     #if value is >= i then it's not unique, so increment and add to the output
#         else:
#             value += 1
#             output += value - i
#             print('value ' + str(value) + ' output ' + str(output))
#     return output

# print(minMovesUnique([3,2,1,2,1,7]))

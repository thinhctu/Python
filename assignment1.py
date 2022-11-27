# Q1
# cast the integer into a string, use slicing to reverse
# and cast it back into an int
#n = 12345
#print(int(str(n)[::-1]))

# Q2
# def isPalindrome(x):
#     if str(x) == str(x)[::-1]:
#         return True

# print(isPalindrome(121))

# Q3
# def happyMath(n):
#     total = 0
#     while n > 0:
#         value = n % 10
#         n //= 10
#         total += value**2
#     return total 
# def isHappy(n):
#     cycle = set()
#     while n != 1 and n not in cycle:
#         cycle.add(n)
#         n = happyMath(n)
#     return n == 1

# print(isHappy(2))

# Q4
# def missing(nums):
#     return sorted(set(range(0,len(nums)+1))-set(nums))[0]

# nums = [0,1]
# print(missing(nums))

# Q5
# def addOne(digits):
#     number = ''
#     newDigits = []
#     for digit in digits:
#         number += str(digit)
#     number = str(int(number) + 1)
#     for n in number:
#         newDigits.append(int(n))
#     return newDigits

# def plusOne(digits):
#     number = int("".join(map(str, digits)))
#     add = str(number + 1)
#     res = [int(x) for x in add]
#     return  res

# print(plusOne([1,2,3]))

#Q6
#XOR of the same number returns 0
# def single(nums):
#     value = 0
#     for num in nums:
#         value ^= num
#     return value

# print(single([4,1,2,1,2]))

# Q7
# def moveZero(nums):
#     pointer = 0
#     end = len(nums)
#     while pointer < end:
#         if nums[pointer] == 0:
#             del nums[pointer]
#             nums.append[0]
#             end -= 1
#         else:
#             pointer += 1
#     return nums

# #list comprehension 
# def moveZero1(nums):
#     zeroes = nums.count(0)
#     nums[:] = [i for i in nums if i != 0]
#     nums.extend([0]*zeroes)
#     return nums
# nums = [0, 1, 0, 3, 12]

# print(moveZero1(nums))

# Q8
# def reverseString(s):
#     start = 0
#     end = len(s) - 1

#     while start < end:
#         temp = s[start]
#         s[start] = s[end]
#         s[end] = temp
#         start += 1
#         end -= 1
#     return s

# s = ['h', 'e', 'l', 'l', 'o']

# print(reverseString(s))

# def rotate(s,r):
#     nums = '0123456789'
#     low = 'abcdefghijlkmnopqrstuvwxyz'
#     cap = 'ABCDEFGHIJKLMNOPQRSTUV'
#     new_string = ''
#     chars = list(s)
#     for ch in chars:
#         if ch.isalnum() == False:
#             continue
#         if ch.isdigit():
#             ch = chr()
#             #print(chr((ord(ch) + r)))
#     return new_string

#rotate('39ZA', 4)

# Q9
def rotate(s,r):
    new_string = ''
    for i in range(len(s)):
        #keep the same if not alphanumberic
        if s[i].isalnum() == False:
            new_string += s[i]
            continue
        #uppercase letters
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            letter = chr((ord(s[i])+r-65)%26 + 65)
        #lowercase letters
        elif ord(s[i]) >= 97 and ord(s[i]) <= 122:
            letter = chr((ord(s[i])+r-97)%26 + 97)
        #numbers
        elif ord(s[i]) >= 48 and ord(s[i]) <= 57:
            letter = chr((ord(s[i])+r-48)%10 + 48)

        new_string += letter
    return new_string

print(rotate('39ZA', 4))
# Q1
# def validParenthesis(s):
#     stack = []

#     p = {")": "(", "]" : "[", "}" : "{"}
#     for letter in s:
#         if letter in ["(", "[", "{"]:
#             stack.append(letter)
#         elif letter in [")", "]", "}"]:
#             # close parenthesis without open
#             if not stack:
#                 return False
#             # parathesis doesn't match
#             elif stack.pop() != p[letter]:
#                 return False
#             else:
#                 continue
#     if len(stack) == 0:
#         return True
#     else:
#         return False

# print(validParenthesis('([[]])'))

# Q2

# def letterCombo(s):
#     mapping = {
#         '2' : 'abc',
#         '3' : 'def',
#         '4' : 'ghi',
#         '5' : 'jkl',
#         '6' : 'mno',
#         '7' : 'pqrs',
#         '8' : 'tuv',
#         '9' : 'wxyz'
#     }
#     #empty list if no digits
#     result = [''] if s else []
#     for digit in s:
#         combinations = []
#         for letter in mapping[digit]:
#             for combination in result:
#                 combinations.append(combination+letter)
#         result = combinations
#     return result

# print(letterCombo('23'))

# Q3 
# def buildTarget(target, n):
#     output = []
#     index = 0
#     for i in range(1,target[-1] + 1):
#         output.append("Push")
#         if i != target[index]:
#             output.append("Pop")
#         else:
#             index += 1
#     return output

#print(buildTarget([1,4],4))

# Q4
# def indicesSum(nums, target):
# # Dictionary to map int 1 to int 2, where i2 = target - i1
#     differences = {}
#     for i in range(len(nums)):
#         if nums[i] in differences:
#             return [differences[nums[i]], i]
#         else:
#             differences[target-nums[i]] = i

# print(indicesSum([2,7,11,15],9))

# Q5 
# def isomorphic(s,t):
#      return [s.find(i) for i in s] == [t.find(j) for j in t]

# def isomorphic(s,t):
#     mapping = {}
#     for i in range(len(s)):
#         if s[i] not in mapping:
#             mapping[s[i]] = 

#print(isomorphic('orr','ooo'))

# Q6
# def nonRepeat(s):
#     indices = []
#     for i in set(s):
#         if s.count(i) == 1:
#             indices.append(s.index(i))
#     if len(indices) > 0:
#         return s[min(indices)]
#     else:
#         return -1

# print(nonRepeat('aabb'))
# print(nonRepeat('pythonprogram'))


# Q7
# def oneRow(words):
# # map the letters to the row
#     mapping = { 'q':1,'w':1,'e':1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1,'p':1,
#                 'a':2,'s':2,'d':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2,
#                 'z':3,'x':3,'c':3,'v':3,'b':3,'n':3,'m':3 }
#     output = []
#     for word in words:
#         same_row = set()
#         for letter in word:
#             same_row.add(mapping[letter.lower()])
#         if len(same_row) == 1:
#             output.append(word)
#     return output

# words = ['Hello', 'Alaska', 'Dad', 'Peace']
# words1 = ['asdf', 'sfd']
# print(oneRow(words1))

# Q8
# def morse(words):
#     morse_code = [".-","-...","-.-.","-..",".","..-.","--.",
#                  "....","..",".---","-.-",".-..","--","-.",
#                  "---",".--.","--.-",".-.","...","-","..-",
#                  "...-",".--","-..-","-.--","--.."]
#     morse_words = []
#     for word in words:
#         # get the right index by subtracting ascii values from ord
#         morse_w = ''.join(morse_code[ord(letter)-ord('a')] for letter in word)
#         morse_words.append(morse_w)
#     #set for unique transformations
#     return len(set(morse_words))

# print(morse(['gin','zen','gig','msg']))

# Q9
def anagram(s,t):
    return sorted(s) == sorted(t)

def anagram1(s,t):
    return all([s.count(l) == t.count(l) for l in 'abcdefghijklmnopqrstuvwxyz'])


print(anagram1('rat','car'))
print(anagram1('nagaram','anagram'))
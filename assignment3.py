# Q1
# Use binary search algorithm
# def firstBadVersion(n, bad):
#     left = 0
#     right = n-1
#     while (left <= right):
#         middle = (left+right)/2
#         if isBadVersion(middle):
#             right = middle
#         else:
#             left = middle + 1
#     return left

# Q2
# def goal(s, goal):
#     count = 0
#     #store indexes of the differences
#     index = []
#     if len(s) != len(goal):
#         return False
#     #if they're identical strings
#     if s == goal:
#         #if there is at least one duplicate pair of letters
#         return len(s) - len(set(s)) >= 1
#     for i in range(len(s)):
#          if s[i] != goal[i]:
#              count += 1
#              index.append(i)
#     if count != 2:
#         return False
#     return s[index[0]] == goal[index[1]] and s[index[1]] == goal[index[0]]
# print(goal("aa","aa"))

# Q3
# def duplicate(nums):
#     return len(set(nums)) != len(nums)

# print(duplicate([1,2,3,4]))

#Q4
# def letterAdded(s, t):
#     letters = list(t)
#     for ch in s:
#         letters.remove(ch)
#     return letters[0]

# def letterAdded1(s,t):
#     value = 0
#     for ch in s + t:
#         value ^= (ord(ch))
#     return chr(value)

# print(letterAdded('abcd','abcde'))

# Q5
# def reverseVowels(s):
#     #use set for constant time lookup
#     letters = list(s)
#     vowels = {'a','e','i','o','u','A','E','I','O', 'U'}
#     vowel_list = []
#     indices = []
#     for i in range(len(s)):
#         if s[i] in vowels:
#             vowel_list.append(s[i])
#             indices.append(i)

#     vowel_list.reverse()
#     #print(vowel_list)
#     for i in range(len(indices)):
#         letters[indices[i]] = vowel_list[i]

#     return ''.join(letters)

# print(reverseVowels('hello'))

# Q6
# def longestSubstring(s):
#     seen = {}
#     left = 0
#     max_length = 0
#     for right, ch in enumerate(s):
#         if ch in seen and left <= seen[ch]:
#             left = seen[ch] + 1
#         else:
#             max_length = max(max_length, right - left + 1)
#         seen[ch] = right
#     return max_length

# print(longestSubstring('adcadccbb'))

# Q7
# def mergeNums(nums1, nums2, m, n):
#     s_nums1 = ''.join([str(x) for x in nums1])
#     s_nums2 = ''.join([str(x) for x in nums2])
#     result = sorted(s_nums1[:m] + s_nums2[:n])
#     return [int(x) for x in result]

# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# print(mergeNums(nums1,nums2,m,n))

# Q8
import random
class Guess():
    def __init__(self):
        self.allowed_guesses = 0
        self.guess_count = 0
        self.min = 0
        self.max = 0
        self.target = 0
        self.player_guess = 0
        self.previous_guess = 0
        self.play = 'no'
        self.game()

    def game(self):
        #keep running until it breaks
        while(True):
            # Three specified inputs
            self.min = int(input("Enter min: "))
            self.max = int(input("Enter max: "))
            self.allowed_guesses = int(input("Enter allowed guesses: "))
            #determine target from input using random.randint
            self.target = random.randint(self.min, self.max)
            #print(self.target) checking if working properly

            self.player_guess = int(input("Guess the number between {} and {}: ".format(self.min,self.max)))
            # first guess
            if self.player_guess > self.target:
                self.previous_guess = self.player_guess
                print("Too Big!")
                self.guess_count += 1
            if self.player_guess < self.target:
                self.previous_guess = self.player_guess
                print("Too Small!")
                self.guess_count += 1
            elif self.player_guess == self.target:
                self.play=input("Congrats! Wanna try again? ")
                break

            # additional guesses
            while self.player_guess != self.target:
                if self.guess_count == self.allowed_guesses:
                    self.play = input("You've lost! Correct Answer is " + str(self.target) + ". Wanna try again? ")
                    break
                self.player_guess = int(input("Enter another number: "))
                self.previous_guess = self.player_guess
                if self.player_guess == self.target:
                    self.play=input("Congrats! Wanna try again? ")
                    break
                # warmer/colder calculated using absolute value of the difference
                elif abs(self.target - self.previous_guess) >= abs(self.target - self.player_guess):
                    print("Warmer")
                    #print("guesses", self.guess_count) checking counter
                    self.guess_count += 1
                elif abs(self.target - self.previous_guess) < abs(self.target - self.player_guess):
                    print("Colder")
                    #print("guesses", self.guess_count)
                    self.guess_count += 1
            #break out of while(true)
            break   
        # restart game
        if self.play == 'yes':
             Guess()
    
Guess()
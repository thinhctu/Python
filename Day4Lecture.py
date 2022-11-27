# #!/usr/bin/env python3

# Day 4

# Exception Handling

# print('Print an unknown variable', x)
#
# print('This will not be printed')

# try:
#     print('Print an unknown variable', x)
# except:
#     print('An exception happened')
#
# print('I will be printed')

#

# def test():
#     try:
#         # print(1)
#         # print(x)
#         print(1/0)
#     except TypeError as te:
#         print('Type Error --- ', te)
#     except NameError as ne:
#         print('Name Error --- ', ne)
#     except:
#         print('Something else happened.')
#         return 1
#     else:
#         print('Seems everything is fine.')
#     finally:
#          print('I will always get printed')
#
#     #
#     print(1)
#
# test()



# Escape Characters
#
# print('\\')
# print('abc\ndef')
# print('abc\'string\'def')




# File Handling
#

# file1 = open('./Demo.txt', 'r')
# print(file1.readline())
# print(file1.readlines())
# file1.close()


# with open('Demo.txt') as file2:
#     for line in file2.readlines():
#         print(line, end = '')
# file2.close()


# file2 = open('./Demo.txt', 'a')
# file2.write('add a new line\n')
# file2.write('add another line\n')
# file2.close()

#
# file3 = open('./Demo.txt', 'w')
# file3.write('add a new line\n')
# file3.write('add a another line\n')
# file3.close()


# file = open('./Demo.txt', 'a')
# file.write('line1\n')
# file.write('line2\n')
# file.write('line3\n')
# file.close()


# Matrix

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# print(matrix[0][1])
#
#
# for i in range(3):
#     for j in range(3):
#         pass
#
# matrix = [[0 for j in range(3)] for i in range(3)]
# print(matrix)




# Linked list

# class Node():
#
#     def __init__(self, value = 0, next = None):
#         self.value = value
#         self.next = next
#
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
#
# head = n1
#
# while head:
#     print(head.value)
#     head = head.next







# # Tree

class TreeNode():

    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6


root = n1

# DFS

# Inorder traversal leads to a sorted array if it is a Valid Binary Search Tree.

# Inorder
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)

# inorder(root)

def preorder(root):
    if root is None:
        return
    print(root.value)
    preorder(root.left)
    preorder(root.right)

# preorder(root)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value)

# postorder(root)

# Non-recursive same as preorder
def dfs(root):
    stack = [root]
    while stack:
        temp = stack.pop()
        if temp:
            print(temp.value)
            stack.append(temp.right)
            stack.append(temp.left)

# dfs(root)







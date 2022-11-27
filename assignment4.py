class TreeNode():

    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right



# Q1

# def isValidBST(root: TreeNode, low=float('-inf'), high=float('inf')):
#     if not root:
#         return True
#     elif not low < root.value < high:
#         return False
#     return isValidBST(root.left,low, root.value) and isValidBST(root.right,root.value, high)


# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n6 = TreeNode(6)

# n5.left = n1
# n5.right = n4
# n4.left = n3
# n4.right = n6

# root = n5

# print(isValidBST(root))

# Q2
# def searchBST(root: TreeNode, val):
#     if not root:
#         return None
#     if root.value == val:
#         return root
#     elif root.value < val:
#         return searchBST(root.right, val)
#     elif root.value > val:
#         return searchBST(root.left, val)

# def preorder(root):
#     if root is None:
#         return
#     print(root.value)
#     preorder(root.left)
#     preorder(root.right)

# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n7 = TreeNode(7)
# # n6 = TreeNode(6)

# n4.left = n2
# n4.right = n7
# n2.left = n1
# n2.right = n3
# root = n4

# print(preorder(searchBST(root, 2)))

# Q3
# def mergeLists(l1, l2):
#     if not l1 or not l2:
#         return l1 or l2
#     if l1.val < l2.val:
#         l1.next = mergeLists(l1.next, l2)
#         return l1
#     else:
#         l2.next = mergeLists(l1, l2.next)
#         return l2

# def mergeLists2(l1, l2):
#     dummy = cur = ListNode(0)
#     while l1 and l2:
#         if l1.val < l2.val:
#             cur.next = l1
#             l1 = l1.next
#         else:
#             cur.next = l2
#             l2 = l2.next
#         cur = cur.next
#     #whatever linked list still has values in it
#     cur.next = l1 or l2
#     return dummy.next

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

# Q4
# def diameter(root):
#     dia = 0
#     #function to find the depth of a node
#     def height(p):
#         if not p: 
#             return 0    
#         left, right = height(p.left), height(p.right)
#         # update the value of the diameter
#         ans = max(dia, left+right)   
#         return 1+max(left, right)
        
#     height(root)
#     return dia

# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n7 = TreeNode(7)
# # n6 = TreeNode(6)

# n4.left = n2
# n4.right = n7
# n2.left = n1
# n2.right = n3
# root = n4

# Q5
# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n6 = TreeNode(6)

# n5.left = n3
# n5.right = n6
# n3.left = n2
# n3.right = n4
# n2.left = n1


# root = n5
# def kthSmallest(root, k):
#     nodes = []
#     inorder(root, nodes)
#     return nodes[k-1]

# def inorder(root, nodes):
#     if not root:
#         return
#     inorder(root.left, nodes)
#     nodes.append(root.value)
#     inorder(root.right, nodes)


# print(kthSmallest(root, 3))

def hasPathSum(root, targetSum):
    if not root:
        return False
    if not root.left and not root.right and root.value == targetSum:
        return True
    targetSum -= root.value
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)

n5 = TreeNode(5)
n4 = TreeNode(4)
n11 = TreeNode(11)
n2 = TreeNode(2)
n7 = TreeNode(7)
n8 = TreeNode(8)
n13 = TreeNode(13)
n4 = TreeNode(4)

root = n5
n5.left = n4
n5.right = n8
n4.left = n11
n11.left = n7
n11.right = n2
n8.left = n13
n8.right = n4

print(hasPathSum(root, 22))
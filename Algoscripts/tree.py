# #node defination
# class Node:
#     def __init__(self,value):
#         self.left=None
#         self.data=value
#         self.right=None
# class Tree:
#     def __init__(self,root):
#         self.root=Node(root)
#     def preorder(self,start,traverse):
#         if start:
#             traverse=self.preorder(start.left,traverse)
#             traverse+=str(start.data)+ '-'
#             traverse=self.preorder(start.right,traverse)
#         return traverse

# arr=[1,0,1,0,1,0,1]
# tree=Tree(1)
# tree.root.left=Node(0)
# tree.root.right=Node(1)
# tree.root.left.left=Node(0)
# tree.root.left.right=Node(1)
# tree.root.right.left=Node(0)
# tree.root.right.right=Node(1)
# print(tree.preorder(tree.root,''))
# class Node:
#     def __init__(self,value) #node ka value
#         self.right=None
#         self.val=value
#         self.left=None
# class Tree:
#     def __init__(self,root):
#         self.root=Node(root) #root node create krta hai
# tree=Tree(1)#root ka value
# tree.root.left=Node(0)
# tree.root.right=Node(1)
# print(tree.root)
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def preorder(self,root,traversal):  
        if root:
            traversal=self.preorder(root.left,traversal)
            traversal+=str(root.data)+'->' 
            traversal=self.preorder(root.right,traversal)
        return traversal
               
# tree=Tree(1)
# tree.root.left=Node(0)
# tree.root.right=Node(1)
# tree.root.left.left=Node(0)
# tree.root.left.right=Node(1)
# tree.root.right.left=Node(0)
# tree.root.right.right=Node(1)
tree=Tree(3)
tree.root.left=Node(9)
tree.root.right=Node(20)
tree.root.right.left=Node(15)
tree.root.right.right=Node(7)
stack=[(tree.root,0)]
res=0
depth=0
iternation=0
while stack:
    root,curr_node=stack.pop()
    if root:
        curr_node=(curr_node<<1)|root.data
        if root.left is None and root.right is None:
            res+=curr_node
            depth=max(iternation,depth)
        else:
            stack.append((root.left,curr_node))
            stack.append((root.right,curr_node))
            iternation+=1
print(res)
print(depth)
#bfs
import statistics
ans=[]
meanarr=[]
queue=[(tree.root,0)]
while queue:
    root,level=queue.pop()
    if root:
        if not level<len(ans):
            ans.append([])
        ans[level].append(root.data)
        queue.append((root.right,level+1))
        queue.append((root.left,level+1))


print(ans)
from statistics import mean
print([mean(i) for i in ans])
#Iterative dfs (IN/PRE/POST)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:
                    #post=> LRV=>VRL(Using stack)
                    #pre=> VLR=>RLV(Using stack)
                    #in=>LVR=>RVL(Using stack)
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res
#search node is present in BST or not and return subtree
#<template>
if not root:
        return None        
while root:
    if root.val == val:
        return root
    elif val < root.val:
        root = root.left
    else:
        root = root.right

return None
#insert in BST:
#<iterative>
if not root: return TreeNode(val)
curr_node = root #just do it
while True:
    if curr_node.val <= val: # go R
        if curr_node.right:
            curr_node = curr_node.right
        else:
            curr_node.right = TreeNode(val)
            break
    else:
        if curr_node.left:
            curr_node = curr_node.left
        else:
            curr_node.left = TreeNode(val)
            break
return root
#<recursive>
def insert(node,val):
    if val>node.val:
        if not node.right:
            node.right=TreeNode(val)
        else:
            insert(node.right,val)
    else:
        if not node.left:
            node.left=TreeNode(val)
        else:
            insert(node.left,val)

insert(root,val)
return root
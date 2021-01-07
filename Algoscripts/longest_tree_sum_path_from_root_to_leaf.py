Longest Tree Sum Path From Root to Leaf
**Given a binary tree root, return the sum of the longest path from the root to a leaf node. If there are two equally long paths, return the larger sum.**
IDEA
Keep track each pathsum and node count
find max num of nodes
find max sum of those nodes
3 Pass O(N) solution
class Solution:
    def solve(self, root):
        if not root:return 0
        self.ans=0
        self.temp=[]

        def dfs(root,i,nodes):
            if  root:
                i+=root.val
                nodes+=1
                if root.left is None and root.right is None:
                    self.temp.append([i,nodes])
                dfs(root.left,i,nodes)
                dfs(root.right,i,nodes) 
        dfs(root,0,0)
        self.ans,x=max(self.temp,key=lambda x:x[1])
        for i in self.temp:
            if i[1]==x:
                self.ans=max(self.ans,i[0])
        return self.ans
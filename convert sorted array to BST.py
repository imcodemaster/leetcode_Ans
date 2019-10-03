class Solution:
    
    def sortedArrayToBST(self, num):
        if len(num)==0: return None
        if len(num)==1:
            root=TreeNode(num[0])
            return root
        mid=int(len(num)/2)
        root=TreeNode(num[mid])
        num1=num[0:mid]
        num2=num[(mid+1):]
        root.left=self.sortedArrayToBST(num1)
        root.right=self.sortedArrayToBST(num2)
        return root

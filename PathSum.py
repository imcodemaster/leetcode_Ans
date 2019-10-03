# Python program to find if there is a root to sum path 

# A binary tree node 
class Node: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None


# s is the sum 
def hasPathSum(node, s): 
	if node is None: 
		return (s == 0) 

	else: 
		ans = 0
		subSum = s - node.data 
		if(subSum == 0 and node.left == None and node.right == None): 
			return True

		if node.left is not None: 
			ans = ans or hasPathSum(node.left, subSum) 
		if node.right is not None: 
			ans = ans or hasPathSum(node.right, subSum) 

		return ans 

# Driver program  

s = 21
root = Node(10) 
root.left = Node(8) 
root.right = Node(2) 
root.left.right = Node(5) 
root.left.left = Node(3) 
root.right.left = Node(2) 

if hasPathSum(root, s): 
	print ("There is a root-to-leaf path with sum %d",(s)) 
else: 
	print ("There is no root-to-leaf path with sum %d", (s)) 

# TASK COMPLETED

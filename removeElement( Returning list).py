class Solution:
    def removeElement(nums, val):
        #initialize with new array 
        new = []
        for i in range(len(nums)):
            #iterating full input
            if nums[i] != val : #if value (given for deletion) not encountered
                new.append(nums[i]) #append nums[i] to new array 
        return new #returning new array 


nums = [1,2,3,4,5,6]
val = 4 
print (Solution.removeElement(nums, val))

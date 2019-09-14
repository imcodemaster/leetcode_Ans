def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums)-1:
                #just checking the last digit is bigger or not 
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return nums 


#Driver Code
nums = [1,1,2,2,3,3,4,5, 5, 6,7]
print (removeDuplicates(nums))

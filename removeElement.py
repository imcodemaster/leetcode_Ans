class Solution:
    def removeElement(nums, val):
        count = 0
        for i in range(len(nums)):
            if nums[i] != val :
                nums[count] = nums[i]
                count +=1
        return count


nums = [1,2,3,4,5,6]
val = 4
print (Solution.removeElement(nums, val))

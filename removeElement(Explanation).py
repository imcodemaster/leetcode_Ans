class Solution:
    def removeElement(nums, val):
        #initial value assuming
        count = 0
        for i in range(len(nums)):
            #iterating loop through out len(num)
            if nums[i] != val : #if val is not encounter :
                nums[count] = nums[i] #equating nums[i] value to nums[count]
                count +=1 #increment the count variable 
        return count #return it (gives lenght of count
                        #(no. of number counts got appending  )) 


nums = [1,2,3,4,5,6]
print('len(nums) : ' , len(nums))
val = 4
print (Solution.removeElement(nums, val))

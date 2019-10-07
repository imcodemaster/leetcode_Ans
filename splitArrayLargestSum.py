
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def isValidCeiling(nums, m, ceiling):
            count, total = 1, 0  
            for i in range(len(nums)):
                if total + nums[i] <= ceiling:
                    total += nums[i] 
                else:
                    total = nums[i]  
                    count += 1
                if (count > m):
                    return False 
            return True 

        l, r = max(nums), sum(nums)
        while l <= r:
            mid = (l + r) // 2
            if isValidCeiling(nums, m, mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

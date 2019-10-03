
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        
        cache, st = {}, []
        for x in nums:
            if len(st) == 0:
                st.append(x)
            elif x <= st[-1]:
                st.append(x)
            else:
                while st and st[-1] < x:
                    cache[st.pop()] = x
                st.append(x)
        result = []
        for x in findNums:
            if x in cache:
                result.append(cache[x])
            else:
                result.append(-1)
        return result


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
      
        cache, st = {}, []
        for x in nums:
            while st and st[-1] < x:
                cache[st.pop()] = x
            st.append(x)
        result = [-1]*len(findNums)
        for idx,x in enumerate(findNums):
            if x in cache:
                result[idx] = cache[x]
        return result

 
num = [2,7,11,15]
n = len(num)
x = 9
    
class Solution ():
    def twoSum (nums , x ):
        i = 0
        j = n - 1
        while i <= j :
            if num[i] + num[j] == x:
                print (num[i] , num[j])
                return True
            elif num[i] + num[j] < x :
                    i = i + 1
            else :
                    j = j - 1
        return False
print (Solution.twoSum(num , x))

#creating class
class Solution:
    #defining function with input haystack and needle 
    def strStr(haystack, needle):
        len1=len(haystack)
        len2=len(needle)
        if len1<len2: # if haystack lenght smaller than needle lenght
            return -1
        for i in range(len1-len2+1):
            if haystack[i:i+len2]==needle:
                return i
        return -1

haystack = 'hello'
needle = 'll'
print (Solution.strStr(haystack, needle))

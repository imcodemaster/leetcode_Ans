#creating class
class Solution:
    #defining function with input haystack and needle 
    def strStr(haystack, needle):
        len1=len(haystack)
        print ('len1 : ' , len1)#get lenght of haystack
        len2=len(needle)
        print ('len2 : ' , len2) # get lenght of needle 
        if len1<len2: # if haystack lenght smaller than needle lenght
            #return -1 (not possible)
            return -1
        for i in range(len1-len2+1):
            print (' i : ', i )
            print (' print haystack [i:i+len2]: ' , haystack[i : i+len2] )
            print (' range from len1-len2+1 : ' , len1-len2+1)
            print ('haystack [len1-len2+1] : ' , haystack [len1-len2+1])
            print ('haystack[i] : ' , haystack[i])
            print ('haystack[i+len2] : ' , haystack[i+len2]  )
            print ('needle : ' , needle  )

            if haystack[i:i+len2]==needle:
                print (' print haystack [i:i+len2]: ' , haystack[i : i+len2] )
                return i
        return -1

haystack = 'BadProgrammer'
needle = 'gram'
print (Solution.strStr(haystack, needle))



            

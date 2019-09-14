def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print('initial nums : ' , nums)
        i = 0
        print ('i : ' ,i)
        print('lenght of nums : ' , len(nums)-1)
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                print ('checking nums [i] == len(nums)-1 : ')  
                print('i : ' , i)
                print('nums[i] : ' , nums[i])
                print('i+1 : ' , i+1 )
                print('nums[i+1 ] : ' , nums[i+1])
                print(' >> delete nums[i] if same ')
                del nums[i]
                print('nums after deletion : ', nums)
            else:
                print('else : increment i ' )
                i += 1
                print('next i : ' , i)
                print(  ' final nums :  ' , nums)
        return nums 


#Driver Code
nums = [1,1,2,2,3,3,4,5, 5, 6,7]
print (removeDuplicates(nums))

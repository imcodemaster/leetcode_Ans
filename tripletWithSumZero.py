def findTriplet  (arr):
    arr.sort() #first sort the array 
    for i in range (0 , n-1):
        x = arr[i]
        leftpointer = i+1 #assign left pointer
        rightpointer = n-1 #assign right pointer

        while leftpointer < rightpointer : #while leftpointer smaller than rightpointer
            if x + leftpointer + rightpointer == 0 :
                print (x, leftpointer, rightpointer)
                leftpointer += 1
                rightpointer -= 1
                return True
            elif x + leftpointer + rightpointer < 0 :
                leftpointer += 1
            else :
                rightpointer -= 1
        return False

#Driver Code
arr = [0 , 1 , 2 , -1 , -3]
n = len (arr)
print (findTriplet (arr))

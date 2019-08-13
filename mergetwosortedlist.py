#Merging 2 sorted list : 
#create a function to merge 2 list :  
def mergelist (arr1, arr2) :
    for i in range (0, n):
        arr.append(arr1[i])
        i += 1
    for j in range (0, n2) :
        arr.append(arr2[j])
        j += 1 
     

#Driver Code
    
arr1 = [2,4 ,6 ,28 ,58, 67]
n = len(arr1)
arr2 = [16 ,48 ,52, 65]
n2 = len(arr2)
arr = []
mergelist (arr1, arr2) #Calling merge function 
print (sorted(arr)) #sort your merge list :



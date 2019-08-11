from statistics import median

def mergearray( arr1, arr2 ) :
    for i in range(0 , len1) :
        arr.append (arr1[i])
        i += 1

    for j in range (0 , len2):
        arr.append(arr2[j])
        j += 1



        
arr1 = [1,12,15,26,38 , 46]
print ('original array 1 : ' , arr1)
arr2 = [2,13,17,30,45]
print ('original array 2 : ' , arr2)
len1 = len(arr1)
len2 = len(arr2)
arr = []
mergearray (arr1, arr2)
print ('New list after merging and sort two given list  => \n', sorted(arr))
nn = len(arr)
print ('median of two sorted array => ' , median(arr))

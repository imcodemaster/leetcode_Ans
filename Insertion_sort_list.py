#insertion-sort-list

def insertionsort(sample):
    for i in range(1, len(sample)):
        j =i
        while (j!=0 and sample[j] < sample[j-1]):
            sample[j-1], sample[j] = sample[j], sample[j-1]

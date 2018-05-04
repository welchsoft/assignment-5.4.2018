import mysort
#array to be sorted
sort_me = [1,2,3,4,5,6,7,8,9,100,25,10,12,13,2,3,4,99,75,50]
size = len(sort_me)

mysort.quickSort(sort_me, 0, size-1)

print(sort_me)

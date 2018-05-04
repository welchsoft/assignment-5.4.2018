#create an array with some numbers in it
numbers = [11,2,3,4,5,6,-7,8,9,3,2,1]
temp = numbers[0]

#itterate through the array compare them against the smallest
for num in numbers:
    if num < temp:
        temp = num

#print result
print(temp)

#create an array with some numbers in it
numbers = [-1,2,3,4,-5,-6,-7,8,9,-4,-3,-1,312,19]
temp = numbers[0]

#itterate through the numbers and set temp to the largest value
for num in numbers:
    if num > temp:
        temp = num

#print result
print(temp)

#create an array with some numbers in it
numbers = [1,2,3,4,5,6,7,8,9]
temp = 0

#itterate through the numbers and set temp to the largest value
for num in numbers:
    if num > temp:
        temp = num

#itterate through the numbers again but this time compare them against the smallest
for num in numbers:
    if num < temp:
        temp = num

#print result
print(temp)

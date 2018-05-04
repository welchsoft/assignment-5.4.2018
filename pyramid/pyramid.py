#take user input
rows = int(input("Enter how many rows you want: "))

#draw this puppy
def drawPyramid(num):
    for i in range(num):
        print(' '*(num-i-1) + '*'*(2*i+1))

#call the function pass the input
drawPyramid(rows)

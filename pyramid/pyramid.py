rows = int(input("Enter how many rows you want: "))



def drawPyramid(num):
    for i in range(num):
        print(' '*(num-i-1) + '*'*(2*i+1))


drawPyramid(rows)

sort_me = [1,5,4,3,2,10]
size = len(sort_me)


for index in range(len(sort_me)-1,0,-1):
    for i in range(index):
        if sort_me[i] > sort_me[i+1]:
            temp = sort_me[i]
            sort_me[i] = sort_me[i+1]
            sort_me[i+1] = temp

print(sort_me)
    
for index in range(len(sort_me)-1,0,-1):
    for i in range(index):
        if sort_me[i] < sort_me[i+1]:
            temp = sort_me[i]
            sort_me[i] = sort_me[i+1]
            sort_me[i+1] = temp

print(sort_me)

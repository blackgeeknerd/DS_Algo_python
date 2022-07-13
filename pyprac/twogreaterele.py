a = [2,8,7,1,5]
size = len(a)
b = []
# 2, 1, 5

for i in range(size):
    count = 0
    for j in range(size):
        if a[j] > a[i]:
            count = count + 1
    
    # if count >= 2:
        # print(a[i], end=" ")
        
        
#method 2
#using sorting

a.sort()
for i in range(0, size-2):
    print(a[i], end=" ")
    
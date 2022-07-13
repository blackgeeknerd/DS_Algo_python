numlst = [0,1,1,0 ]

def count_number_of_change(arr):
    counter = 0
    
    for i in range(len(arr)-1):
        if numlst[i] == numlst[i + 1]:
            counter = counter + 1
    return counter

print(count_number_of_change(numlst))
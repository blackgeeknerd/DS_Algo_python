def Quicksort(arr):
    
    less = []
    greater = []
    # pivot = len(arr)- 1 //2 
    
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        # pivot = len(arr)- 1 //2 
        
        for i in range(len(arr)):
            if arr[i] < pivot:
                # if arr[i] not in less:
                less.append(arr[i])
            else:
                if arr[i] > pivot:
                    # if arr[i] not in greater:
                    greater.append(arr[i])
        # print(lenght, arr[lenght])
        # print(pivot)
        return Quicksort(less) + [pivot] + Quicksort(greater)
        

testarr = [3,4,1,6,7,2,6,8,9, 1]

print(Quicksort(testarr))
    
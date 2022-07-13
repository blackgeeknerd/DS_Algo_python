#Quicksort method 1
def QuickSort(arr):
    
    elements = len(arr)
    
    #base case
    if elements < 2:
        return arr
    
    current_position = 0 #position of the partitioning element
    
    for i in range(1, elements): #partitioning  loop
        print(arr[i], arr[0])
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position]  = temp
            
    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp #brings pivot to its appopriate position
    
    left = QuickSort(arr[0:current_position])
    right = QuickSort(arr[current_position+1:elements])
    
    arr = left + [arr[current_position]] + right #merging everything together
    
    return arr

array_to_sort = [4,2,7,3,1,6]

# print("Original: " , array_to_sort)
# print("Sorted: ", QuickSort(array_to_sort) )
    
    
#Quicksort method 2
def quickSort2(arr):
    
    if len(arr) < 2:
        return arr
    
    else:
        pivot = arr[0]
        
        less = [i for i in arr[1:] if i <= pivot]
        print("less", less)
        
        greater = [i for i in arr[1:] if i >= pivot]
        print("greater", greater)
        
        return quickSort2(less) + [pivot] + quickSort2(greater)
    
print(quickSort2(array_to_sort))
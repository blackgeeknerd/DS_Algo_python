def reverseList(arr, start, end):
    while start < end :
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1
        
    return arr
    
A = [1, 2, 3, 4, 5, 6]
size = len(A)
# print(A)

# print(reverseList(A, 0, size-1))

test = "iloveyou"
testlist = [*test]
# reverse = reverseList(testlist, 0, len(testlist)-1)
# print(reverse)
# joined = " ".join(reverse)
# print(joined)

print(A[::-1])

def mul(arr):
    val = 1
    for i in range(0, len(arr)):
        val = val * arr[i]
    if val % 2 == 0:
        return val
    else:
        return 'Odd'
        
        

word = [1,3,3]
print(mul(word))
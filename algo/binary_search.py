num_list = []
for num in range(1, 101):
        num_list.append(num)

    

def binary_search(arr, item):

    
    low = 0
    high = len(arr) - 1
    counter = 0
    
    while low <= high:
        mid = (high + low) // 2
        guess = arr[mid]
        
        if guess == item:
            counter = counter + 1
            
            return mid, guess, item, counter
        elif guess > item:
            high = mid - 1
            # counter = counter + 1
        else:
            low = mid + 1
            # counter = counter + 1
        counter = counter + 1
        
    return None, counter


            
            
word = [1,2,3,5,6,7,8,10,11]
# first step = 6 less than 11
# second step = adding 1 to mid = 6 + 1

print(binary_search(num_list, 50))
    
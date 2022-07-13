
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
    



def find_runner_up(arr):
    listvale =[]
    arr.sort()
    # setlist = set(arr)
    # sortedlist = list(setlist)
    # sortedlist = arr.sort
    
    maxvalue = arr[-1]
    if arr[-2] != maxvalue and arr[-2] > arr[-3]:
        listvale.append(arr[-2])
        return arr[-2]
    else:
        return arr[-3]
    

winners = [5,3,10,1,8,9,8]

check_list =sorted([runner for runner in winners if runner > 5])

print(check_list)

print(find_runner_up(winners))



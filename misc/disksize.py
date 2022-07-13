import os
import sys

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendants"""
    
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
            
    print('{0:<7}'.format(total), path)
    return total


url = "/Users/ADMIN/Videos/me/"
# print(disk_usage(url))


"""An experiment to explore the relationship between a list's length and its underlying size in Python"""
data = []
n = 10
for k in range(n):
    a = len(data)       #number of elements
    b = sys.getsizeof(data)     #actual size in bytes
    print('lenght: {0:3d}; size in bytes: {1:4d}'.format(a,b))
    data.append(None)       #Increase length by one
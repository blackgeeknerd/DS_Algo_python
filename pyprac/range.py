class Range:
    """A Class that mimics the built-in range class"""
    
    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance.
        
        Semantics is similar to built-in range class
        """ 
        if step == 0:
            raise ValueError('Step cannot be 0')
        
        if stop is None:             #special case of range(n)
            start, stop = 0, start   #should be treated as if range(0,n)
            
        #calculate the effective length once
        self._length = max(0, (stop - start + step -1) // step)
        
        #need knowledge of start and step(but not stop) to support __getitem__
        self._start = start
        self._step = step
        
    def __len__(self):
        """Return number of entries in the range"""
        return self._length
    
    def __getitem__(self, k):
        """Return entry at index k (usingstandard interpretation if negative"""
        if k < 0:
            k += len(self)          #attempt to convert negative index
            
        if not 0 <= k < self._length:
            raise IndexError("Index out of range")
        
        return self._start + k * self._step
    
    
if __name__ == '__main__':
    
    ranger = Range(2,10, 3)
    range_list = []
    sum = 0
    for i in ranger:
        print(i)
        sum += i
        range_list.append(i)
    print(range_list)
    print(sum)
        
        
        
    
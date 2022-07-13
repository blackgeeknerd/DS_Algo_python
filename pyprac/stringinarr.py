def solve(s, arr):
    """Program that checks for possible outcome of a string and checks if any is in an already defined array/list
    
    Steps:
        1 - Find the permutations of the given string(which is all possible combination of the string)
        2 - store them in a list/array
        3 - check to see if elements in the new array(st_arr) are in the first array(message) 
        4 - if yes, store this elements in a new array(completelst)
        5 - Display the new array/list (completelst)
    """
    st_arr = []
    completelst = []
    
    for i in range(len(s)-1,-1,-1): #looping from the end of the string
        for j in range(len(st_arr)): #looping from the begining of the st_arr array
            st_arr.append(s[i] + st_arr[j]) #add the values of s[i] + st_arr[j]
            # print(s[i] + st_arr[j])
        st_arr.append(s[i])
    # return st_arr 
    
    for k in range(len(st_arr)): #loop over the st_arr array
        if st_arr[k] in arr: #check if elements in st_arr are in the first array (message)
            completelst.append(st_arr[k]) #if yes, add the element to the new array (completelst)

        if completelst:      
            newset = set(completelst)
            completelst = list(newset)
            
    return completelst  
        
def check_for_combination(s, arr):
    pass
      
# test = "huhyisdftelol"
# test = "huhyisdftelolkhsadgiyeqiuohobiugfkiuyi"
# test ='ubtpod'
# test = 'byuaiboylet'
test = 'khsadgiyeqiuohobiugfkiuyi'

message = ['hell', 'ho', 'tel', 'lol', 'hi', 'hu', 'baby', 'sad' , 'tell', 'holy', 'oooh', 'dug', 'let', 'bug', 'boy', 'oyb']
print(solve(test, message))


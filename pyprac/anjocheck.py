def checkstrings(word,block):
    from itertools import permutations
    
    return [s for s in block if tuple(s) in permutations(word, len(s))]
    

message = ['hell', 'ho', 'tel', 'let', 'lol', 'hi', 'hu', 'sad' , 'tell', 'holy', 'oooh', 'boy' , 'baby']
# test = "huhyisdftelol"
test = 'byuaiboylet'
# test = "huhyisdftelolkhsadgiyeqiuohobiugfkiuyi"

print(checkstrings(test, message))
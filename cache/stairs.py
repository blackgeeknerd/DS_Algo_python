from timeit import repeat
from functools import lru_cache


@lru_cache(maxsize=16)
def steps_to(stair):
    
    
    if stair == 1:
        #you can reach the first stair with only a single step from the floor
        return 1
    elif stair == 2:
        #you can reach the second stair by jumping from the floor 
        # with a single two-stair hop or by jumping
        # a single stair a couple of times
        return 2
    elif stair == 3:
        #you can reach the 3rd stair using four possible combinations
        # 1. Jumping all the way from the floor
        # 2. Jumping two stairs, then one
        # 3. Jumping one stair, then two
        # 4. Jumping one stair three times
        return 4
    else:
        #you can reach your current stair from 3 different places:
        # 1. From three stairs down
        # 2. from two stairs down
        # 3. from one stair down
        #
        # If you add up the number of ways of getting to thos 3 positions
        # then you should have your solution
        return(
            steps_to(stair -3)
            + steps_to(stair -2)
            + steps_to(stair - 1)
        )
        
print(steps_to(4))

print(steps_to.cache_info())

# setup_code = "from __main__ import steps_to"
# stmt = "steps_to(30)"
# times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
# print(f"minimum execution time: {min(times)}")
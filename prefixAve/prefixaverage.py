
#Using Quadratic-Time algorithm
def prefix_average1(S):
    """Return list such that, for all j, A[j] equals average of S[0],....s[j]."""
    n = len(S)
    A = [0] * n 
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        A[j] = total /(j+1)
    return A

def prefix_average2(S):
    """Returns list such that, for all j, A[j] equals average of S[0],....,S[j]."""
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j + 1])/(j + 1)
    return A


#Using linear-time algorithm
def prefix_average3(S):
    """Returns list such that, for all j, A[j] equals average of S[0],...S[j]."""
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total /(j + 1)
    return A

same = [50, 20,30, 34, 45]
print(prefix_average3(same))

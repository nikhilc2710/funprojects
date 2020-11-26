def memoize(fn):
    '''Return a memoized version of the input function.
    
    The returned function caches the results of previous calls.
    Useful if a function call is expensive, and the function 
    is called repeatedly with the same arguments.
    '''
    cache = dict()
    def wrapped(*v):
        key = tuple(v) # tuples are hashable, and can be used as dict keys
        if key not in cache:
            cache[key] = fn(*v)
        return cache[key]
    return wrapped
@memoize
def lcs_(i, j):
    if i and j:
        xe, ye = xs[i-1], ys[j-1]
        if xe == ye:
            return lcs_(i-1, j-1) + [xe]
        else:
            return max(lcs_(i, j-1), lcs_(i-1, j), key=len)
    else:
        return []
    return lcs_(len(xs), len(ys))
s1='ABC'
s2='CHIMPANZEE'
print(lcs_(s1,s2))
a=[1,2,3,0,0,0]
b=[2,5,6]
a=a+b
a.sort()
print(a)

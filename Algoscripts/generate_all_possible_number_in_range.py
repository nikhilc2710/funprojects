def sqeuntialDigits(lo,hi):
    """
     return all the  possible digit in range
     in increasing order
     lo=100 hi=300
     [123,234]
     """
    mapper="123456789"
    output=[]
    for digits in range(len(str(lo)),len(str(hi))+1):
        for i in range(0,10-digits):
            numberfound=int(mapper[i:i+digits])
            if numberfound<lo: continue
            if numberfound>hi: break
            output.append(numberfound)
    return output
print(sqeuntialDigits(100,300))
import sys
def bus_sell_stock1(arr):
    res=0
    cur_min=arr[0]
    arr.pop(0)
    for i in arr:
        res=max(res,i-cur_min)
        cur_min=min(cur_min,i)
    return res
print(bus_sell_stock1([7,6,4,3,1]))




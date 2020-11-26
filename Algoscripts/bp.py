a=[2,6,5,9,100]
i=0
try:
    while i<=len(a):
        diff=abs(a[i]-a[i+1])
        if diff not in a:a.append(diff)
        i+=1
except IndexError:
    print(f'{a}= {len(a)}')

#problem2 Infosys
from bisect import bisect_left
a=[1,6,2,9,4,3]
diff=0
i=0
while i<len(a)-1:
    if a[i]<a[i+1]:
       i+=1
    else:
        diff=max((a[i]-a[i+1]),diff)
        a[i],a[i+1]=a[i+1],a[i]
        i+=1

print(a)
print(diff)

# for i in range(len(a)-1):
#     if a[i]<a[i+1]:
#         pass
#     else:
#         diff=max((a[i]-a[i+1]),diff)
#         a[i],a[i+1]=a[i+1],a[i]
# print(diff)
# print(a)
#valid pranthesis #approch using stack and map
s='{{[[(())]]}}'
bracketmap={'{':'}','(':')','[':']'}
inputmap=['{','[','(']
stack=[]
for i in s:
    if i in inputmap:
        stack.append(i)
    elif stack and i==bracketmap[stack[-1]]:
        stack.pop()
    else:pass
print(stack)

def coinproblem(list,ammount):
    result=[0]+[ammount+1]*ammount
    print(result)
coinproblem([1,2,5],11)

class Solution:
    def coinChange(self, coins, amount):
        def dfs(start, amt, n_coins):
            nonlocal min_coins

            coin = coins[start]

            # LHS = lower bound on number of coins, achieved using the current coin
            # Return early since we can't possibly achieve original "amount"
            # along this path.
            # For this particular solution, this check isn't necessarily,
            # since there is another check within the loop below. However, it
            # speeds up the solution. Better to have this check before the
            # "amt == 0" check below.
            #if n_coins + (amt + coin - 1) / coin > min_coins:
            #if (min_coins - n_coins - 1) * coin + 1 < amt:
            #    return

            div = amt // coin
            n_coins += div
            amt %= coin
            
            if amt == 0:
                min_coins = min(min_coins, n_coins)
                return
            
            if start < len_coins:
                # use as many of current coin as possible, and try next smaller coin
                dfs(start + 1, amt, n_coins)

                # Always greedily taking as many of biggest coins as possible doesn't work.
                # "Backtrack" by using 1 less of current coin per iteration, and
                # trying the next smaller coin.

                next_coin = coins[start + 1]
                
                for _ in range(div):
                    amt += coin 
                    n_coins -= 1
                    
                    if (min_coins - n_coins - 1) * next_coin + 1 > amt:
                    #if (min_coins - n_coins) * next_coin > amt: # hope still exists
                        dfs(start + 1, amt, n_coins)
                    else:
                        break
        
        len_coins = len(coins) - 1
        
        # try biggest coins first
        coins.sort(reverse=True)
        
        min_coins = float('inf')

        dfs(0, amount, 0)
        
        return min_coins if min_coins < float('inf') else -1

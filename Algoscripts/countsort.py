# #!/bin/python

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    number_set=[]
    for i in arr:
        number_set.append(i[0])
    sext=set(list(map(int,number_set)))
    mapx={ix:[] for ix in sext}
    for it in arr:
        if int(it[0]) in mapx:
            mapx[int(it[0])].append(it[1])
    final_ans=[[] for i in range(len(sext))]
    # for index in mapx:
    #     print(mapx[index])
    #     final_ans[index].append('testmesaage')
    # print(final_ans)
    # print(mapx[0])
    # print(mapx[1])
    visited=[]
    mapindex=mapx.keys()
    for mindex in mapindex:
        for values in mapx[mindex]:
            if values not in final_ans[mindex] and values not in visited:
                final_ans[mindex].append(values)
            else:
                index=final_ans[mindex].index(values)
                visited.append(values)
                final_ans[mindex][index]='-'

    finalresult=""
    for i in final_ans:
        for j in i:
            finalresult+=j
    print(finalresult)
    
    
    #     for values in mapx[index]:
    #         if values not in final_ans:
    #             final_ans[index].append(values)
    #         else:
    #             innerindex=final_ans[index].index[values]
    #             final_ans[index][innerindex]='-'
    # print(final_ans)
    # number_set=[]
    # for i in arr:
    #     if i[1] not in number_set:
    #         number_set.append(i[1])
    #     else:
    #         index=number_set.index(i[1])
    #         number_set[index]='-'
    # print(number_set)

if __name__ == '__main__':
    n = int(raw_input().strip())

    arr = []

    for _ in xrange(n):
        arr.append(raw_input().rstrip().split())

    countSort(arr)




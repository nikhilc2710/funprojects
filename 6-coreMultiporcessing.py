import os
from random import randint
from functools import reduce
from operator import add
from multiprocessing import Pool
import time


def oddlist(num):
    return reduce(add,(i for i in range(num) if i&1))


if __name__ == '__main__':
    oddcounts=tuple(randint(10,50) for i in range(1000000))
    print('with multiporcessing')
    s=time.process_time()
    with Pool(12) as p:
        mp=p.map(oddlist, oddcounts)
    e=time.process_time()
    print(f'time took {e-s}')
    print('witout multiporcessing')
    s=time.process_time()
    z=tuple(oddlist(i) for i in oddcounts)
    e=time.process_time()
    print(f'time took {e-s}')






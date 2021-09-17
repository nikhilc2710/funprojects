def bubblesort(arr):
    N=len(arr)
    for i in range(N):
        for j in range(N-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
def mergesort(arr):
    def helper(arr1,arr2):
        p1,p2,ans=0,0,[]
        M,N=len(arr1),len(arr2)
        while p1<M and p2<N:
            if arr1[p1]<=arr2[p2]:
                ans.append(arr1[p1])
                p1+=1
            else:
                ans.append(arr2[p2])
                p2+=1
        ans.extend(arr1[p1:])
        ans.extend(arr2[p2:])
        return ans
    if len(arr)==1:return arr
    else:
        M=len(arr)//2
        firstHalf=mergesort(arr[:M])
        secondHalf=mergesort(arr[M:])
        return helper(firstHalf,secondHalf)


def insertionSort(arr):
    N=len(arr)
    for i in range(N):
        temp=arr[i]
        while i>=0 and arr[ i-1 if i-1>=0 else 0]>temp:
                arr[i-1],arr[i]=arr[i],arr[i-1]
                i-=1
    return arr

def quickSort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less=[i for i in arr[1:] if i<=pivot]
        greater=[i for i in arr[1:] if i>pivot]
        return quickSort(less)+[pivot]+quickSort(greater)


def selectionSort(arr):
    N=len(arr)
    for i in range(N):
        for j in range(i+1,N):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
from random import randint
def tester():
    xarr=[randint(-33443,34343) for i in range(700)]
    compare=xarr[:]
    compare.sort()
    SelectionSort=selectionSort(xarr[:])
    Bubblesort=bubblesort(xarr[:])
    Mergesort=mergesort(xarr[:])
    Quicksort=quickSort(xarr[:])
    Inserionsort=insertionSort(xarr[:])
    print("Selection sort Accepted" if SelectionSort==compare else "Not Accepted")
    print("Quick sort Accepted" if Quicksort==compare else "Not Accepted")
    print("Insertion sort Accepted" if Inserionsort==compare else "Not Accepted")
    print("Merge sort Accepted" if Mergesort==compare else "Not Accepted")
    print("Bubble sort Accepted" if Bubblesort==compare else "Not Accepted")
tester()
#create a list
arr=[i for i in range(1,100) if not i&1]
pass

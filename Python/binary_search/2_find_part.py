#내 코드
n=int(input())
exist=list(map(int,input().split()))
m=int(input())
want=list(map(int,input().split()))
exist.sort()
isExist=[]
def binary_search(array,target,start,end):
    mid = (start + end) // 2
    if(start>end):
        return False
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

for i in want:
    if binary_search(exist,i,0,n-1)!=False:
        isExist.append("yes")
    else:
        isExist.append("no")

for i in isExist:
    print(i,end=" ")
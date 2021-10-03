#내 코드
import numpy as np
n,m = map(int,input().split())
arr=np.array(list(map(int,input().split())))
arr.sort()
result=0
for i in range(max(arr),0,-1):
    temp_arr=np.array([i]*n)
    for_sum=np.where(arr-temp_arr<0,0,arr-temp_arr)
    temp_sum=sum(for_sum)
    if temp_sum==m:
        result=i
        break

print(result)
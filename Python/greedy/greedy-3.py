#내 풀이
'''import time
start_time=time.time()
n,k = map(int,input().split())
result=0
while n!=1:
    if n%k==0:
        n=n/k
        result+=1
    else:
        n-=1
        result+=1
print(result)
end_time=time.time()
print("time : ",end_time-start_time)'''
#답안 예시
n,k = map(int,input().split())
result=0
while True:
    target=(n//k)*k
    result+=(n-target)
    n=target
    if n<k:
        break
    result+=1
    n//=k
result+=(n-1)
print(result)
#내 풀이
n,m=map(int,input().split())
array=[]
maxofmin=0
for i in range(n):
    data=list(map(int,input().split()))
    data.sort()
    array.append(data)
    if maxofmin<data[0]:maxofmin=data[0]
print(maxofmin)
#py.min()함수를 이용하는 답안 예시
n,m=map(int,input().split())
#한 줄씩 입력받아 확인
result=0
for i in range(n):
    data=list(map(int,input().split()))
    #현재 행에서 가장 작은 수 찾기
    min_value=min(data)
    #가장 작은 수 중에서 가장 큰 수 찾기
    result=max(result,min_value)
print(result)
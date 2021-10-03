
n,m,k=map(int,input().split())
#n,m,k를 공백으로 구분하여 입력받기
data=list(map(int,input().split()))
#N개의 수를 공백으로 구분하여 입력받기
data.sort()
first=data[-1]
second=data[-2]
#가장 큰 수가 더해지는 횟수 계산
count=(m/(k+1))*k+m%(k+1)
print(count)
result=0
result+=count*first#가장 큰 수 더하기
result+=(m-count)*second#두 번째로 큰 수 더하기

print(result)
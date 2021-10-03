n=int(input())
k=list(map(int,input().split()))

result=[0]*len(k)
for i in range(len(k)):
    if i==0 or i==1:
        result[i]=k[i]
    else:
        result[i]=max(result[:i-1])+k[i]
print(max(result))
'''#답안 예시
#정수 N을 입력받기
n=int(input())
##모든 식량 정보 입력받기
array=list(map(int,input().split()))
#앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d=[0]*100

#다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0]=array[0]
d[1]=max(array[0],array[1])
for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+array[i])

#계산된 결과 출력
print(d[n-1])'''
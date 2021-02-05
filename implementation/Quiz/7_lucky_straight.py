#내 코드
n=list(input())
n_int = list(map(int, n))
left=sum(n_int[:len(n_int)//2])
right=sum(n_int[len(n_int)//2:])

if right==left:
    print('LUCKY')
else:
    print('READY')
'''답안 예시
n=input()
length=len(n)#점수값의 총 자릿수
summaary=0

#왼쪽 부분의 자릿수 합 더하기
for i in range(length//2)
    summary+=int(n[i])
#오른쪽 부분의 자릿수 합 빼기
for i in range(length//2,length):
    summary-=int(n[i])
    
#왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary==0:
    print("LUCKY")
else:
    print("READY")
'''
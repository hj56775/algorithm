#내 코드
n=int(input())
data=[]
for i in range(n):
    number=int(input())
    data.append(number)
data.sort()
data.reverse()
for i in data:
    print(i,end=' ')
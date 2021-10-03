''''#내 코드
n=input()
dirs=input().split()
x=1
y=1
for dir in dirs:
    if dir=='L':
        if y==1:
            continue
        else:
            y-=1
    elif dir=='R':
        if y==n:
            continue
        else:
            y+=1
    elif dir=='U':
        if x==1:
            continue
        else:
            x-=1
    elif dir=='D':
        if x==n:
            contine
        else:
            x+=1
print(x,y)'''
#답안 예시
n=int(input())
x,y=1,1
plans=input().split()

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]
            break
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y=nx,ny

print(x,y)
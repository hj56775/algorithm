n=int(input())
k=int(input())
board=[[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    row,col=map(int,input().split())
    board[row][col]=1
l=int(input())
data=[]
for _ in range(l):
    x,c=input().split()
    data.append((int(x),c))
dirs=[(-1,0),(0,-1),(1,0),(0,1)]#북,서,남,동
board[1][1]=-1
x,y=1,1
tail_x,tail_y=1,1
result=0
dir_idx=3
record=[]
while True:
    x+=dirs[dir_idx][0]
    y+=dirs[dir_idx][1]
    record.append(dirs[dir_idx])
    if x < 1 or y<1 or x>n or y>n or board[x][y]==-1:
        result += 1
        break
    if board[x][y]==1:
        board[x][y]=-1
    else :
        board[x][y] = -1
        board[tail_x][tail_y]=0
        tail_x+=record[0][0]
        tail_y+=record[0][1]
        del record[0]
    result += 1
    if data:
        if result==data[0][0]:
            if data[0][1]=='L':
                dir_idx=(dir_idx+1)%4
            else:
                dir_idx=(dir_idx-1)%4
            del data[0]
print(result)
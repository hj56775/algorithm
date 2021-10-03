from collections import deque

n,m = map(int,input().split())
maze=[]
for i in range(n):
    l=list(map(int,input()))
    maze.append(l)
dirs=[[1,0],[-1,0],[0,-1],[0,1]]

def bfs(maze,x,y):
    queue = deque()
    queue.append((x,y))
    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        x,y=queue.popleft()
        for dir in dirs:
            temp_x=x+dir[0]
            temp_y=y+dir[1]
            if temp_x<0 or temp_y<0 or temp_x>n-1 or temp_y>m-1:
                continue
            if maze[temp_x][temp_y]==0:
                continue
            if maze[temp_x][temp_y]==1:
                maze[temp_x][temp_y]=maze[x][y]+1
                queue.append((temp_x,temp_y))
    return maze[n-1][m-1]

print(bfs(maze,0,0))
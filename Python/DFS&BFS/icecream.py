
n,m = map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or y<=-1 or x>=n or y>=m:
        return False
    if l[x][y]==0:
        l[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

count=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            count+=1
print(count)

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


n,m= map(int,input().split())
graph=[]
for i in range(1,m+1):
    a,b,c=map(int,input().split())
    graph.append((a,b,c))
parent=[0]*(n+1)

for i in range(1,n+1):
    parent[i]=i

graph.sort(key=lambda x:x[2])

print(graph)
result=0
last=0

for edge in graph:
    a,b,cost=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union(parent,a,b)
        result+=cost
        last=cost

print(result-last)
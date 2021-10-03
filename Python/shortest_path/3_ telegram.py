#내 코드
import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)
n,m,c=map(int,input().split())
graph=[[] for _ in range(n)]
for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x-1].append((z,y-1))
distance=[INF]*n
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[0]
            if cost<distance[i[1]]:
                distance[i[1]]=cost
                heapq.heappush(q,(cost,i[1]))

dijkstra(c-1)

count=0
for i in distance:
    if i!=INF:
        count+=1
print(count-1,max(distance))

print(graph)
#https://programmers.co.kr/learn/courses/30/lessons/60059
def check(newlock):
    n=len(newlock)//3
    for i in range(n):
        for j in range(n):
            if newlock[n+i][n+j]!=1:
                return False
    return True
def solution(key, lock):
    rotate_keys=[]
    rotate_keys.append(key)
    for k in range(3):
        rotate_key=[[0]*len(key) for _ in range(len(lock))]
        for i in range(len(key)):
            for j in range(len(key)):
                rotate_key[i][j]=rotate_keys[k][len(key)-1-j][i]
        rotate_keys.append(rotate_key)
    n=len(lock)
    m=len(key)
    newlock=[[0]*(3*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            newlock[n+i][n+j]=lock[i][j]
    for rotate in rotate_keys:
        for i in range(n*2):
            for j in range(n*2):
                for x in range(m):
                    for y in range(m):
                        newlock[i+x][j+y]+=rotate[x][y]
                if check(newlock):
                    return True
                for x in range(m):
                    for y in range(m):
                        newlock[i+x][j+y]-=rotate[x][y]
    return False

#회전까지는 생각했지만 자물쇠의 크기를 3배 늘리는 아이디어를 떠올리지 못했음
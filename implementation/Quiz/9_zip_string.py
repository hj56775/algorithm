#내 코드
def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        arr=[]
        temp=1
        prev=s[:i]
        for j in range(i,len(s),i):
            if prev==s[j:j+i]:
                temp+=1
            else:
                if temp!=1:
                    arr.append(str(temp))
                arr.append(prev)
                prev=s[j:j+i]#리스트 범위를 넘어갈 경우 마지막까지 출력
                temp=1
        if temp!=1:
            arr.append(str(temp))
        arr.append(prev)
        answer=min(len(''.join(arr)),answer)
        print(answer)
    return answer
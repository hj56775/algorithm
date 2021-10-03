#내 코드
s=list(input())
alpha=[]
num=0
for i in s:
    if (ord(i)>=48 and ord(i)<=57):
        num+=int(i)
    else:
        alpha.append(i)
alpha.sort()
if num!=0:#숫자가 0이 아닌 경우에만 넣어줘어야 한다. 간과하지 말자.
    alpha.append(num)
for i in alpha:
    print(i,end='')

'''답안 예시
data=input()
result=[]
value=0

#문자를 하나씩 확인하며
for x in data:
    #알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    #숫자는 따로 더하기
    else:
        value+=int(x)

#알파벳을 오름차순으로 정렬
result.sort()

#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value !=0:
    result.append(str(value))
#최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))
'''
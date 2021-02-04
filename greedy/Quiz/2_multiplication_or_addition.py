#내 코드
import time

start=time.time()
data=input()
result=0
for i,num in enumerate(data):
    i_num=int(num)
    if i==0:
        continue
    elif i==1:
        a=int(data[i-1])
        b=int(data[i])
        if a<=1 or b<=1:#0 또는 1일 경우 더하는 게 유리
            result=a+b
        else:
            result=a*b
    else:
        a=int(data[i])
        if a<=1:
            result+=a
        else:
            result*=a
print(result)
end=time.time()
print(end-start)
'''답안 예제
import time
start=time.time()
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
end=time.time()
print(end-start)'''
#내 코드
n=int(input())
data=[]
for i in range(n):
    name,score=input().split()
    data.append([name,score])

def setting(data):
    return data[1]

results=sorted(data,key=setting)
for result in results:
    print(result[0],end=' ')

''''#답안 예시
n=int(input())
array=[]

#N명의 학생 정보를 입력받아 리스트에 저장
for i in range(n):
    input_data=input().split()
    #이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append(input_data[0],int(input_data[1]))

#key를 이용하야, 점수를 기준으로 정렬
array=sorted(array,key=lambda student:student[1])

#정렬이 수행된 결과를 출력
for student in  array:
    print(student[0],end=' ')
'''
#계수 정렬
def count_sort(array):#데이터의 개수 N, 최대값의 크기 K일 때 O(N+K)
    #모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
    count=[0]*(max(array)+1)
    temp_arr=[]
    for i in range(len(array)):
        count[array[i]]+=1#각 데이터에 해당하는 인덱스의 값 증가

    for i in range(len(count)):#리스트에 기록된 정렬 정보 확인
        for j in range(count[i]):
            temp_arr.append(i)
    return temp_arr

array=list(map(int,input().split()))
print(count_sort((array)))


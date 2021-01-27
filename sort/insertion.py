def insertion_sort(array):#평균적인 경우 O(n^2), but 거의 정렬되어 있는 경우 O(N)
    for i in range(1,len(array)):
        for j in range(i,0,-1):#인덱스 i부터 1까지 감소
            if array[j]<array[j-1]:#한칸씩 왼쪽으로 이동
                array[j],array[j-1]=array[j-1],array[j]
            else:#자기보다 작은 데이터를 만나면 break
                break
    return array

array=list(map(int,input().split()))
print(insertion_sort(array))
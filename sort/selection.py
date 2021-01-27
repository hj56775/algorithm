def selcetion_sort(array): #O(n^2)
    for i in range(len(array)):
        min_index=i #가장 작은 원소의 인덱스
        for j in range(i+1,len(array)):
            if array[min_index]>array[j]:
                min_index=j
        array[i],array[min_index]=array[min_index],array[i] #스와프
    return array

array=list(map(int,input().split()))
print(selcetion_sort(array))
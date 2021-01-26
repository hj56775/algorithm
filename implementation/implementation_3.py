#내 코드
'''pos=input()
col=pos[0]
real_row=int(pos[1])
count=0
cols=['a','b','c','d','e','f','g','h']
temp_col=cols.index(col)
dirs=['uur','uul','ddr','ddl','rru','rrd','llu','lld']
for dir in dirs:
    temp_col = cols.index(col)
    row=real_row
    if dir=='uur':
        temp_col+=1
        row+=-2
        if temp_col>len(cols)-1 or row<1:
            continue
        else:
            count+=1
    if dir=='uul':
        temp_col-=1
        row-=2
        if temp_col<0 or row<1:
            continue
        else:
            count+=1
    if dir=='ddr':
        temp_col+=1
        row+=2
        if temp_col>len(cols)-1 or row>8:
            continue
        else:
            count+=1
    if dir=='ddl':
        temp_col-=1
        row+=2
        if temp_col<0 or row>8:
            continue
        else:
            count+=1
    if dir=='rru':
        temp_col+=2
        row-=1
        if temp_col>len(cols)-1 or row<1:
            continue
        else:
            count+=1
    if dir=='rrd':
        temp_col+=2
        row+=1
        if temp_col>len(cols)-1 or row>8:
            continue
        else:
            count+=1
    if dir=='llu':
        temp_col-=2
        row-=1
        if temp_col<0 or row<1:
            continue
        else:
            count+=1
    if dir=='lld':
        temp_col-=2
        row+=1
        if temp_col<0 or row>8:
            continue
        else:
            count+=1
print(count)'''
#답안 예시
input_data=input()
row=int(input_data[1])
column=ord(input_data[0])-ord('a')+1#아스키코드로 변환후 +1
steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result=0
for step in steps:
    next_row=row+step[0]
    next_column=column+step[1]
    if next_row>=1 and next_row<=8 and next_column>=1 and next_row<=8:
        result+=1
print(result)
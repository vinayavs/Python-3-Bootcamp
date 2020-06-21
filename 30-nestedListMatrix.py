# PRINT NESTED LIST AS METRIX
l = [[10,20,30],[40,50,60],[70,80,90]]
for i in l:
    print(i) 
print('####ELEMENTS BY ROW WISE####')
for i in l:
    for j in i:
        print(j,end=' ')
    print()
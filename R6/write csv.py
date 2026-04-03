import csv
matrix=[[],[],[],[],[]]
for i in range(1,6):
    matrix[0].append(i)
for i in range(1,5):
    for j in range(0,4):
        matrix[i].append(matrix[i-1][j+1])
    matrix[i].append(matrix[i-1][0])
file=open('martix.csv','w')
writer=csv.writer(file)
writer.writerows(matrix)



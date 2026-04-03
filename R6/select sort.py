file=open('data.txt','r')
data=file.read()
file.close()
numbers=list(map(int,data.split(',')))
def Select_Sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
def EF_search(arr,n):
    mid=len(arr)//2
    while True:
        if arr[mid]==n:
            print(f"{arr[mid]}是第{mid+1}个数")
            break
        elif arr[mid]<n:
            mid=mid+1
        elif arr[mid]>n:
            mid=mid-1
Select_Sort(numbers)
num=int(input('输入一个数'))
position=EF_search(numbers,num)
print(numbers)
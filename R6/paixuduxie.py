file = open('data.txt', 'r')
data = file.read()
file.close()
numbers = list(map(int, data.split(',')))
def MP_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
MP_sort(numbers)
print(numbers)
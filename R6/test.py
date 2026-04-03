def selection_sort(arr):
    # 遍历所有数组元素
    for i in range(len(arr)):
        # 找到未排序部分的最小元素的索引
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 将找到的最小元素与未排序部分的第一个元素交换位置
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 示例
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
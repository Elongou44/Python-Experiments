n=int(input("请输入n："))
def weishu(num):
    qianwei = num // 1000
    baiwei = (num // 100) % 10
    shiwei = (num // 10) % 10
    gewei = num % 10
    return qianwei, baiwei, shiwei, gewei
result = []
if n==3:
    result = [num for num in range(100, 1000)
              if sum(weishu(num)[i]**3 for i in range(1,4))==num]
if n==4:
    result = [num for num in range(1000, 10000)
              if sum(weishu(num)[i]**4 for i in range(4))==num]
print(result)
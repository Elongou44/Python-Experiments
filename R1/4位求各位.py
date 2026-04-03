num = int(input("请输入一个四位整数: "))
qianwei = num // 1000        # 千位
baiwei = (num // 100) % 10   # 百位
shiwei = (num // 10) % 10    # 十位
gewei = num % 10             # 个位
# print("千位："+qianwei)
# print("百位："+baiwei)
# print("十位："+shiwei)
# print("个位："+gewei)   字符串不能与整数直接相加
print(f"千位：{qianwei}")
print(f"百位：{baiwei}")
print(f"十位：{shiwei}")
print(f"个位：{gewei}")
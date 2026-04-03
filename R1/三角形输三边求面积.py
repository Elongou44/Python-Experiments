import math
a = float(input("三角形的第一条边: "))
b = float(input("三角形的第二条边: "))
c = float(input("三角形的第三条边: "))
s = (a + b + c) / 2
s = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"三角形的面积: {s}")
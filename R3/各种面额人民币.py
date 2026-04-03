sum=[(ten,five,one)
     for ten in range(11)
     for five in range(51)
     for one in range(101)
     if ten*10+five*5+one==100]
for ten,five,one in sum:
    print(f'10元：{ten}张  5元：{five}张  1元：{one}张')

print('='*25+'开始下载'+"="*25)
for i in range(0,51) :
    num=i*2
    star=i
    point=50-star
    print("{}%[{}{}]".format(num,star*'*',point*'.'))
print('='*25+'下载完成'+"="*25)

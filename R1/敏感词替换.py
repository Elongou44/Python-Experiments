word='很;不'
newwords=word.split(';')
str=input("输入语句：")
for w in newwords:
    if w in str:
        str=str.replace(w,'*'*len(w))
print(str)
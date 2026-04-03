MAP={
    'a':{'b','f','d'},
    'b':{'e','f'},
    'c':{'d','e'},
    'd':{'e'},
    'e':{'f'},
    'f':{'c','g','h'},
    'g':{'f','h','i'},
    'h':{'f','g','i'},
    'i':{'h'}
}
node=input("请输入节点:")
if node not in MAP:
    print('节点不存在')
else:
    in_node=sum(1 for i in MAP.values() if node in i)#入度
    out_node=len(MAP[node])#出度
print(f'{node}结点的入度为：{in_node}，出度为：{out_node}，分别如下：')
for i in MAP[node]:
    print(f"{node} >> {i}")
incoming = [key for key, value in MAP.items() if node in value]
for key in incoming:
    print(f"{key} >> {node}")

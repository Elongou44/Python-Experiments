i=1
root=input("输入用户名：")
while(i<4):
    if(root!='XX'):
        if i == 3:
            print("3次用户或密码都输入错误，程序结束。")
            break
        root=input("用户名输入错误，请重新输入：")
        i+=1
    else:
        password = input("请输入密码：")
        while(i<4):
            if (password != '666'):
                if i == 3:
                    print("3次用户或密码都输入错误，程序结束。")
                    break
                password = input("密码输入错误，请重新输入:")
                i += 1
            else:
                print('登录成功')
                break
        break


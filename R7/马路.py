import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\SimSun.ttc')
plt.legend(prop=myfont)
df=pd.DataFrame({'男':(450,800,200),'女':(150,100,300)})
df.plot(kind='bar',color=['red','blue'])
plt.xticks([0,1,2],['从不闯红灯灯','跟别人闯红灯','带头闯红灯'],color='blue',fontproperties=myfont)
plt.yticks(list(df['男'].values)+list(df['女'].values))
plt.ylabel('人数',fontproperlies=myfont,fontsize=14)
plt.title('集体过马路方式',fontproperties=myfont,fontsize=20)
plt.show()
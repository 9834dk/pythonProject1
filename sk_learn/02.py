import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='C:/Windows/Fonts/SimHei.ttf')

a_area=[10,20,40]
a_y=[0,0,0]

b_area=[100,200]
b_y=[0,0]

plt.scatter(a_area,a_y,label='A',color='r')
plt.scatter(b_area,b_y,label='B',color='g')
plt.vlines(50,ymin=-0.015,ymax=0.015,color='gray',linestyles='--')
plt.xlabel('房子面积',fontproperties=font,fontsize=15)
plt.ylabel('分类问题',fontproperties=font,fontsize=20)
plt.legend()
plt.show()

# 特征（feature）：描述一件事物的特性，如一个人的身高、体重、年龄和五官。
# 样本（sample）：由一个人的特征组成的数据，如{180，60，19，精致}
# 标记（label）：描述一件事物的特性，如一个人帅或丑、一个人的财富数量，特征和标记没有明确的划分，
# 由于问题的不同可能导致A问题的特征是B问题的标记，B问题的标记是A问题的特征。
# 样例（example）：由一个人的特征和标记组成的数据，如
# 特征空间（feature space）：由{x1,x2,xn}n个特征张成的n维空间
# 这n个特征张成的n维空间，如以身高张成的一维空间（线）；以身高和体重张成的二维空间（面）；以身高、
# 体重和年龄张成的三维空间（体）。
# 特征向量（feature vector）：特征空间内的某一个具体的向量，即特种空间中的某一个具体的点，
# 表示第m个人的第n个特征。如身高、体重、年龄张成的三维空间中的某一个具体的点
#监督学习分为回归问题（连续数据2，2，2，4，5，6）和分类问题（0，1，0，1的离散值输出不是1就是0），
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# %matplotlib inline
font=FontProperties(fname='C:/Windows/Fonts/SimHei.ttf')
x=np.linspace(0,200,10)
y=10*x
plt.plot(x,y)
plt.xlabel('房子面积',fontproperties=font,fontsize=15)
plt.ylabel('房价',fontproperties=font,fontsize=15)
plt.title('回归问题')
plt.show()



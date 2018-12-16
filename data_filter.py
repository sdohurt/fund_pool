## 策略
# 1.四分位法筛选3年、2年、1年业绩都排名1/4的基金；
# 2.规模适中（20至100亿）
# 3.基金经理工作年限较久（从事证券相关工作和直接管理基金的两个角度；最好工作时间大于3年）


import pandas as pd
import numpy as np

fileName = '基金数据情况-2018-11-06'
f = open('./{}.csv'.format(fileName))
# f = open('./test.csv')
data = pd.read_csv(f)

data.近3年增幅 = data.近3年增幅.replace('--', np.nan)
data = data.dropna(axis=0,how='any')

data.基金规模 = data.基金规模.str.extract('(\d+\.?\d*)', expand=False)
data['基金规模'] = data['基金规模'].apply(pd.to_numeric, errors='coerce')
data = data[data.基金规模 > 5]

for i in ['近3月排名', '近1年排名', '近2年排名', '近3年排名']:
    data[i + '系数'] = data[i].str.split('|').map(lambda x: int(x[0])/int(x[1]))
    data = data[data[i+'系数'] < 1/4]

data.to_csv('./{}{}.csv'.format(fileName, '-筛选后版本'))
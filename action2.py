from pandas import DataFrame
#输入成绩
data = {'语文':[68,95,98,90,80],'数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}
df1 = DataFrame(data)
df2 = DataFrame(data,index=['张飞','关羽','刘备','典韦','许褚'],columns=['语文','数学','英语'])
temp = df2[['语文','数学','英语']]
#计算最大最小值，平均值，方差，标准差，和，排序
df2['max'] = temp.max(axis = 1)
df2['min'] = temp.min(axis = 1)
df2['mean'] = temp.mean(axis = 1)
df2['var'] = temp.var(axis = 1)
df2['std'] = temp.std(axis = 1)
df2['sum'] = temp.sum(axis = 1)

print(df2)
print(df2['sum'].sort_values(ascending=False))







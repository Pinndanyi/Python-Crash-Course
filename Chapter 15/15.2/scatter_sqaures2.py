import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

#要指定自定义颜色，可传递参数c ，并将其设置为一个元组，其中包含三个0~1之间的小数值，它们分别表示红色、绿色和蓝色分量。
plt.scatter(x_values, y_values, c = (0.4, 0.2, 0.2), edgecolor = 'none', s = 20)
plt.title("Squares of Numbers", fontsize = 24)
plt.xlabel("Values", fontsize = 14)
plt.ylabel("Square of values", fontsize= 14)

#设置每个坐标的取值范围
#将 x 坐标轴的取值范围设置为0~1100，并将 y 坐标轴的取值范围设置为0~1 100 000
plt.axis([0, 1100, 0, 1100000])
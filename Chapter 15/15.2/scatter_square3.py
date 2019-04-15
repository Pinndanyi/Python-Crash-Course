import matplotlib.pyplot as plt

x_values = list(range(10001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, 
            edgecolor = 'none', s = 40)

plt.title("Squares of Numbers", fontsize = 24)
plt.xlabel("Values", fontsize = 14)
plt.ylabel("Square of values", fontsize= 14)  

#第二个实参指定将图表多余的空白区域裁剪掉
plt.savefig('square_plot.png')  
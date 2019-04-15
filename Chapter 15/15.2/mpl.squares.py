import matplotlib.pyplot as plt

input_values = list(range(1,6))
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth = 5)

plt.title("Square nNumbers", fontsiz = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

#设置标记刻度的大小
plt.tick_params(axis = 'both', labelsize = 14)

plt.show()

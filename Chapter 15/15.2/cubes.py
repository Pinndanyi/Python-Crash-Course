import matplotlib.pyplot as plt

x_values = list(range(5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, linewidth = 3, c = y_values,
            cmap = plt.cm.rainbow)

plt.title("The cube of numbers",fontsize = 15)
plt.xlabel("Values")
plt.ylabel("Cube of the value.")    

    

    


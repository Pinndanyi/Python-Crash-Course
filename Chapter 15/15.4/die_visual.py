import pygal
from die import Die

die = Die()

#投掷几次骰子，讲结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
frequencies = []
for i in range (1, die.num_sides+1):
    frequency = results.count(i)
    frequencies.append(frequency)
    
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
   
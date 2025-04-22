import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [30, 25, 25, 20]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Simple Pie Chart")
plt.show()

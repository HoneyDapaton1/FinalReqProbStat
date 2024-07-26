import matplotlib.pyplot as plt

data = {'IT1': 3.0, 'IT2': 1.25, 'IT3': 1.00, 'IT4': 2.75}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)

# Plotting each type of chart on its respective subplot
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)

# Adding a title to the entire figure
fig.suptitle('Categorical Plotting')

# Displaying the plots
plt.show()
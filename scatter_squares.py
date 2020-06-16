import matplotlib.pyplot as plt

plt.scatter(2, 4, s=200)

# name of the diagram
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Fonts
plt.tick_params(axis='both', labelsize=14)

plt.show()
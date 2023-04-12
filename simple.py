import numpy as np
import matplotlib.pyplot as plt
from data_creator import input_data


plt.style.use('ggplot')

num_categories = int(input("Enter the number of categories: "))

# categories = []
# for i in range(num_categories):
#     categories.append(input(f"Enter category {i+1}: "))

num_observers = int(input("Enter the number of observations: "))

data = categories, data = input_data(num_categories, num_observers, 0, 100)






angles=np.linspace(0,2*np.pi,num_categories, endpoint=False)
print(angles)

angles=np.concatenate((angles,[angles[0]]))
print(angles)

# HARDCOED FOR NOW DON'T JUDGE

categories.append(categories[0])
data["Ankkit"].append(data["Ankkit"][0])




fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(polar=True)#basic plot
ax.plot(angles,data["Ankkit"], 'o--', color='g', label='Ankkit')
#fill plot
ax.fill(angles, data["Ankkit"], alpha=0.25, color='g')
#Add labels
ax.set_thetagrids(angles * 180/np.pi, categories)
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
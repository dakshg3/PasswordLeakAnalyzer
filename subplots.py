import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

slices_hours = [4, 8]
colors = ['r', 'y', 'g', 'b','r', 'y', 'g', 'b','r', 'y', 'g', 'b'] 
labels = ["Yes","No"]

fig = plt.figure(figsize=(18,9))
j=0
lis= [[1,1],[2,3],[4,7],[12,2]]
for i in lis:
	j = j+1
	ax1 = fig.add_subplot(4,2,j)
	plt.pie(i, labels = labels,colors=colors,  startangle=90, shadow = True, explode = (0, 0.1), radius = 1.2, autopct = '%1.1f%%')


plt.legend() 
plt.show()


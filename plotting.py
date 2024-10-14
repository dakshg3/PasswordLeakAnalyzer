import pymongo
import re
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["test"]
mycol = mydb["test_con"]

lower=0
upper=0
spec=0
numbers=0
letteronly=0
numberonly=0
symbolonly=0
allthree=0
score=0
weak=0
normal=0
strong=0

string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')

mydoc = mycol.find({},{"pass":1,"_id":0})
for x in mydoc:
	x = str(x).split("'")
	data = x[3]

	l=False
	u=False
	n=False
	s=False
	score=0

	for c in data:
		if(c.islower()):
			l=True
		if(c.isupper()):
			u=True
		if(c.isdigit()):
			n=True
		if(string_check.search(data) is not None):
			s=True


	if(l):
		lower = lower + 1

	if(u):
		upper = upper + 1

	if(n):
		numbers = numbers + 1

	if(s):
		spec = spec + 1
		score = score + 5

	if((l or u) and n):
		score = score + 10

	if(l and u):
		score = score + 10	

	if(len(data)>8):
		score = score + 5	

	if((l==True or u==True) and n==True and s==True):
		allthree = allthree + 1
	
	if(l==True or u==True and n==False and s==False):
		letteronly = letteronly + 1

	if(l==False and u==False and n==True and s==False):
		numberonly = numberonly + 1

	if(l==False and u==False and n==False and s==True):
		symbolonly = symbolonly + 1


	if(score >= 20):
		strong = strong + 1
	elif(score>=10 and score<20):
		normal = normal + 1
	else:
		weak = weak + 1


total = mycol.count()
print("Total Passwords: ", total)
print("Lower Case Exists: ", lower)
print("Upper Case Exists: ", upper)
print("Digit Exists: ", numbers)
print("Special Character Exists: ", spec)
print("All Three Exists: ", allthree)
print("Number Only: ", numberonly)
print("Letter Only: ", letteronly)
print("Symbol Only: ", symbolonly)
print("Weak Passwords: ", weak)
print("Normal Passwords: ", normal)
print("Strong Passwords: ", strong)

labels = ["Yes","No"]
labs = []
colors = ['b', 'y', 'g', 'r'] 
range = (0, total) 
bins = 10

lis=[[lower,total],[upper,total],[numbers,total],[spec,total],[allthree,total],[numberonly,total],[letteronly,total],[symbolonly,total]]
title=["LowerCase","UpperCase","Digits","Special Characters","All Three","Number Only","Letter Only","Symbol Only"]
fig = plt.figure("Pie Charts",figsize=(15,12))
j=0
for i in lis:
	j = j+1
	ax1 = fig.add_subplot(2,4,j)
	plt.pie(i, labels = labels,colors=colors,  startangle=90, shadow = True, explode = (0, 0.1), radius = 1.2, autopct = '%1.1f%%')
	plt.title(title[j-1])


plt.figure("Bar Graph 1")
objects=["LowerCase","UpperCase","Digits","Special Characters"]
y_pos = np.arange(len(objects))
performance=[lower,upper,numbers,spec]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('No. of Passwords')
plt.title('Bar Graph 1')


plt.figure("Bar Graph 2")
objects=["Letters Only","Numbers Only","Special Characters Only","All Three"]
y_pos = np.arange(len(objects))
performance=[letteronly,numberonly,symbolonly,allthree]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('No. of Passwords')
plt.title('Bar Graph 2')

plt.figure("Bar Graph 3")
objects=["Strong","Normal","Weak"]
y_pos = np.arange(len(objects))
performance=[strong,normal,weak]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('No. of Passwords')
plt.title('Strength of Passwords')


plt.legend() 
plt.show()



'''
plt.figure("LowerCase")
plt.pie([lower,total], labels = labels,colors=colors,  
        startangle=90, shadow = True, explode = (0, 0.1), 
        radius = 1.2, autopct = '%1.1f%%')

plt.figure("UpperCase")
plt.pie([upper,total], labels = labels,colors=colors,  
        startangle=90, shadow = True, explode = (0, 0.1), 
        radius = 1.2, autopct = '%1.1f%%')

plt.figure("Has Numbers")
plt.pie([numbers,total], labels = labels,colors=colors,  
        startangle=90, shadow = True, explode = (0, 0.1), 
        radius = 1.2, autopct = '%1.1f%%')

plt.figure("Special Characters")
plt.pie([spec,total], labels = labels,colors=colors,  
        startangle=90, shadow = True, explode = (0, 0.1), 
        radius = 1.2, autopct = '%1.1f%%')

plt.figure("Letters Only")
plt.pie([letteronly,total], labels = labels,colors=colors,  
        startangle=90, shadow = True, explode = (0, 0.1), 
        radius = 1.2, autopct = '%1.1f%%')

plt.figure("Special Characters Only")
plt.pie([symbolonly,total], labels = labels,colors=colors,  
        startangle=90, shadow = True, explode = (0, 0.1), 
        radius = 1.2, autopct = '%1.1f%%')

plt.figure("Number Only")
plt.pie([numberonly,total], labels = labels,colors=colors,  
        startangle=90, shadow = True, explode = (0, 0.1), 
        radius = 1.2, autopct = '%1.1f%%')

plt.figure("All Three")
plt.pie([allthree,total], labels = labels,colors=colors,  
        startangle=90, shadow = True, explode = (0, 0.1), 
        radius = 1.2, autopct = '%1.1f%%')
'''



'''
STRENGTH CRITERIA : 

The password is at least 8 characters long.			+5 pts
The password contains number and letters.			+10 pts
The password contains at least one punctuation sign.		+5 pts
The password contains lowercase and uppercase characters.	+10 pts

'''





"""
Data Visualisation
"""
import matplotlib.pyplot as plt


data = {
    "Argentina": 31118074,
    "India": 391255067,
    "Japan": 119039541,
    "South Africa": 3024355,
    "United Kingdom": 62351648,
    "United States": 245425910
}


# because we are plotting a BarChart we will put x and y in a list
#Independent Variavle (x-axis)

x = list(data.keys())

#Dependent variable (y-axis)

y = list(data.values())

#Figure Margins
fig = plt.figure(figsize = (10,5))

#Plotting our bar graph
plt.bar(x,y, color = 'green', width = 0.2)
plt.show()



#Independent Variavle (x-axis)

u = data.keys()

#Dependent variable (y-axis)

v = data.values()

plt.scatter(u,v, color='red')
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:59:34 2020

@author: Kunj
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:51:19 2020

@author: Kunj
"""


import matplotlib.pyplot as plt 

# Prabhu " path " pradashit karo yahan bhi.

a=open(r'D:\detection\vehicles_info\lane1.txt',"r")
b=open(r'D:\detection\vehicles_info\lane2.txt',"r")
c=open(r'D:\detection\vehicles_info\lane3.txt',"r")
d=open(r'D:\detection\vehicles_info\lane4.txt',"r")

def summation(fname):
		sum=0
		x=0
		with open(fname,"r") as myfile:
			for line in myfile:
				 if(x==int(line)):
					 sum=sum + 0
				 else:
					  sum=sum+int(line)
						
				 x=int(line)
				 
		return(sum)

'''The Bar graph below show the results of average traffic density on  busy cross roads.
Write a report for district traffic office, describing the information shown below.
You should write at least 150 words.
'''

# x-coordinates of left sides of bars  
left = [1, 2, 3, 4] 
  
# heights of bars 
height = [summation(r'D:\detection\vehicles_info\lane1.txt'), summation(r'D:\detection\vehicles_info\lane2.txt'), summation(r'D:\detection\vehicles_info\lane3.txt'), summation(r'D:\detection\vehicles_info\lane4.txt')]  
  
# labels for bars 
tick_label = ['lane-1', 'lane-2', 'lane-3', 'lane-4'] 
  
# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
        width = 0.8, color = ['red', 'blue','green','orange']) 
  
# naming the x-axis 
plt.xlabel('Lanes') 
# naming the y-axis 
plt.ylabel('No. Of Vehicles') 
# plot title 
plt.title('vehicle analysis chart!') 
a.close()
b.close()
c.close()
d.close()
  
# function to show the plot 
plt.show() 

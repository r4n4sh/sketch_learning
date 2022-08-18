import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import os
import re
from math import pow
from collections import defaultdict
import statistics

dictRand= defaultdict(string)
#dictShift= defaultdict(int)


Batch,LFU,LRU,Hyperbolic,ARC,Caffeine
0,7640,6966,7349,6988,7500



window = 10000

with open('parsed-gradle.csv') as f:
	data = f.read()
	tuple=re.findall(r'trace size = *(\d+)\, exact = *\d+\, estimated = *\d+\, MSRE = (\d+\.?\d*)',data)
	tuple=re.findall(r'*(\d+)\,*(\d+)\,*(\d+)\,*(\d+)\,*(\d+)\,*(\d+)\',data)



tuple=[float(i)/window for i in tuple]

#with open('shift_w_100k.csv') as f1:
#  data1 = f1.read()
#  #msre=re.findall(r'trace size = *\d+\, exact = *\d+\, estimated = *\d+\, MSRE = (\d+\.?\d*)',data)
#  tupleshift=re.findall(r'trace size = *(\d+)\, exact = *\d+\, estimated = *\d+\, MSRE = (\d+\.?\d*)',data1)


for t in tuple:      
  e=float(t[1])
    dictRand[e]+=1


for t in tupleshift:      
  e=float(t[1])
  if e ==1:
    dictShift[0]+=1
  else:
    dictShift[e]+=1

#for e in msre:
#	if e ==1:
#		dict[0]+=1
#	else:
#		dict[e]+=1

labels = ['LFU','LRU', 'Hyperbolic', 'ARC', 'AW-TinyLFU']
scala =[0,0.001,0.01,0.1,1,10]	
histogramRand=[0,0,0,0,0,0]
keylistRand = dictRand.keys()
for e in sorted(keylistRand):
	for i in range(0,len(scala)):
		if e<=scala[i] and (i==0 or e > scala[i-1] ):
			histogramRand[i]+=dictRand[e]


histogramShift=[0,0,0,0,0,0]
keylistShift = dictShift.keys()
for e in sorted(keylistShift):
  for i in range(0,len(scala)):
    if e<=scala[i] and (i==0 or e > scala[i-1] ):
      histogramShift[i]+=dictShift[e]

fig, ax = plt.subplots()
x = np.arange(len(labels)) 


barWidth = 0.25
r1 = x
r2 = [k + barWidth for k in r1]


histogramShift =   [135827, 145, 1754, 3803, 20925, 314]
histogramRand =   [164456, 114, 950, 3966, 16656, 174]


ax.set_xlabel('Length', fontsize=36)
ax.set_ylabel('Hit Raio',fontsize=36)
ax.set_xticks(x)
ax.set_xticklabels(labels)
rects1 =ax.bar(r1,histogramRand,color='darkcyan', width=0.2, edgecolor='white',align= 'edge', label='RAND')


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    i=0
    for rect in rects:
        if i==0:
               #height = rect.get_height()
               #ax.annotate('{}'.format(int(height)),
               #				xy=(rect.get_x() + rect.get_width()*1.7+0.0001 , height),
               #				xytext=(0, 3),  # 3 points vertical offset
               #				textcoords="offset points",
               #				ha='center', va='bottom', fontsize=30)
        		a=5		
        elif i==5:
                height = rect.get_height()
                ax.annotate('{}'.format(int(height)),
                				xy=(rect.get_x()-0.01 , height),
                				xytext=(0, 3),  # 3 points vertical offset
                				textcoords="offset points",
                				ha='center', va='bottom', fontsize=30)	
        else:
                height = rect.get_height()
                ax.annotate('{}'.format(int(height)),
                			xy=(rect.get_x() + rect.get_width() / 2, height),
                			xytext=(0, 3),  # 3 points vertical offset
                			textcoords="offset points",
                			ha='center', va='bottom', fontsize=30)			
        i+=1;


#autolabel(rects1)
print("RAND: ", histogramRand)
print("SHIFT: ", histogramShift)

plt.legend(loc="best",prop={'size':13},ncol=15) # keys of the graphs
fig.tight_layout()
plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))	
plt.rcParams.update({'font.size': 30})

plt.savefig('policiesHist.png')

#plt.show()

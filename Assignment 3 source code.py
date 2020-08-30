#Guys, the level of the problem i took is 'Hardest' one.

# Use the following data for this assignment:

import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])


import matplotlib.pyplot as plt
%matplotlib notebook

xcoods=[1992,1993,1994,1995]
yco=[np.array(df.iloc[i]) for i in range(4)]
ycoods=[np.mean(x) for x in yco]
yerr=[(np.max(x)-np.min(x))/250 for x in yco]
colors=['b','y','c','lime']
plt.bar(xcoods,ycoods,width=1,yerr=yerr,color= colors,alpha =0.5,edgecolor='k')

plt.xticks([1991.5,1992,1992.5,1993,1993.5,1994,1994.5,1995,1995.5],['','1992','','1993','','1994','','1995',''])
plt.tick_params(axis = 'x', which='both',top=False,bottom =False)
#plt.gca().spines['top'].set_visible(False)
#plt.gca().spines['right'].set_visible(False)


def onhover(event):
    plt.cla()
    plt.title(event.ydata)
    bars=plt.bar(xcoods,ycoods,width=1,yerr=yerr,color= colors,alpha =0.5,edgecolor='k')
    dt=event.ydata
    
    listcol=['lemonchiffon','papayawhip','navajowhite','burlywood','salmon','tomato','red','firebrick','darkred']
    for i in range(4):
        s1=set(list(np.arange(int(ycoods[i]-yerr[i]),int(ycoods[i]+yerr[i]))))
        s2=set(list(np.arange((event.ydata-2987)//1,(event.ydata+2987)//1)))
        x=  len(list(s1.intersection(s2)))/min([2*yerr[i],5974])
    
        if x==1:
            k=-1
        else:
            k=(x*10)//1
        
        bars[i].set_color(listcol[int(k)])
    
    i=0
    
    plt.xticks([1991.5,1992,1992.5,1993,1993.5,1994,1994.5,1995,1995.5],['','1992','','1993','','1994','','1995',''])
    plt.tick_params(axis = 'x', which='both',top=False,bottom =False)
    #plt.gca().spines['top'].set_visible(False)
    #plt.gca().spines['right'].set_visible(False)
    
    
    plt.plot(list(range(1991,1997)),[dt+2987]*(len(list(range(1991,1997)))),'g-')
    plt.plot(list(range(1991,1997)),[dt-2987]*(len(list(range(1991,1997)))),'g-')
    
    plt.gca().fill_between(list(range(1991,1997)),[dt-2987]*len(list(range(1991,1997))),[dt+2987]*len(list(range(1991,1997))),facecolor='k',alpha=0.2)
    plt.text(1991,dt+2987,str((dt+2987)//1))
    plt.text(1991,dt-4307,str((dt-2987)//1))
    
plt.gcf().canvas.mpl_connect('motion_notify_event',onhover)

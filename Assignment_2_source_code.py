# Guys, Assignment 2 is similar for everyone but data is different, Data I was given was in Ann Arbor, Michigan, United States
# if you are given different data just change that file path in the 9th line of this code.
#just copy paste this code in the jupyter notebook and run that to get the pic, that I uploaded

#Sorting out the required Data

import numpy as np
import pandas as pd
df= pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')

df=df.sort_values('Date')

df=df.drop('ID',axis =1)
df=df.set_index('Date')

df.head(30)
l=[]

dff=pd.DataFrame()
d=pd.DataFrame()
for x in np.arange('2005-01-01' , '2016-01-01',dtype = 'datetime64[D]'):
    d=df.loc[str(x)]
    d=d.sort_values('Data_Value')
    l.append({'Day':x,'TMIN':d['Data_Value'].iloc[0],'TMAX':d['Data_Value'].iloc[-1]})    
    
dff = pd.DataFrame(l)

l=[]
for x in np.arange('2005-01-01' , '2016-01-01',dtype = 'datetime64[D]'):
    x=str(x.astype('datetime64[D]'))
    l.append(x[5:])
    
dff['Days'] = l


dff=dff[dff.Day !='2008-02-29']
dff=dff[dff.Day !='2012-02-29']

dff.drop('Day',axis = 1)


df15=dff.iloc[-365::1]
df15.head(20)

#Seperating the data of the year 2015 to find the extremes in the period of 2005-14

dff=dff.iloc[:3650] 

dff=dff.set_index('Days')

l=[]
d=pd.DataFrame()
e=pd.DataFrame()
for x in dff.index[:365]:
    d=dff.loc[str(x)]
    e=dff.loc[str(x)]
    d=d.sort_values('TMIN')
    e=e.sort_values('TMAX')
    l.append({'Days':x,'TMIN':d['TMIN'].iloc[0],'TMAX':e['TMAX'].iloc[-1]})
    
#thus, the data frame 'df' contains the maximum and minimum temperatures of each day from the year 2005-14
df=pd.DataFrame(l)
df=df[:365]

if 'Day' in df.columns:
    df15 = df15.drop('Day',axis = 1)

#'df15' contains temperatures of each day in the year 2015
df15=df15.set_index('Days')
df15=df15.reset_index()

maxl=[]
minl=[]

for x in df.index:
    if(df15.loc[x]['TMAX'] > df.loc[x]['TMAX'] ):
        maxl.append(df15.loc[x]['TMAX'])
    else:
        maxl.append(None)
    
for x in df.index:
    if (df15.loc[x]['TMIN'] < df.loc[x]['TMIN']):
        minl.append(df15.loc[x]['TMIN'])
    else:
        minl.append(None)

#maxl list conatins the max temperatre, where the record was broken
#minl list conatins the min temperatre, where the record was broken


#Here goes the code for plotting the graph

%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
fig, ax = plt.subplots()

right = ax.spines["right"]
top = ax.spines["top"]
right.set_visible(False)
top.set_visible(False)
a=np.array(df['Days'])
b=list(df['TMIN'])

c=np.array(df['TMAX'])

month=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
plt.plot(b,'b-',label= 'Record Least Temp (2005 - 2014) ')
plt.plot(c,'g-',label= 'Record High Temp (2005 - 2014) ')


plt.gca().fill_between(range(len(df15)),b,c,facecolor='k',alpha=0.12)

maxl15=np.array(maxl)
minl15=np.array(minl)
dates = np.array(df['Days'])

plt.scatter(range(0,365),maxl15,c='orange',s=10,label = 'Record Breaking High Temp in 2015')
plt.scatter(range(0,365),minl15,c='red',s=10,label = 'Record Breaking Lest Temp in 2015')
#plt.xticks(month)

ax=plt.gca()
ax.set(xlim=(1, 365), ylim=(-370, 430))

plt.tick_params(top ='off',bottom = 'on',left='on', right = 'off',labelleft = 'on', labelbottom='on')

plt.ylabel('Temp in tenths of degree in C', fontsize='large')
plt.xlabel('Days of the year distributed over months',fontsize='large')
plt.title('Temperature distribution over the days of the years from 2005-2015')

l=[(365//12)*i +1 for i in range(12)]

plt.xticks(l,month)

plt.legend(loc = 0,frameon=False )


# File: ads_stats.py
#  Cre: 2014-07-06
#
# Analyses data downloaded by download_ads_data.py.  Tells you how
# many people wrote x papers in 2013.  Run in ipython for best
# results.

import pickle
from pandas import Series 
import pandas as pd
import re 
import numpy as np 
import matplotlib.pyplot as plt

pd.options.display.mpl_style = 'default'

with open("ads_data.dat","rb") as f:
    data = pickle.load(f)

data1 = data.split("Authors")

hook2 = "Affiliation"
data2 = [] 
for x in data1: 
    if hook2 in x:
        n = x.find(hook2)
        data2.append(x[:n])

sep = " "
all_authors = sep.join(data2)
aa2 = all_authors.split("\n")
aa3 = [x.strip() for x in aa2]
aa4 = [x.strip(":") for x in aa3]
aa5 = [x.strip() for x in aa4]

aa = aa5[0]+";"
for x in aa5[1:]:
    if (x!=''):
        if (x[-1] != ";"):
            aa += (x+";")
        else:
            aa += x 

aa6 = [x.strip() for x in aa.split(";")] 

obj = Series(aa6)
obj2 = obj.value_counts()
obj3 = obj2.values

fig, ax = plt.subplots()
ax.grid(False, which="minor") 
ax.grid(False, which="majorminor") 
obj2.hist(ax=ax,bins=20,bottom=0.1,grid=None,xlabelsize=15.0,ylabelsize=15.0)
ax.set_yscale('log')
plt.xlabel('Number of refereed publications in 2013')


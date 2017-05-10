
# coding: utf-8

# In[19]:

import pandas as pd

dat = pd.read_csv("2015_City.csv", skiprows = 4, encoding = 'iso-8859-1')


# In[20]:

dat.head()


# In[21]:

from matplotlib import pyplot as plt
plt.style.use('ggplot')


# In[22]:

plt.hist(dat["Total Wages"], bins = 50)
plt.xlabel("Wages")
plt.ylabel("LOVE")
plt.show()


# In[23]:

dat.sort_values(by="Total Wages", ascending=False)["Total Wages"].head()


# In[24]:

# remove the rows with total wages <= 0

new_dat = dat.loc[dat["Total Wages"] >= 18000]


# In[25]:

new_dat.sort_values(by="Total Wages", ascending=True)["Total Wages"].head(15)


# In[26]:

len(new_dat), len(dat)


# In[27]:

float(len(new_dat))/float(len(dat)) # removed 30% of our data! :O


# In[28]:

plt.hist(new_dat["Total Wages"], bins = 20)
plt.xlabel("Wages")
plt.ylabel("LOVE")
plt.title("Full Time Workers")
plt.show()


# In[30]:

dat = pd.read_csv("2015_City.csv", skiprows = 4, encoding = 'iso-8859-1')

fnames = ["2009_City.csv","2010_City.csv","2011_City.csv", "2012_City.csv", "2013_City.csv", "2014_City.csv", "2015_City.csv"]


bigass_df = pd.DataFrame()
li = []

for f in fnames:
    df = pd.read_csv(f, skiprows = 4, usecols = ["Year", "Total Wages"])
    li.append(df)

bigass_df = pd.concat(li)

bigass_df.head()


# In[41]:

from ggplot import *

myplot = (ggplot(aes(x = "Total Wages", color = "Year"), data = bigass_df)       +  geom_density(alpha = 0.2))

print(myplot)

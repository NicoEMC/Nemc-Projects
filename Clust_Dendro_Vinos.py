#!/usr/bin/env python
# coding: utf-8

# ## Clustering con Python
# 

# In[2]:


get_ipython().run_line_magic('config', 'IPCompleter.greedy=True')
import pandas as pd 
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv("C://Users/nicol/Desktop/Nueva Carpeta/data science/python-ml-course-master/datasets/wine/winequality-red.csv", sep = ";")
df.head()


# In[7]:


df.shape


# In[8]:


plt.hist(df["quality"])


# In[10]:


df.groupby("quality").mean()


# ### Normalización de los datos

# In[11]:


df_norm = (df-df.min())/(df.max()-df.min())
df_norm.head()     ### se normaliza para que todos los datos tengan el mismo peso, quedan en relación [0,1]


# ### Clustering jerárquico con scikit-learn

# In[13]:


from sklearn.cluster import AgglomerativeClustering as AgC


# In[14]:


clus = AgC(n_clusters= 6, linkage="ward").fit(df_norm)


# In[30]:


md_h = pd.Series(clus.labels_)
md_h


# In[31]:


plt.hist(md_h)
plt.title("Histograma de los Clusters")
plt.xlabel("Cluster")
plt.ylabel("Número de vinos del cluster")


# In[19]:


clus.children_


# In[20]:


from scipy.cluster.hierarchy import dendrogram, linkage


# In[21]:


Z = linkage(df_norm, "ward")


# In[27]:


plt.figure(figsize=(25,10))
plt.title("Dendrograma de los vinos")
plt.xlabel("Id del vino")
plt.ylabel("Distancia")
dendrogram(Z, leaf_rotation=90., leaf_font_size=8.,truncate_mode="lastp", p=40, show_contracted=True, show_leaf_counts=False)
plt.show()


# ### K-means

# In[28]:


from sklearn.cluster import KMeans
from sklearn import datasets


# In[29]:


model = KMeans(n_clusters = 6)
model.fit(df_norm)
## KMean(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
## n_clusters=6, n_init=10, n_jobs=1, precompute_distances='auto',
## random_state=None, tol=0.0001, verbose=0)


# In[32]:


model.labels_  ## para saber la etiqueta sobre a que cluster corresponde cada uno del modelo


# In[33]:


md_k = pd.Series(model.labels_)


# In[34]:


df_norm["clust_h"] = md_h
df_norm["clust_k"] = md_k


# In[35]:


df_norm.head()


# In[36]:


df_norm.tail()


# In[38]:


plt.hist(md_k)


# In[39]:


model.cluster_centers_


# In[40]:


model.inertia_ ## suma de los cuadrados al 2 


# ## Interpretación final

# In[42]:


df_norm.groupby("clust_k").mean()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
from sklearn import metrics
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


telegramData = pd.read_csv("cleanedTelegram.txt", header=None)
telegramData.head()


# In[3]:


telegramData.info()


# In[4]:


redditData = pd.read_csv("cleanedReddit.txt", header=None)
redditData.head()


# In[5]:


redditData.info()


# In[6]:


#merge both dataframes
all_data = pd.concat([telegramData, redditData], ignore_index=True)
all_data.head()


# In[7]:


#remove numerical values
all_data[0] = all_data[0].str.replace('\d+', '')
all_data.head()


# In[8]:


#td-idf vectorize
data = all_data[0].values
vectorizer = TfidfVectorizer(strip_accents='unicode', stop_words='english', min_df=2) # Corpus is in English
X = vectorizer.fit_transform(data)
print(X.shape)


# In[9]:


word_features = vectorizer.get_feature_names_out()
print(len(word_features))
print(word_features[5000:5100])


# In[11]:


#elbow method
score = []
for i in range(2,11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    score.append(kmeans.inertia_)
    
plt.plot(range(2,11), score)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Score')
plt.savefig('elbow.png')
plt.show()


# In[14]:


print(word_features[250:300])


# In[28]:


kmeans = KMeans(n_clusters = 3, n_init = 20)
kmeans.fit(X)
label = kmeans.fit_predict(X)
# print(label)

common_words = kmeans.cluster_centers_.argsort()[:,-1:-26:-1]

for num, centroid in enumerate(common_words):
    print(str(num) + ' : ' + ', '.join(word_features[word] for word in centroid))


# In[29]:


print("Homogeneity: %0.3f" % metrics.homogeneity_score(label, kmeans.labels_))
print("Completeness: %0.3f" % metrics.completeness_score(label, kmeans.labels_))
print("V-measure: %0.3f" % metrics.v_measure_score(label, kmeans.labels_))
print("Adjusted Rand-Index: %.3f" % metrics.adjusted_rand_score(label, kmeans.labels_))
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, kmeans.labels_, sample_size=1000))


# In[ ]:





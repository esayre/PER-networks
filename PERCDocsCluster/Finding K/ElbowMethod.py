from FinalCode2 import tfidf_matrix
from scipy.spatial.distance import cdist, pdist
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

K = range(1,100)
KM = [KMeans(n_clusters=k).fit(tfidf_matrix.toarray()) for k in K]
centroids = [k.cluster_centers_ for k in KM]

D_k = [cdist(tfidf_matrix.toarray(), cent, 'euclidean') for cent in centroids]
cIdx = [np.argmin(D,axis=1) for D in D_k]
dist = [np.min(D,axis=1) for D in D_k]
avgWithinSS = [sum(d)/tfidf_matrix.toarray().shape[0] for d in dist]

# Total with-in sum of square
wcss = [sum(d**2) for d in dist]
tss = sum(pdist(tfidf_matrix.toarray())**2)/tfidf_matrix.toarray().shape[0]
bss = tss-wcss

kIdx = 10-1

# elbow curve
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(K, avgWithinSS, 'b*-')
ax.plot(K[kIdx], avgWithinSS[kIdx], marker='', markersize=12,
markeredgewidth=2, markeredgecolor='r', markerfacecolor='None')
plt.grid(True)
plt.xlabel('Number of clusters')
plt.ylabel('Average within-cluster sum of squares')
plt.title('Elbow for KMeans clustering')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(K, bss/tss*100, 'b*-')
plt.grid(True)
plt.xlabel('Number of clusters')
plt.ylabel('Percentage of variance explained')
plt.title('Elbow for KMeans clustering')
plt.show()
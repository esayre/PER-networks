from sklearn.metrics import silhouette_score
from FinalCode2 import tfidf_matrix
from scipy.spatial.distance import cdist, pdist
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

s = []
for n_clusters in range(2,100):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(tfidf_matrix.toarray())

    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_

    s.append(silhouette_score(tfidf_matrix.toarray(), labels, metric='euclidean'))


plt.ylabel("Silouette")
plt.xlabel("k")
plt.title("Silouette for K-means")
plt.plot(s)
plt.show(s)
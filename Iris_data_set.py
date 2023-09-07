import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]  # We're using only the first two features (sepal length and width)

# Perform k-means clustering with k=3 (three clusters)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
labels = kmeans.labels_

# Create a scatter plot to visualize the clusters
plt.figure(figsize=(10, 6))

# Scatter plot the data points for each cluster
for cluster_num in range(3):
    plt.scatter(X[labels == cluster_num][:, 0], X[labels == cluster_num][:, 1], label=f'Cluster {cluster_num + 1}')

# Plot the cluster centers
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', label='Cluster Centers')

plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('K-Means Clustering of Iris Dataset (Sepal Length vs. Sepal Width)')
plt.legend()
plt.show()
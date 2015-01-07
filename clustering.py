from sklearn import cluster


# Class to interface with KMeans Clustering object from scikit-learn cluster module
class KMeans:
    def __init__(self, data, n_clusters=8, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances=True, verbose=0, random_state=None, copy_x=True, n_jobs=1):
        self.n_clusters=n_clusters
        self.init=init
        self.n_init=n_init
        self.max_iter=max_iter
        self.tol=tol
        self.precompute_distances=precompute_distances
        self.verbose=verbose
        self.random_state=random_state
        self.copy_x=copy_x
        self.n_jobs=n_jobs

        self.data = data
        self.result = None
        self.dataTransformed = None
        self.obj = cluster.MiniBatchKMeans(n_clusters=self.n_clusters, init=self.init, n_init=self.n_init, max_iter=self.max_iter, tol=self.tol, precompute_distances=self.precompute_distances, verbose=self.verbose, random_state=self.random_state, copy_x=self.copy_x, n_jobs=self.n_jobs)

    def fit_model(self):
        self.dataTransformed = self.obj.fit_transform(self.data) # Transformed to cluster-distance space
        self.result = self.obj.fit_predict(self.data) # Index of closest cluster

    def print_results(self):
        print('\n Cluster Centers')
        print(self.obj.cluster_centers_)
        print('\n')

    def plot_results(self):
        # plot cluster centers along with all data, colored by nearest cluster
        pass


# Class to interface with MiniBatch KMeans Clustering object from scikit-learn cluster module
class MiniBatchKMeans:
    def __init__(self, data, n_clusters=8, init='k-means++', max_iter=100, batch_size=100, verbose=0, compute_labels=True, random_state=None, tol=0.0, max_no_improvement=10, init_size=None, n_init=3, reassignment_ratio=0.01):
        self.n_clusters=n_clusters
        self.init=init
        self.max_iter=max_iter
        self.batch_size=batch_size
        self.verbose=verbose
        self.compute_labels=compute_labels
        self.random_state=random_state
        self.tol=tol
        self.max_no_improvement=max_no_improvement
        self.init_size=init_size
        self.n_init=n_init
        self.reassignment_ratio=reassignment_ratio

        self.data = data
        self.result = None
        self.dataTransformed = None
        self.obj = cluster.KMeans(n_clusters=self.n_clusters, init=self.init, max_iter=self.max_iter, batch_size=self.batch_size, verbose=self.verbose, compute_labels=self.compute_labels, random_state=self.random_state, tol=self.tol, max_no_improvement=self.max_no_improvement, init_size=self.init_size, n_init=self.n_init, reassignment_ratio=self.reassignment_ratio)

    def fit_model(self):
        self.dataTransformed = self.obj.fit_transform(self.data) # Transformed to cluster-distance space
        self.result = self.obj.fit_predict(self.data) # Index of closest cluster

    def print_results(self):
        print('\n Cluster Centers')
        print(self.obj.cluster_centers_)
        print('\n')

    def plot_results(self):
        # plot cluster centers along with all data, colored by nearest cluster
        pass

# Class to interface with MeanShift clustering object from scikit-learn cluster module
# No need to know number of clusters a priori
class MeanShift:
    def __init__(self, data, bandwidth=None, seeds=None, bin_seeding=False, min_bin_freq=1, cluster_all=True):
        self.bandwidth=bandwidth
        self.seeds=seeds
        self.bin_seeding=bin_seeding
        self.min_bin_freq=min_bin_freq
        self.cluster_all=cluster_all

        self.data = data
        self.result = None
        self.dataTransformed = None
        self.obj = cluster.MeanShift(bandwidth=self.bandwidth, seeds=self.seeds, bin_seeding=self.bin_seeding, min_bin_freq=self.min_bin_freq, cluster_all=self.cluster_all)

    def fit_model(self):
        self.result = self.obj.fit_predict(self.data) # Index of closest cluster

    def print_results(self):
        print('\n Cluster Centers')
        print(self.obj.cluster_centers_)
        print('\n')

    def plot_results(self):
        # plot cluster centers along with all data, colored by nearest cluster
        pass

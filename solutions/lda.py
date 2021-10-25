from sklearn.decomposition import LatentDirichletAllocation
lda = LatentDirichletAllocation(n_components=4, 
                                max_iter=20, 
                                random_state=0)
lda.fit(bow)

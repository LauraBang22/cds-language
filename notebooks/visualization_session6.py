def visualization(words,model):

    
    import matplotlib.pyplot as plt
    from sklearn.decomposition import PCA
    
    X = []
    
    for word in words:
        X.append(model[word])

    
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)

    
    plt.scatter(result[:, 0], result[:, 1], marker = "*", color='#22ddca', s= 200)
    plt.title("Dimensionality reduction")
    plt.xlabel("Dimension 1")
    plt.ylabel("Dimension 2")

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    
    for i, word in enumerate(words):
        plt.annotate(word, xy=(result[i, 0], result[i, 1]))

    plt.show()



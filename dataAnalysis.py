import sklearn # scikit-learn
import numpy as np
import ols
import sgd
import pca

def main(dataset):

    while True:
        s=raw_input('Select data analysis task:\n 1. Regression\n 2. Diminsionality reduction\n 3. Clustering 0. Exit\n')
        if s=='0':
            break
        elif s=='1':
            if dataset.data.shape[0] < 100000:
                print('Running OLS Regression')
                reg = ols.OLS(dataset.data[:,1:dataset.data.shape[1]],dataset.data[:,0]) #independent variable is assumed to be in the first column
                reg.fit_model()
                print('Regression summary', reg.fitted_model.coef_)
                print('Performing assumption checks')
                reg.checks()
                print('Taking any necessary corrective actions')
                reg.mcAction()
                reg.acAction()
                reg.linAction()
                reg.singAction()
                reg.homoskeAction()
            else:
                print('Dataset is very large, running SGD Regression')
                reg = sgd.SGD(dataset.data[:,1:dataset.data.shape[1]], dataset.data[:,0])
                reg.fit_model()
                print('Regression summary', reg.fitted_model.coef_)

        elif s=='2':
            print('Trying randomized PCA\n')
            dec=pca.RPCA(dataset.data)
            dec.fit_model()
            print('Components')
            print(dec.obj.components_)
            print('\n Explained Variance Ratio')
            print(dec.obj.explained_variance_ratio_)

        elif s=='3':
            s=raw_input('Number of categories? Enter zero if unknown\n')
            try: n=int(s)
            except: n=0
            
            if n>0 & dataset.data.shape[0] < 10000:
                print('Known number of categories and <10k samples: Using KMeans clustering\n')
                # Use KMeans clustering
                # Followed by Spectral Clustering or GMM in event of failure
            elif n>0:
                print('Known number of categories and >10k samples: Using MiniBatch KMeans\n')
                # Use MiniBatch KMeans
            elif dataset.data.shape[0] < 10000:
                print('Unknown number of categories and <10k samples: Using MeanShift')
                # Use MeanShift or VBGMM
            else:
                print('Too many samples to analyze without knowing number of categories\n')

        else:
            print('Input not recognized')





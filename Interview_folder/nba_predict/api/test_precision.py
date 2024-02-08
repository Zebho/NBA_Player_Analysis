import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import KFold

from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score

from sklearn.svm import SVC

##Remarque :
# J'ai souhaité modifier le scorer car de mon point de vue, ce problème nécessite une metric qui nous
# permet d'être sur que les joueurs sélectionnés vont durer 5 ans. C'est donc la metric de
# de precision qui permet de visualiser cela.
# Il est possible de mdifier facilement un nouveau seuil, ou même de passer du coté du recall si nécessaire

#Ce premier scorer ne prend pas en compte une precision à 90%
def score_classifier_precision(dataset,classifier,labels,show=False):

    """
    performs 3 random trainings/tests to build a confusion matrix and prints results with precision and recall scores
    :param dataset: the dataset to work on
    :param classifier: the classifier to use
    :param labels: the labels used for training and validation
    :return:
    """

    kf = KFold(n_splits=3,shuffle=True,random_state=50)
    confusion_mat = np.zeros((2,2))
    precision = 0
    for training_ids,test_ids in kf.split(dataset):
        training_set = dataset[training_ids]
        training_labels = labels[training_ids]

        test_set = dataset[test_ids]
        test_labels = labels[test_ids]

        classifier.fit(training_set,training_labels)
        predicted_labels = classifier.predict(test_set)

        confusion_mat+=confusion_matrix(test_labels,predicted_labels)
        precision += precision_score(test_labels, predicted_labels) #Passage de Recall à Précision car on souhaite maximiser nos "prédits" afin qu'ils soient le plus statitisquement bon

    precision/=3

    if show:
        print(confusion_mat)
        print("Precision=",precision)
    return precision


def custom_predict(nouveau_joueur_scaled,model, custom_threshold=0.8472):
    """
    Input :
    - nouveau_joueur_scaled : dataframe composée des données du joueurs
    - model : model que l'on souhaite utiliser pour classifier
    - custom_threshold = 0.8472 : valeur calculé du seuil, qu'on peut modifier au besoin


    Output : Booléen
        True : Il est intéressany de le garder
        False : Il n'est pas intéressant de le garder

    """
    probs = model.predict_proba(nouveau_joueur_scaled)
    proba_1 = probs[:, 1]
    return (proba_1 > custom_threshold) #On modifiera la sortie au sein de la page Streamlit


#Ce second scorer prend en compte une precision à 90%, et renvoie la précision,
#en modifiant les prédictions qui ne pourraient pas être réalisable avec une précison de 90%
def score_classifier_precision_90(dataset,classifier,labels,show=False):

    """
    performs 3 random trainings/tests to build a confusion matrix and prints results with precision and recall scores
    :param dataset: the dataset to work on
    :param classifier: the classifier to use
    :param labels: the labels used for training and validation
    :return:
    """
    #Passage de recall à Précision car on souhaite maximiser nos "prédits" afin qu'ils soient le plus statitisquement bon
    kf = KFold(n_splits=3,shuffle=True,random_state=50)
    confusion_mat = np.zeros((2,2))
    precision = 0
    for training_ids,test_ids in kf.split(dataset):
        training_set = dataset[training_ids]
        training_labels = labels[training_ids]

        test_set = dataset[test_ids]
        test_labels = labels[test_ids]

        classifier.fit(training_set,training_labels)

        #Je calcule les probabilités et récupère celles d'être dans la catégorie "Bon Joueur"
        proba_1 = np.array(classifier.predict_proba(test_set)[:,1])
        #Que je compare avec le seuil trouvé à l'analyse pour que la précision soit de 90%
        predict = proba_1>0.8472

        confusion_mat+=confusion_matrix(test_labels,predict)
        precision += precision_score(test_labels, predict)

    precision/=3

    if show:
        print(confusion_mat)
        print("Précision=",precision)
    return precision

if __name__ == "__main__":
    # Load dataset
    df = pd.read_csv("data/nba_logreg.csv")

    # extract names, labels, features names and values
    names = df['Name'].values.tolist() # players names
    labels = df['TARGET_5Yrs'].values # labels
    paramset = df.drop(['TARGET_5Yrs','Name'],axis=1).columns.values
    df_vals = df.drop(['TARGET_5Yrs','Name'],axis=1).values

    # replacing Nan values (only present when no 3 points attempts have been performed by a player)
    for x in np.argwhere(np.isnan(df_vals)):
        df_vals[x] = 0

    # normalize dataset
    X = MinMaxScaler().fit_transform(df_vals)

    #example of scoring with support vector classifier
    score_classifier_precision(X,SVC(),labels,True)

    # TODO build a training set and choose a classifier which maximize recall score returned by the score_classifier function

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import KFold

from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score

from sklearn.svm import SVC

# This first scorer does not take into account an accuracy of 90%.
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
        precision += precision_score(test_labels, predicted_labels)

    precision/=3

    if show:
        print(confusion_mat)
        print("Precision=",precision)
    return precision


def custom_predict(nouveau_joueur_scaled,model, custom_threshold=0.8472):
    """
    Input :
    - new_player_scaled: dataframe composed of player data
    - model : model we want to use to classify
    - custom_threshold = 0.8472: calculated threshold value, which can be modified as required


    Output: Boolean
        True: It is interesting to keep it
        False : It is not interesting to keep it

    """
    probs = model.predict_proba(nouveau_joueur_scaled)
    proba_1 = probs[:, 1]
    return (proba_1 > custom_threshold) # We will modify the output in the Streamlit page


#This second scorer takes into account an accuracy of 90%, and returns the accuracy,
#by modifying the predictions that could not be made with 90% accuracy.
def score_classifier_precision_90(dataset,classifier,labels,show=False):

    """
    performs 3 random trainings/tests to build a confusion matrix and prints results with precision and recall scores
    :param dataset: the dataset to work on
    :param classifier: the classifier to use
    :param labels: the labels used for training and validation
    :return:
    """
    #Change from recall to accuracy because we want to maximise our "predictions" so that they are as statistically sound as possible.
    kf = KFold(n_splits=3,shuffle=True,random_state=50)
    confusion_mat = np.zeros((2,2))
    precision = 0
    for training_ids,test_ids in kf.split(dataset):
        training_set = dataset[training_ids]
        training_labels = labels[training_ids]

        test_set = dataset[test_ids]
        test_labels = labels[test_ids]

        classifier.fit(training_set,training_labels)

        # I calculate the probabilities and recover those of being in the "Good Player" category.
        proba_1 = np.array(classifier.predict_proba(test_set)[:,1])
        # I compare it with the threshold found in the analysis so that the accuracy is 90%.
        predict = proba_1>0.8472

        confusion_mat+=confusion_matrix(test_labels,predict)
        precision += precision_score(test_labels, predict)

    precision/=3

    if show:
        print(confusion_mat)
        print("Precision=",precision)
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


# system tools
import os
import sys
sys.path.append("..")

# data munging tools
import pandas as pd
import utils.classifier_utils as clf

# Machine learning stuff
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, ShuffleSplit
from sklearn import metrics
from codecarbon import EmissionsTracker

# Visualisation
import matplotlib.pyplot as plt

from joblib import dump, load

def load_data():
    filename = os.path.join("in", "fake_or_real_news.csv")
    data = pd.read_csv(filename, index_col=0)
    
    X = data["text"]
    y = data["label"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)
    
    return X, y, X_train, X_test, y_train, y_test

def create_vectorizer():
    vectorizer = TfidfVectorizer(ngram_range = (1,2),
                                lowercase = True,
                                max_df = 0.95,
                                min_df = 0.05,
                                max_features = 100)
    return vectorizer

def fitting_data(X_train, X_test, y_train, y_test, vectorizer):
    X_train_feats = vectorizer.fit_transform(X_train)

    X_test_feats = vectorizer.transform(X_test)

    feature_names = vectorizer.get_feature_names_out()

    classifier = LogisticRegression(random_state=42).fit(X_train_feats, y_train)

    return X_train_feats, X_test_feats, classifier

def predictions(X_test_feats, classifier):
    y_pred = classifier.predict(X_test_feats)

    return y_pred

def important_features(vectorizer, y_train, classifier):
    features = clf.show_features(vectorizer, y_train, classifier, n=20)
    #text_file = open("out/logistic_regression/features.txt", 'w')
    #text_file.write(features)
    #text_file.close()

def confusion_matrix(classifier, X_train_feats, y_train):
    metrics.ConfusionMatrixDisplay.from_estimator(classifier, X_train_feats,
                                                  y_train,
                                                  cmap = plt.cm.Blues,
                                                  labels = ["FAKE", "REAL"])
    plt.savefig("out/logistic_regression/confusion_matrix_logistic.png")

def classification_report(y_test, y_pred):
    classifier_metrics = metrics.classification_report(y_test, y_pred)
    text_file = open("out/logistic_regression/classification_report.txt", 'w')
    text_file.write(classifier_metrics)
    text_file.close()

def cross_validation(vectorizer, X, y):
    X_vect = vectorizer.fit_transform(X)
    title = "Learning Curves (Logistic Regression)"
    cv = ShuffleSplit(n_splits=100, test_size=0.2, random_state=0)

    estimator = LogisticRegression(random_state=42)
    clf.plot_learning_curve(estimator, title, X_vect, y, cv=cv, n_jobs=4)
    plt.savefig("out/logistic_regression/cross_validation.png")

def save_model(classifier, vectorizer):
    dump(classifier, os.path.join("models","LR_classifier.joblib"))
    dump(vectorizer, os.path.join("models","tfidf_vectorizer.joblib"))

def main():
    tracker = EmissionsTracker(project_name="assignment2_logistic_regression",
                        experiment_id="assignment2_logistic_regression",
                        output_dir=os.path.join("..", "Assignment5", "emissions"),
                        output_file="assignment2_logistic_regression.csv")

    tracker.start_task("load_data")
    X, y, X_train, X_test, y_train, y_test = load_data()
    data_emissions = tracker.stop_task

    tracker.start_task("vectorizer")
    vectorizer = create_vectorizer()
    vectorizer_emissions = tracker.stop_task

    tracker.start_task("fitting")
    X_train_feats, X_test_feats, classifier = fitting_data(X_train, X_test, y_train, y_test, vectorizer)
    fitting_emissions = tracker.stop_task

    tracker.start_task("predictions")
    y_pred = predictions(X_test_feats, classifier)
    predictions_emissions = tracker.stop_task

    tracker.start_task("features")
    important_features(vectorizer, y_train, classifier)
    features_emissions = tracker.stop_task

    tracker.start_task("confusion_matrix")
    confusion_matrix(classifier, X_train_feats, y_train)
    matrix_emissions = tracker.stop_task

    tracker.start_task("classification_report")
    classification_report(y_test, y_pred)
    report_emissions = tracker.stop_task

    tracker.start_task("cross_validation")
    cross_validation(vectorizer, X, y)
    cross_validation_emissions = tracker.stop_task

    tracker.stop

    save_model(classifier, vectorizer)


if __name__ == "__main__":
    main()
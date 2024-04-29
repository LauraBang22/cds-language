from transformers import pipeline

import os
import sys
sys.path.append("..")
import pandas as pd
import matplotlib.pyplot as plt

def load_model():
    classifier = pipeline("text-classification", 
                        model="j-hartmann/emotion-english-distilroberta-base", 
                        top_k=None)
    return classifier

def load_data():
    filename = os.path.join("in", "Game_of_Thrones_Script.csv")
    data = pd.read_csv(filename)
    data.dropna(inplace=True)
    return data

def generate_labels(classifier, data):
    labels = []
    for line in data["Sentence"]:
        label = classifier(line)
        labels.append(label[line][0]["label"])
    return labels

def add_labels(labels, data):
    data["labels"] = labels
    simple_data = data.loc[:, ["Season", "labels"]]
    return simple_data

def save_data(simple_data):
    outpath = os.path.join("out", "labels.csv")
    simple_data.to_csv(outpath)

def main():
    tracker = EmissionsTracker(project_name="sentiment classification",
                           experiment_id="sentiment_classifier",
                           output_dir=outfolder,
                           output_file="emissions_sentiment.csv")
    tracker.start_task("")
    classifier = load_model()

    data = load_data()
    labels, data = generate_labels(classifier, data)
    tracker.stop_task()

    simple_data = add_labels(labels, data)
    save_data(simple_data)

    tracker.stop()

if __name__ == "__main__":
  main()

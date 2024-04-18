from transformers import pipeline

import os
import sys
sys.path.append("..")
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    filename = os.path.join("out", "labels.csv")
    data = pd.read_csv(filename)
    return data

def plot_emotion_distribution(data):
    unique_seasons = data['Season'].unique()
    unique_labels = data['labels'].unique()

    fig, axs = plt.subplots(2, 4, figsize=(16, 8))
    fig.suptitle("Distribution of all emotion labels in that season", fontsize=20, y=1.3)
    axs = axs.flatten()

    for idx, season in enumerate(unique_seasons):
        season_data = data[data['Season'] == season]
        label_counts = season_data['labels'].value_counts()
        axs[idx].bar(label_counts.index, label_counts.values)
        axs[idx].tick_params(axis='x', which='major', rotation=45)
        axs[idx].set_title(season)

    plt.tight_layout()  # Adjust spacing for titles and subplots
    plt.savefig("out/emotion_distribution.png")

    return unique_labels

def plot_relative_frequency(data, unique_labels):
    fig, axs = plt.subplots(2, 4, figsize=(16, 8))
    axs = axs.flatten()
    axs[7].axis('off')

    for idx, label in enumerate(unique_labels):
        label_data = data[data['labels'] == label]
        season_counts = label_data['Season'].value_counts(normalize=True) * 100
        season_counts = season_counts.sort_index()  # Sort by index to ensure proper line plot
        axs[idx].plot(season_counts.index, season_counts.values, marker='o')
        axs[idx].tick_params(axis='x', which='major', rotation=45)  # Ensure major tick rotation
        axs[idx].set_title(label)
        

    fig.suptitle("Relative frequency of each emotion across all seasons", fontsize = 20)
    plt.tight_layout()
    plt.savefig("out/relative_frequency.png")

def main():
    # Load the data
    data = load_data()

    # Plot the emotion distribution
    unique_labels = plot_emotion_distribution(data)

    # Plot the relative frequency
    plot_relative_frequency(data, unique_labels)

if __name__ == "__main__":
    main()

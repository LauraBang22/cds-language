# Assignment 4 in Language Analytics

### Assignment Discription
In this assignment I have solved the following tasks:
- Predict emotion scores for all lines in the data
- For each season
    - Plot the distribution of all emotion labels in that season
- For each emotion label
    - Plot the relative frequency of each emotion across all seasons

### Data
The data I have used in this assignment, is the scripts for all seasons of the TV show Game of Thrones, which can be found [here](https://www.kaggle.com/datasets/albenft/game-of-thrones-script-all-seasons).  You'll need to download it into the ```in``` folder in this repository. 

The model I have used to train the data is the model called **emotion-english-distilroberta-base** , which you can find more information about [here](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base).

### Reproducebility 
I have created a ```setup.sh``` file that can be run from the terminal using the code: 
```
bash setup.sh
``` 
When running it you create a virtual environment where you run the accompanying ```requirements.txt```. It also installs the model that is needed in the code.

I have for this assignment created two different ```run.sh``` files that can be run from the terminal using the code:
```
bash run_data.sh
bash run_plotting.sh
```
Each file opens the virtual environment again, then runs one of the scripts that I have written for this assignment, and finishes off by deactivating the virtual environment. 

### Results
I have for this assignment created two ```.py``` scripts. One is called ```data.py```, in which I load the dataset and run the classifier on it. I then cut the dataframe down to only containing the columns "Season" and "labels", and then save it in my **out** folder. This script can be very timeconsuming to run, which is why I decided to save the new dataframe for later use.

The other script is called ```plotting.py```. In that script I load the processed data, so I don't have to run the classifier on the data every time I open the code. Then I plot the distribution of all emotion labels in each season and the relative frequency of each emotion across all seasons. Both sets of plots can be found in the **out** folder.

From the plots over distribution of all emotion labels in each season, I can see that the distribution across the seasons are very similar. The vast majority of all lines have been deemed "neutral". The labels of "anger", "surprise" and "disgust" all have similar distribution across the seasons, but the last three labels of "fear", "sadness" and "joy" vary a little bit across the seasons.

From the plots over relative frequency of each emotion, I can see that they vary quite a lot. 
- Season 1 has the most "surprise"
- Season 3 has the most "disgust"
- Season 5 has the most "joy"
- Season 6 has the most "sadness"
- Season 7 has the most "fear"
- Season 8 has the most "anger" 

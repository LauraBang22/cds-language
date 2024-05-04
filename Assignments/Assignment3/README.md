# Assignment 3 - Query expansion with word embeddings

### Assignment Discription
In this assignment I have solved the following tasks for the given data:
- Loads the song lyric data
- Downloads/loads a word embedding model via ```gensim``` (see below)
- Takes a given word as an input and finds the most similar words via word embeddings
- Find how many songs for a given artist feature terms from the expanded query
- Calculate the percentage of that artist's songs featuring those terms
- Print and/or save results in an easy-to-understand way
    - For example, "45% of {ARTIST}'s songs contain words related to {SEARCH TERM}"

### Repository Structure
In this repository you'll find ttwo subfolders.
- In ```in``` you'll find the data that is being used in the code.
- In ```src``` you'll find the scripts of code written to solve the tasks given in the assignment.

I have also created a requirements.txt and a setup.sh file for you to run, for the setting up a virtual enviroment to run the code in.

### Data
The data I have used in this assignment, is called **57,650 Spotify Songs**. More information about the data can be found  [here](https://www.kaggle.com/datasets/joebeachcapital/57651-spotify-songs). You'll need to download it into the ```in``` folder in this repository. 

### Reproducebility 
I have created a ```setup.sh``` file that can be run from the terminal using the code: 
```
bash setup.sh
``` 
When running it you create a virtual environment where you run the accompanying ```requirements.txt```. It also installs the model that is needed in the code.

To run the code of the script you have to run this in the terminal: 
```
python src/Assignment3.py --artist "{ARTIST}" -- "{SEARCH TERM}"
``` 
You can choose an artist and a searchterm yourself.

I have also created a ```run.sh``` file that can be run from the terminal using the code:
```
bash run.sh
```
The ```run.sh``` opens the virtual environment again and contians code seaching for a specific artist and searhterm, that have been tested and works, and then deactivates the virtual environment again.

### Results
When running this code, you'll get a percentage of songlyrics in the dataset, that contains the word or one of the five most similar words.

Examples of code I have tested myself:
- ```python src/Assignment3.py --artist "The Beatles" --search_term "love"```
    - 69.7 % of The Beatles 's songs contain words related to love
- ```python src/Assignment3.py --artist "Lady Gaga" --search_term "power"```
    - 10.9 % of Lady Gaga 's songs contain words related to power
- ```python src/Assignment3.py --artist "Elton John" --search_term "joy"```
    - 2.9 % of Elton John 's songs contain words related to joy
 

#### CodeCarbon
I have used the package ```CodeCarbon``` to measure the environmantal impact of running the code in this repository. Please see Assignment 5 for the results of that.
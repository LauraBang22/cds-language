# Assignment 1 - Extracting linguistic features using spaCy

### Assignment Discription
In this assignment I have solved the following tasks for the given data:
- Loop over each text file in the folder called ```in```
- Extract the following information:
    - Relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words
    - Total number of *unique* PER, LOC, ORGS
- For each sub-folder (a1, a2, a3, ...) save a table which shows the following information:

|Filename|RelFreq NOUN|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORG|
|---|---|---|---|---|---|---|---|
|file1.txt|---|---|---|---|---|---|---|
|file2.txt|---|---|---|---|---|---|---|
|etc|---|---|---|---|---|---|---|

In this repository you'll find three subfolders called ```in```, ```out``` and ```scr```. In these folders youll be able to find the data I'm working with, the script with code I have written and the results I have produced.

I have also created a requirements.txt and a setup.sh file for you to run, for the setting up a virtual enviroment to run the code in.

### Data
The data used in this assignment, is a dataset called **The Uppsala Student English Corpus (USE)**.
The data can be found [here](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457). You'll need to download the folder called **USEcorpus.zip**  and unpack it in the ```in``` folder in this repository. 

The model I have used to work on the data is from the package ```spaCy```train the data is the model called **en_core_web_md** , which you can find more information about [here](https://spacy.io/models/en#en_core_web_md).

### Reproducebility 
I have created a ```setup.sh``` file that can be run from the terminal using the code: 
```
bash setup.sh
``` 
When running it you create a virtual environment where you run the accompanying ```requirements.txt```. It also installs the model that is needed in the code.

I have also created a ```run.sh``` file that can be run from the terminal using the code:
```
bash run.sh
```
It opens the virtual environment again, then runs the script I have written to solve the task given, and finishes off by deactivating the virtual environment.

### Results
This code generates 14 ```.csv``` files structured in the way, that was part of the task.  

#### CodeCarbon
I have used the package ```CodeCarbon``` to measure the environmantal impact of running the code in this repository. Please see Assignment 5 for the results of that.
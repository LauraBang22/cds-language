# Assignment 2 - Text classification benchmarks

### Assignment Discription
In this assignment I have solved the following tasks for the given data:
- Save the classification report to a text file the folder called out
- Save the trained models and vectorizers to the folder called models

### Repository Structure
In this repository you'll find four subfolders.
- In ```in``` you'll find the data that is being used in the code.
- In ```models``` you'll find the different models I have run on the data.
- In ```out``` you'll find the results the code have produced.
- In ```src``` you'll find the scripts of code written to solve the tasks given in the assignment.

I have also created a requirements.txt and a setup.sh file for you to run, for the setting up a virtual enviroment to run the code in.

### Data
The data I have used in this assignment, is called **Fake News Dataset**. The data can be found [here](https://www.kaggle.com/datasets/jillanisofttech/fake-or-real-news). You'll need to download it into the ```in``` folder in this repository. 


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
It opens the virtual environment again, then runs the scripts I have written to solve the task given, and finishes off by deactivating the virtual environment. 
The first script is ```logistic_regression.py```, that trains a logistic regression model to predict labels for the data. The second script is ```neural_network.py```, that trains a MLP Classifier, which is a type of neural network model, to predict labels for the data. The third script is ```vectorizer.py```, which creates and saves the a vectorizer model for later possible use.

### Results
#### Logistic Regression
When running the logistic regression model on the data, it gives an accuracy of 83% in the classification report. That is very good. However when you look at learning curves of the cross validation, it shows that the curves are quite far apart, which might indicate that there is a problem of the model overfitting. Something that might help fix that problem is if we had more data to train it on. 

#### Neural Network
When running the neural network model on the data, it  gives an accuracy of 84%, which is one percent better than the logistic regression model.
At first glance the loss curve for the model looks very good. It decreases and stabilizes, which is good. I don't have something to compare it to, which makes it difficult to tell is the model is either underfitting or overfitting. That is something that could be worked on adding to the code. 

#### CodeCarbon
I have used the package ```CodeCarbon``` to measure the environmantal impact of running the code in this repository. Please see Assignment 5 for the results of that.
# Book Recommendation System

# About the project:

This is a streamlit web application that can recommend various kinds of similar books based on an user interest the concept of Collaborative based filtering is used here.

# Dataset Link:

* [Dataset link](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset)

# Concept used to build the model.pkl file : NearestNeighbors

1 . Load the data
	
2 . Initialise the value of k

3 . For getting the predicted class, iterate from 1 to total number of training data points

4 . Calculate the distance between test data and each row of training data. Here we will use Euclidean distance as our distance metric since it’s the most popular method. 

5 . Sort the calculated distances in ascending order based on distance values
	
6 . Get top k rows from the sorted array

# How to run?
### STEPS:

Clone the repository

```bash

```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n bookenv python=3.8 -y
```

```bash
conda activate bookenv
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Run this file to generate the model files in the artifacts folder
notebook.ipynb
```

Now run,
```bash
streamlit run app.py
```


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these following steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Description of your changes'`.
4. Push your changes to your fork: `git push origin feature-name`.
5. Create a pull request on the original repository.

# Reddit Flair Detector

A Reddit Flair Detector web application to detect flairs of India subreddit posts using Machine Learning algorithms. The application can be found live at [Reddit Flair Detector](https://r-india-flair-classifier.herokuapp.com/).
![](home.png)

### Directory Structure

The directory is a ***Flask*** web application set-up for hosting on *Heroku* servers. The description of files and folders can be found below:

  1. [app.py](https://github.com/pranay-ar/Reddit-Flare-Detection/blob/master/app.py) - The file used to start the Flask server.
  2. [requirements.txt](https://github.com/pranay-ar/Reddit-Flare-Detection/blob/master/requirements.txt) - Containing all Python dependencies of the project.
  3. [nltk.txt](https://github.com/pranay-ar/Reddit-Flare-Detection/blob/master/nltk.txt) - Containing all NLTK library needed dependencies.
  4. [Procfile](https://github.com/pranay-ar/Reddit-Flare-Detection/blob/master/Procfile) - Needed to setup Heroku.
  5. [Automated Testing](https://r-india-flair-classifier.herokuapp.com/automated_testing) - Webpage to predict the flairs of multiple posts at once using a .txt file.
  6. [templates](https://github.com/pranay-ar/Reddit-Flare-Detection/tree/master/templates) - Folder containing HTML/CSS files.
  7. [flair-detector](https://github.com/pranay-ar/Reddit-Flare-Detection/blob/master/app.py) - Folder containing the main application which loads the Machine Learning models and renders the results on the web application.
  8. [data](https://github.com/pranay-ar/Reddit-Flare-Detection/tree/master/Data) - Folder containing CSV and MongoDB instances of the collected data.
  9. [Models](https://github.com/pranay-ar/Reddit-Flare-Detection/tree/master/model) - Folder containing the saved model.
  10. [Jupyter Notebooks](https://github.com/pranay-ar/Reddit-Flare-Detection/tree/master/model) - Folder containing Jupyter Notebooks to collect Reddit India data and train Machine Learning models. 


### Project Execution

  1. Open the `Terminal`.
  2. Clone the repository by entering `https://github.com/pranay-ar/Reddit-Flare-Detection.git`.
  3. Ensure that `Python3` and `pip` is installed on the system.
  4. Create a `virtualenv` by executing the following command: `virtualenv -p python3 env`.
  5. Activate the `env` virtual environment by executing the follwing command: `source env/bin/activate`.
  6. Enter the cloned repository directory and execute `pip install -r requirements.txt`.
  7. Enter `python` shell and `import nltk`. Execute `nltk.download('stopwords')` and exit the shell.
  8. Now, execute the following command: `python manage.py runserver` and it will point to the `localhost` with the port.
  9. Hit the `IP Address` on a web browser and use the application.
  
### Dependencies

The following dependencies can be found in [requirements.txt](https://github.com/pranay-ar/Reddit-Flare-Detection/blob/master/requirements.txt):

  1. [praw](https://praw.readthedocs.io/en/latest/)
  2. [scikit-learn](https://scikit-learn.org/)
  3. [nltk](https://www.nltk.org/)
  4. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  5. [bs4](https://pypi.org/project/bs4/)
  6. [pandas](https://pandas.pydata.org/)
  7. [numpy](http://www.numpy.org/)
  
### Approach

Going through various literatures available for text processing and suitable machine learning algorithms for text classification, I based my approach using [[2]](https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568) which described various machine learning models like Naive-Bayes, Linear SVM and Logistic Regression for text classification with code snippets. Along with this, I tried other models like Random Forest Algorithm. I have obtained test accuracies on various scenarios which can be found in the next section.

The approach taken for the task is as follows:

  1. Collect 1800 India subreddit data for each of the 15 flairs using `praw` module [[1]](http://www.storybench.org/how-to-scrape-reddit-with-python/).
  2. The data includes *title, comments, body, url, author, score, id, time-created* and *number of comments*.
  3. For **comments**, only top level comments are considered in dataset and no sub-comments are present.
  4. The ***title, comments*** and ***body*** are cleaned by removing bad symbols and stopwords using `nltk`.
  5. Five types of features are considered for the the given task:
    
    a) Title
    b) Comments
    c) Urls
    d) Body
    e) Combining Title, Comments, Body and Urls as one feature.
  6. The dataset is split into **70% train** and **30% test** data using `train-test-split` of `scikit-learn`.
  7. The dataset is then converted into a `Vector` and `TF-IDF` form.
  8. Then, the following ML algorithms (using `scikit-learn` libraries) are applied on the dataset:
    
    a) Naive-Bayes
    b) Linear Support Vector Machine
    c) Logistic Regression
    d) Random Forest
   9. Training and Testing on the dataset showed the **Linear Support Vector Machine** showed the best testing accuracy of **77.97%** when trained on the combination of **Title + Comments + Body + Url** feature.
   10. The best model is saved and is used for prediction of the flair from the URL of the post.
    
### Results

#### Title as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Naive Bayes                | 0.6792452830      |
| Linear SVM                 | 0.8113207547      |
| Logistic Regression        | **0.8231132075**  |
| Random Forest              | 0.8042452830      |
| MLP                        | 0.8042452830    |

#### Body as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Naive Bayes                | 0.5636792452   |
| Linear SVM                 | **0.8278301886**      |
| Logistic Regression        | 0.8066037735      |
| Random Forest              | 0.8207547169  |
| MLP                        | 0.7971698113      |

#### URL as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Naive Bayes                | 0.5754716981    |
| Linear SVM                 | **0.7523584905**  |
| Logistic Regression        | **0.7523584905**    |
| Random Forest              | 0.6886792452      |
| MLP                        | 0.7523584905      |

#### Comments as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Naive Bayes                | 0.4622641509      |
| Linear SVM                 | 0.4056603773      |
| Logistic Regression        | **0.4716981132**  |
| Random Forest              | 0.4646226415    |
| MLP                        | 0.4599056603      |

#### Title + Comments + URL + Body as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Naive Bayes                | 0.5589622641      |
| Linear SVM                 | **0.8325471698**      |
| Logistic Regression        | 0.8254716981      |
| Random Forest              | 0.8089622641  |
| MLP                        | 0.8372641509      |


### Intuition behind Combined Feature

The features independently showed a test accuracy near to **82%** with the `URL` feature giving the worst accuracies during the training. 
### References

1. [How to scrape data from Reddit](http://www.storybench.org/how-to-scrape-reddit-with-python/)
2. [Multi-Class Text Classification Model Comparison and Selection](https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568)

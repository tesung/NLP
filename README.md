# NLP

### Reddit Thread Recommender

App can be found here https://share.streamlit.io/tesung/nlp/main/NFT_recommender.py

##### Abstract

The purpose of this project is to build a recommender system for reddit threads based off comment content. I want to sort through thousands of reddit comments to find the thread that best matches a topic I am interested in learning more about with ease (and as little research/reading as possilbe). This project incorporates the fundamental concepts and models of NLP data processing. 

##### Design

I want to sort through reddit comments to pinpoint a specific thread related to the topic in mind. I downloaded public data obtained from [Kaggle](https://www.kaggle.com/datasets/pavellexyr/the-reddit-nft-dataset), stored it as a .csv file, used python as my programming language and for data wrangling, then wrote a .py file that is pushed to streamlit and functions as an interactive recommender. 

##### Data

The total data set had over 8 million rows. There was a consistent problem with run-time taking a long period, therefore I elected to run my NLP models on  a sample set of 1 million rows. At the end, after data processing and cleaning, I ended up with 276282 rows and 218995 columns. The rows represent comments of reddit threads and the columns represent each word seen in each comment. There were a lot of missing data points scattered throughout the .csv file, which is why the dataset shrunk from 1 million to about 280k. That said, there is still a significant amount of data and I was able to run my models smoothly. 

##### Algorithms

I tried both count vectorizer and TFIDF vectorizer as well as LSA and NMF topic modeling. In addition, I ran KMeans cluster modeling and plotted an inertia graph to determine how many topics I should be aiming for (I ended up choosing to have 10 topics). Ultimately, I decdied to go with TFIDF vectorizer and NMF topic modeling as that returned the best topics. Count vectorizer + LSA returned topics that did not make as much sense. Lastly, I used streamlit to deploy my recommender app.

##### Tools

Pandas
Scikit Learn
Count Vectorizer
TFIFD Vectorizer
LSA 
NMF
KMeans Clustering 
Streamlit

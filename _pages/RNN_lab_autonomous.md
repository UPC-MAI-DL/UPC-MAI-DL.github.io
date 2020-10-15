---
permalink: /rnn-lab-autonomous/
---

## Recurrent Neural Networks (Autonomous Laboratory)

This assignment is to be **solved individually**. You can repeat the partner from the previous 
assignment or change it if you prefer.

The autonomous laboratory is open for your exploration. Using the basic code provided in the guided laboratory, 
you should modify it to test different settings, and to understand the effect of the various components. 


You could use any dataset you wish as long as it is a problem that involves sequential data (e.g. time series, music, 
trajectories, text...). 

**You will have to inform me of the dataset you chosed as soon as possible, no repeated datasets
 are allowed**. Send me an email with your choice (bejar@cs.upc.edu)

  
At the end of this page you have a list of possible 
datasets and datasources. Using one of those is not a requirement, but **don't use a dataset** that is too simple or that has 
been used on tensorflow, keras, pytorch, CNTK demos. 


You can also use any framework you wish, train model you can find, or online dataset. 

In the end you must upload to the *raco* a report around 10-12 pages long as a PDF document (references not included) with your work. 
Minimum font size of 11. 

In general, it is better to focus in one aspect and to study it thoroughly, than to do small experiments 
on different topics without going any deep.

In this document there is a list of suggested questions you may consider to explore. 
It is not necessary to answer any or all these questions. 
You may choose to perform different experiments, for exploring different aspects of recurrent neural networks. 
Follow your own curiosity.

### Possible questions

* Does the type of recurrent unit cell have an impact on the results (Vanilla RNN, LSTM, GRU)
* Does the use of multiple layers help?
* How many neurons per layer are enough to overfit?
* When overfitting, what is the result of applying various regularization techniques? Is the behaviour different for different types of recurrent units?
* Does the optimization algorithm have an impact on the speed the network converges
* Does the batch size have an impact on the results?
* If the data has sequences of different length, does have an impact if the padding is at the begginnig or the end?
* If the sequences are reversed, does it improve the result? 
* If the dataset is a continuous sequence and it is a regression problem, using longer windows impoves the accuracy?
* If other methods have been already applied to the dataset, do recurrent networks obtain better results?


### Tips
Follows a list of tips for your report

- Properly introduce the data you work with
- Define the problem to solve (classification or regression) and the adequate loss function
- Properly split the data into train, test and validation (if needed)
- Don't use datasets for which achieving a 95% of accuracy is straight-forward 
- Use and show loss and/or accuracy plots in your discussion
- Apply techniques (e.g., regularization, dropout...) for a reason and properly motivate it. Dont do it just for the sake of doing stuff.
- Use a number of neurons per layer which is a power of 2
- Don't try to use all possible methods and techniques. Focus on certain aspects, try to understand and interpret their behavior
- Do not show only positive results, failures are as important as successes
- Use statistics and graphics to support your explanations
- When using a plot, stare at it for a while. Try to reason what can be understood from it. Make yourself related questions and act in consequence.
- To properly analyze and understand a model, you must train it to overfitting


---

This is a list of possible datasets and data sources:

* From Kaggle:

    * [air quality madrid](https://www.kaggle.com/decide-soluciones/air-quality-madrid)
    * [motionsense](https://www.kaggle.com/malekzadeh/motionsense-dataset)
    * [ema 65 crossover](https://www.kaggle.com/daytrader/ema-65-crossover)
    * [the smell of fear](https://www.kaggle.com/jswicker/the-smell-of-fear)
    * [pollution in atchison village richmond ca](https://www.kaggle.com/nicapotato/pollution-in-atchison-village-richmond-ca)
    * [hourly pollution levels in indian cities](https://www.kaggle.com/ankurankan/hourly-pollution-levels-in-indian-cities)
    * [web traffic time series forecasting](https://www.kaggle.com/c/web-traffic-time-series-forecasting)
    * [news category dataset](https://www.kaggle.com/rmisra/news-category-dataset)
    * [urban sound classification](https://www.kaggle.com/pavansanagapati/urban-sound-classification)
    * [kindle reviews](https://www.kaggle.com/bharadwaj6/kindle-reviews)
    * [amazon alexa reviews](https://www.kaggle.com/sid321axn/amazon-alexa-reviews)

* From UCI:

    * [Activity Recognition](https://archive.ics.uci.edu/ml/datasets/Activity+Recognition+system+based+on+Multisensor+data+fusion+%28AReM%29)
    * [Beijing PM2.5 Data](https://archive.ics.uci.edu/ml/datasets/Beijing+PM2.5+Data)
    * [Bach Chorales](https://archive.ics.uci.edu/ml/datasets/Bach+Chorales)
    * [Character Trajectories](https://archive.ics.uci.edu/ml/datasets/Character+Trajectories)
    * [Dataset for ADL Recognition](https://archive.ics.uci.edu/ml/datasets/Dataset+for+ADL+Recognition+with+Wrist-worn+Accelerometer)
    * [Epileptic Seizure Recognition](https://archive.ics.uci.edu/ml/datasets/Epileptic+Seizure+Recognition)

* Other data repositores and lists:
    * [Google Quickdraw Dataset](https://github.com/googlecreativelab/quickdraw-dataset)
    * [UCI ML repository](https://archive.ics.uci.edu/ml/index.php)
    * [Skywind list of open datasets](https://skymind.ai/wiki/open-datasets)
    * [Microsoft Research data science repository](https://www.microsoft.com/en-us/research/academic-program/data-science-microsoft-research/#!dataset-directory)
    * [Big Data Made Simple list of free dataserts](http://bigdata-madesimple.com/70-websites-to-get-large-data-repositories-for-free/)
    * [KDnuggets list of datasets](https://www.kdnuggets.com/datasets/index.html)
    * [Physionet database](https://physionet.org/physiobank/database/)

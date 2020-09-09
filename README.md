# Data Analysis Portfolio

------------
## Table of contents
* [About](#about)
* [Web Scraping](#web-scraping)
* [Data Cleaning and Debugging](#data-cleaning-and-debugging)
* [Machine Learning](#machine-learning)
* [Data Analysis and Visualization](#data-analysis-and-visualization)
* [SQL](#sql)
* [Interviews](#interviews)
* [Contact](#contact)
------------
## __About__
  This repository was created to track my progress in data analysis and machine learning using python. While it demonstrates my capability, it also keeps me motivated and inspired.
  
  
------------
## __Web Scraping__
I started off data analysis by collecting some publicly published data sets, but not all data of my interest were available, so I decided to learn web scraping.

For websites with implementations of infinite scrolling and 'load more' buttons, [selenium](https://selenium-python.readthedocs.io/getting-started.html) was used to navigate; whereas, for websites with multiple pages, [beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) was enough to perform web scraping. 

__Notebook__ | __Description__ | __Library__ | __Source__
-------------|-----------------|-------------|-----------
[Train to Busan IMDb Reviews](https://github.com/tw7366/Projects/blob/master/Projects/Train%20to%20Busan%20IMDb%20Reviews%20-%20NLP.ipynb) | Gathered reviews, titles, and ratings from the IMDb website - Have to click the "Load More" button | pandas, selenium, beaitufulsoup | [Train to Busan](https://www.imdb.com/title/tt5700672/reviews?ref_=tt_ov_rt)
[Web Scraping](https://github.com/tw7366/Projects/blob/master/Projects/Web%20Scraping.ipynb) | Used loops to web scrape information from multiple pages / Imported an already existing table / Joined tables from multiple sources | pandas, beaitufulsoup, requests, selenium | [Newegg](https://www.newegg.ca/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7708&Order=3), [Steam](https://store.steampowered.com/search/?specials), [Sky Sports EPL](https://www.skysports.com/premier-league-table/2019), [Wikipedia - Population](https://en.wikipedia.org/wiki/Population_of_Canada_by_province_and_territory), [Wikipedia - PostalAbbreviation](https://en.wikipedia.org/wiki/Canadian_postal_abbreviations_for_provinces_and_territories), [Books to Scrape](http://books.toscrape.com/)


------------
## __Data Cleaning and Debugging__
While I worked on multiple projects, I've come to realize most of data analysts' task is preprocessing data and debugging. 

* [Data preprocessing](https://www.geeksforgeeks.org/data-preprocessing-machine-learning-python/#:~:text=Data%20Preprocessing%20is%20a%20technique,not%20feasible%20for%20the%20analysis.) is a technique of cleansing and tidying raw data into a clean data set. 

* [Debugging](https://en.wikipedia.org/wiki/Debugging) is the process of finding and resolving bugs 

__Notebook__ | __Description__ | __Library__ | __Source__
-------------|-----------------|-------------|------------
[Cleansing and Tidying Data](https://github.com/tw7366/Projects/blob/master/Projects/Cleansing%20and%20Tidying%20Data.ipynb) | Transformed wide data to narrow data by unpivoting and melting dataframes | pandas, numpy | [Daniel Chen: Cleaning and Tidying Data in Pandas](https://www.youtube.com/watch?v=iYie42M1ZyU)
[Covid-19](https://github.com/tw7366/Projects/blob/master/Projects/Covid-19.ipynb) | Performed light data cleaning and debugging to fix graphs and functions | pandas, numpy, collections | [Covid-19 Activity](https://data.world/covid-19-data-resource-hub/covid-19-case-counts)
[Price of used cars](https://github.com/tw7366/Projects/blob/master/Projects/Price%20of%20used%20cars.ipynb) | Evaluated and selected relevant information from the huge volume of data, then more preprocessing was applied. This was probably the messiest data I had to deal with | collections, pandas, numpy, sklearn |  [Kaggle - Used cars database](https://www.kaggle.com/orgesleka/used-cars-database)
[Data Analyst](https://github.com/tw7366/Projects/blob/master/Projects/Data%20Analyst.ipynb) | Dealt with messy data and transformed it into a desirable form for data analysis | numpy, pandas | [Kaggle - Data Analyst Jobs](https://www.kaggle.com/andrewmvd/data-analyst-jobs)


------------
## __Machine Learning__
__Project__ | __Description__ | __Algorithm__ | __Library__ | __Source__
------------|-----------------|---------------|-------------|-----------
[Train to Busan IMDb Reviews](https://github.com/tw7366/Projects/blob/master/Projects/Train%20to%20Busan%20IMDb%20Reviews%20-%20NLP.ipynb) | Trained a doc2vec model to examine similarities between reviews  | [Natural Language Processing (NLP)](https://en.wikipedia.org/wiki/Neuro-linguistic_programming) | nltk, gensim, re | [IMDb - Train to Busan](https://www.imdb.com/title/tt5700672/reviews?ref_=tt_ov_rt)
[Google Stock Pricing](https://github.com/tw7366/Projects/blob/master/Projects/Google%20Stock%20Pricing%20-%20Prediction%20using%20regression.ipynb) | Created a OHLC chart to see the past trend and trained a linear regression model to forecast prices in the future | [Linear Regression](https://en.wikipedia.org/wiki/Linear_regression#:~:text=In%20statistics%2C%20linear%20regression%20is,is%20called%20simple%20linear%20regression.) | pandas, mplfinance, sklearn | [Yahoo Finance - Google Stock](https://finance.yahoo.com/quote/GOOG/history?p=GOOG)
[Price of used cars](https://github.com/tw7366/Projects/blob/master/Projects/Price%20of%20used%20cars.ipynb) | Created a correlation matrix to see the weight of significance of each feature and trained a linear regression model & a random forest regressor model to make predictions | [Linear Regression](https://en.wikipedia.org/wiki/Linear_regression#:~:text=In%20statistics%2C%20linear%20regression%20is,is%20called%20simple%20linear%20regression.), [Random Forest Regressor](https://heartbeat.fritz.ai/random-forest-regression-in-python-using-scikit-learn-9e9b147e2153) | sklearn, pandas, seaborn, matplotlib | [Kaggle - Used cars database](https://www.kaggle.com/orgesleka/used-cars-database)
[Mushroom Classification](https://github.com/tw7366/Projects/blob/master/Projects/Mushroom%20Classification.ipynb) | Predicted types of mushrooms by using various classification models |  [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) , [GaussianNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html), [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html) | pandas, numpy, sklearn | [Kaggle - Mushroom Classification](https://www.kaggle.com/uciml/mushroom-classification)
[SMS Spam Classification](https://github.com/tw7366/Projects/blob/master/Projects/SMS%20Spam%20Classification.ipynb) | Classified whether SMS texts are spam or not by using RandomForestClassifier and MultinomialNB. Then, the models' performances were examined and compared. | [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html), [MultinomialNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html), [make_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html), [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) | pandas, numpy, sklearn, re | [SMS Spam Collection Dataset](https://www.kaggle.com/uciml/sms-spam-collection-dataset)


------------
## __Data Analysis and Visualization__
__Project__ | __Objective__ | __Description__ | __Library__ | __Source__
------------|---------------|-----------------|-------------|-----------
[2018 Data Professionals' Average Salaries](https://github.com/tw7366/Projects/blob/master/Projects/2018%20Data%20Professionals'%20Average%20Salaries.ipynb) | I wanted to know the variety of data related jobs, the most used database systems, and average salaries. | Analyzed the most used DBMS(s) / popularity of data jobs / the most wanted job's average & median salaries in the U.S vs outside of the U.S. / job market locations / correlation between salaries and education | pandas, numpy, matplotlib, collections | [The 2018 Data Professionals Salary Survey Results](https://www.brentozar.com/archive/2018/01/2018-data-professionals-salary-survey-results/)
[Covid-19](https://github.com/tw7366/Projects/blob/master/Projects/Covid-19.ipynb) | As the pandemic of Covid-19 continues, I hoped to draw some insights and trends through this analysis. | Analyzed countries and provinces with the most confirmed cases / tracked the progression of covid by continent (confirmed vs new) / calculated mortality rate by continent / tracked the aggregate of covid-19 progression | pandas, numpy, collections, matplotlib, seaborn | [Covid-19 Activity](https://data.world/covid-19-data-resource-hub/covid-19-case-counts)
[Supermarket](https://github.com/tw7366/Projects/blob/master/Projects/Supermarket.ipynb) | Practice data analysis & visualization | Analyzed sales by gender, product line, branch, and time |  pandas, numpy, collections, matplotlib, seaborn | [Supermarket sales](https://www.kaggle.com/aungpyaeap/supermarket-sales)


------------
## __Interviews__
These are the past technical interview questions/assignments I've worked on 
 __Notebook__ | __Description__ | __Library__ |
--------------|-----------------|-------------|
[Creating a Timeline of Multiple Levels](https://github.com/tw7366/Projects/blob/master/Interviews/Interview%20Assignment%20-%20Creating%20a%20timeline%20of%20multiple%20levels.ipynb) | Given multiple events with start times and end times, I had to write a function to create a timeline by assigning a level to each event. Also, performed light data analysis| pandas, numpy, collections |


------------
## __SQL__
__Project__ | __Purpose__ | __DBMS__
------------|-------------|---------
[Valorant](https://github.com/tw7366/Projects/blob/master/Projects/Valorant_Stats_SQL.py) | Aside from trying online quizzes, I wanted to create my own database to practice SQL. I thought it'd be fun to track video game statistics of myself and my friends, so I started a small SQL project | [MySQL](https://www.mysql.com/)


------------
## __Contact__
* [LinkedIn](https://www.linkedin.com/in/tw7366/)
* E-mail: tw7366@hotmail.com

# Data Analysis Portfolio

## Table of contents
* [About](#about)
* [Web Scraping](#web-scraping)
* [Data Cleansing](#data-cleansing)
* [Machine Learning](#machine-learning)


------------
## __About__
  This repository was created to track my progress in data analysis and machine learning using python. While it demonstrates my capability, it also keeps me motivated and inspired.
  
  
------------
## __Web Scraping__
I started off data analysis by collecting some publicly published data sets, but not all data of my interest were available, thus, I decided to learn web scraping.

For websites with clever implementations of infinite scrolling and 'load more' buttons, [selenium](https://selenium-python.readthedocs.io/getting-started.html) was used to navigate; however, for most websites, [beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) was enough to perform web scraping. 

__Notebook__ | __Description__ | __Library__ | __Source__
------------|-----------------|---------------|-------------
[Train to Busan IMDb Reviews](https://github.com/tw7366/Projects/blob/master/Projects/Train%20to%20Busan%20IMDb%20Reviews%20-%20NLP.ipynb) | Gathered reviews, titles, and ratings from the IMDb website - Have to click the "Load More" button | pandas, selenium, beaitufulsoup (bs4) | [Train to Busan](https://www.imdb.com/title/tt5700672/reviews?ref_=tt_ov_rt)
[Web Scraping](https://github.com/tw7366/Projects/blob/master/Projects/Web%20Scraping.ipynb) | Used loops to web scrape information from multiple pages / Imported an already existing table / Joined tables from multiple sources | pandas, beaitufulsoup (bs4), requests, selenium | [Newegg](https://www.newegg.ca/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7708&Order=3), [Steam](https://store.steampowered.com/search/?specials), [Sky Sports EPL](https://www.skysports.com/premier-league-table/2019), [Wikipedia - Population](https://en.wikipedia.org/wiki/Population_of_Canada_by_province_and_territory), [Wikipedia - PostalAbbreviation](https://en.wikipedia.org/wiki/Canadian_postal_abbreviations_for_provinces_and_territories), [Books to Scrape](http://books.toscrape.com/)


------------
## __Data Cleansing__
While I worked on multiple projects, I've come to realize most of data analysts' task is preprocessing data. 

[Data preprocessing](https://www.geeksforgeeks.org/data-preprocessing-machine-learning-python/#:~:text=Data%20Preprocessing%20is%20a%20technique,not%20feasible%20for%20the%20analysis.) is a technique of cleansing and tidying raw data into a clean data set. 

__Notebook__ | __Description__ | __Library__ | __Source__
------------|-----------------|---------------|-------------
[Cleansing and Tidying Data](https://github.com/tw7366/Projects/blob/master/Projects/Cleansing%20and%20Tidying%20Data.ipynb) | Transformed wide data to narrow data by unpivoting and melting dataframes | pandas, numpy | [Daniel Chen: Cleaning and Tidying Data in Pandas](https://www.youtube.com/watch?v=iYie42M1ZyU)


------------
## __Machine Learning__
__Project__ | __Description__ | __Topic__ | __Library__ | __Source__
------------|-----------------|-----------|---------------|-----------
[Train to Busan IMDb Reviews](https://github.com/tw7366/Projects/blob/master/Projects/Train%20to%20Busan%20IMDb%20Reviews%20-%20NLP.ipynb) | Trained a doc2vec model to examine similarities between reviews  | [Natural Language Processing (NLP)](https://en.wikipedia.org/wiki/Neuro-linguistic_programming) | nltk, gensim, re | [Train to Busan](https://www.imdb.com/title/tt5700672/reviews?ref_=tt_ov_rt)
[Google Stock Pricing](https://github.com/tw7366/Projects/blob/master/Projects/Google%20Stock%20Pricing%20-%20Prediction%20using%20regression.ipynb) | Created a OHLC chart to see the past trend and trained a linear regression model to forecast prices in the future | Linear Regression | pandas, mplfinance, sklearn | [Yahoo Finance - Google Stock](https://finance.yahoo.com/quote/GOOG/history?p=GOOG)
[Price of used cars](https://github.com/tw7366/Projects/blob/master/Projects/Price%20of%20used%20cars.ipynb) | Created a correlation matrix to see the weights of significance of each feature and trained a linear regression model to make a prediction | Linear Regression | sklearn, pandas, seaborn, matplotlib | [Kaggle - Used cars database](https://www.kaggle.com/orgesleka/used-cars-database)


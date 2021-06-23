## Top Selling Books

### Project Summary

![image](https://user-images.githubusercontent.com/54513557/123025572-67861280-d3a0-11eb-859c-71434c6784d1.png)

Books are a very important aspect in the personal development of a human being as it exposes them to new ideas, perspectives and literary styles. Millions of books have been published over the years and they continue to be an integral aspect of people’s lives around the globe.
As part of my project, I have gathered data from three different data sources about the top selling books in the world and performed data cleaning/wrangling steps.  


### Dataset Details

1) Source 1 [Kaggle](https://www.kaggle.com/jealousleopard/goodreadsbooks) - The file contains details about 11,128 books with its book name, author, isbn, isbn13, publisher, publication date and other related information
2) Source 2 [Google books API](https://www.googleapis.com/books) - Google books API link contains details about the cost of the book, the link to buy the book along with book name, author, isbn, isbn13, publisher, publication date.
3) Source 3 [Wikipedia](https://en.wikipedia.org/wiki/List_of_best -selling_books) - This Wikipedia link has details about the best-selling books. Best-selling refers to the number of copies sold. It has details regarding the book name, author, approximate number of copies sold & genre.


### Technology Used:

1) Python 3
2) Jupyter Notebook


### Approach

- The 3 CSV files from the different sources were read and was merged using merge() and ‘inner’ join.
- Fuzzy matching technique was used to merge the Wikipedia data and the Google API data. Book Name & Author was used as a key and a threshold of 95. This merged dataframe was then loaded into the SQLite database.
- Kaggle data was loaded to the database and then the above merged data was then merged with the Kaggle data using ‘Inner’ join.
- The data was then read from the database to create Visualizations.


### Exploratory Data Analysis

1) Top 10 books sold

![image](https://user-images.githubusercontent.com/54513557/123026101-3ce88980-d3a1-11eb-85b8-dec5e92a42ad.png)

2) Highest Grossing Books in USA

![image](https://user-images.githubusercontent.com/54513557/123026139-4eca2c80-d3a1-11eb-987c-7ebb1b85a87f.png)

3) Compare Google Ratings & Goodreads Ratings

![image](https://user-images.githubusercontent.com/54513557/123026191-60abcf80-d3a1-11eb-8619-71bf584d0aeb.png)

4) Average Google rating distribution for all books

![image](https://user-images.githubusercontent.com/54513557/123026246-73be9f80-d3a1-11eb-9041-1693eb49437b.png)


### Conclusion

1) A Tale of Two Cities was the Top selling books which sold 200 Million copies.
2) The Alchemist was the book with the top dollar value sales of 779.35 Million Dollars.
3) Majority of the Top Selling books are written in English.
4) The overall rating of most of the top selling books are around 4.0.

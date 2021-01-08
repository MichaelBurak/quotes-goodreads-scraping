# Goodreads Quotes Scraping Script Suite(GQSSS one might say, don't say that...)
Scrapy scraper for goodreads to put text and author info into dynamo or mongodb, credit to https://paulvanderlaken.com/2019/12/27/web-scraping-python-goodreads-quotes/

# Files:

- goodreads-scraper.py: not my work, your use may vary, but I found it very helpful, check the link giving credit for details.
- goodreads-parse-dynamo.py: uses boto3 on the 'scraped-philosophy.txt' file produced by the scraper to insert quote text and quote author strings into a dynamodb table.
- goodreads-parse-mongo.py: uses pymongo to do the same with a MongoDB Atlas cluster. 

# Notes:

Default values for things like environmental variables on the parser-uploaders, configuration of boto3, any change in the name of the produced file need to be accounted for by any users. 

# Future work: 

- Adapt to a more general purpose set of scripts for working with goodreads and the quotes there. 

# Legal stuff:

- I don't own Goodreads, I didn't code the scraper, do what you want with this code, but in exchange for that, follow the three rules of life: be kind, be kind, you gotta be kind.

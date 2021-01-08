# import from existing scraped text file of philosophy quotes to mongo atlas
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient

# env var handling of token
load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")

# setting mongo references
cluster = MongoClient(MONGO_URL)
db = cluster["deep-thoughts"]
quote_col = db["quotes"]

# populating list of dictionaries of quotes and authors
lines = []

with open('scraped-philosophy.txt') as f:
    lines = f.readlines()

quote_list = []

for i in lines:
    quote_list.append({'text': i.split('-')[0], 'author': i.split('-')[-1]})

# insert into mongo
quote_col.insert_many(quote_list)

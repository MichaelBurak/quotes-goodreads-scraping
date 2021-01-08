# adapted from boto3 documentation tutorial, importing main libraries
import boto3
import requests

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('test_quotes')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
print(table.creation_date_time)

lines = []

with open('scraped-philosophy.txt') as f:
    lines = f.readlines()

quote_list = []

for i in lines:
    quote_list.append({'text': i.split('-')[0], 'author': i.split('-')[-1]})


# likely a less brute force and more pythonic way to do this, limited in record writes by dynamodb as well
for i in quote_list:
    table.put_item(
        Item={
            'text': i['text'],
            'author': i['author']
        }
    )

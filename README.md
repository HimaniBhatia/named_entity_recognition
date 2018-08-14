# Named Entity Recognition
This is a demonstration of named entity recognition.
Problem Statement - 
1.Searching relevant millions of news articles based on keywords is time consuming.
  Aim is to cut down the time cost by indexing the news articles by tagging the important 
  keywords of each news article.
2.Searching on the basis of certain tags - 'ORGANIZATION','PERSON','LOCATION'.It can then
  filter out news related to the tag given as input.
  Let say, if tag = 'ORGANIZATION', then it will filter out news containing "organization' news
  such as : Apple CEO decides to buy Korean Company
            Hitachi Data Systems launching new product resolving Water Harvesting Technique.
  
## Pre-requisites:
- Python3 installed
- `pip` installed

## Usage:
main.py [-h] tag [word]

Recognizes the named entites

positional arguments:
  tag --        Required(The tag with which to recognize)
  word --       Optional(The tag with which to refine the query)

optional arguments:
  -h, --help  show this help message and exit

## Description:
### `tag`: 
Required. The tag with which the entities will be recognized

### `word`:
Optional. The word with which given tag will be filtered.

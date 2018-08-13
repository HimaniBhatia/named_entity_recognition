# Named Entity Recognition
This is a demonstration of named entity recognition.

## Pre-requisites:
- Python3 installed
- `pip` installed

## Steps to setup the Project:
- `git clone` this project or download zip and extract it
- cd into the project directory and run:

    `pip install -r requirements.txt`

## Usage:
main.py [-h] tag [word]

Recognizes the named entites

positional arguments:
  tag         Required. The tag with which to recognize
  word        Optional. The tag with which to refine the query

optional arguments:
  -h, --help  show this help message and exit

## Description:
### `tag`: 
Required. The tag with which the entities will be recognized

### `word`:
Optional. The word with which given tag will be filtered.
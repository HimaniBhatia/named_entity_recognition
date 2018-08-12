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
main.py [-h] [--tag] [--word] query

Recognizes the named entites

positional arguments:
  query       The tag/word with whcih to recognize

optional arguments:
  -h, --help  show this help message and exit
  --tag       Marks the input as a tag. If not given, --word is required
  --word      Marks the input as a word. If not given, --tag is required

## Description:
### `query`: 
Required. The string with which the entities will be recognized

### `--tag`:
Optional. If used, the query to the program will be marked as a TAG.
If this is not given, then `--word` is requried.

### `--word`:
Optional. If used, the query to the program will be marked as a WORD.
If this is not given, then `--tag` is requried.
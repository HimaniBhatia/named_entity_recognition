import argparse

# initiate the parser
parser = argparse.ArgumentParser(
        description="Recognizes the named entites")

# add required argument
parser.add_argument(
    'query', 
    help="The tag/word with which to recognize"
)

# add a flag that marks the query as a TAG
parser.add_argument(
    '--tag', 
    dest='is_tag',
    action='store_true',
    help="Marks the input as a tag. If not given, --word is required"
)

# add a flag that marks the query as a WORD
parser.add_argument(
    '--word', 
    dest='is_word',
    action='store_true',
    help="Marks the input as a word. If not given, --tag is required"
)
import argparse

# initiate the parser
parser = argparse.ArgumentParser(
        description="Recognizes the named entites")

# add required argument
parser.add_argument(
    'tag', 
    help="Required. The tag with which to recognize"
)

# add a flag that marks the query as a TAG
parser.add_argument(
    'word', 
    nargs='?',
    help="Optional. The tag with which to refine the query"
)
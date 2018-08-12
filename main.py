from cli_parser import parser

def main():

    # parse all the command line arguments
    args = parser.parse_args()

    # validate the path passed in the argument
    if(args.is_tag and args.is_word):
        arge.error("Both --tag and --word cannot be used together")

    if(not args.is_tag and not args.is_word):
        arge.error("Either --tag or --word is required")

    if(args.is_tag):
        # code
    else:
        # code

if __name__ == '__main__':
  main()
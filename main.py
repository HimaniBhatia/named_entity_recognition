from cli_parser import parser

def main():

    # parse all the command line arguments
    args = parser.parse_args()
    tag = None
    word = None
    if args.tag:
        tag = args.tag
    if args.word:
        word = args.word

if __name__ == '__main__':
  main()
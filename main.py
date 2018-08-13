from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize
from cli_parser import parser
import pandas as pd

def formatted_entities_for_tag(classified_paragraph):
    entities = {'PERSON': list(), 'ORGANIZATION': list(), 'LOCATION': list()}

    for entry in classified_paragraph:
        entry_value = entry[0]
        entry_type = entry[1]

        if entry_type == 'PERSON':
            entities['PERSON'].append(entry_value)

        elif entry_type == 'ORGANIZATION':
            entities['ORGANIZATION'].append(entry_value)

        elif entry_type == 'LOCATION':
            entities['LOCATION'].append(entry_value)

    return entities


def tag_search(tag,news_dict):
    search_news_key_ls = []
    for k,v in news_dict.items():
        for k1,v1 in v.items():
            if k1 == tag and len(v[k1])>0:
                search_news_key_ls.append(k)
    return search_news_key_ls
    
    
def keyword_search(tag,keyword,news_corpus,news_dict,tagger):
    tokenized_corpus = list()

    for text in news_corpus:
        tokenized_corpus.append(word_tokenize(text))

    classified_corpus_list = tagger.tag_sents(tokenized_corpus)
    formatted_result = formatted_entities_for_keyword(classified_corpus_list)
    
    search_news_key_ls = []
    if keyword in set(formatted_result[tag]):
        for k,v in news_dict.items():
            for k1,v1 in v.items():
                if keyword in v1 and len(v[k1])>0:
                    search_news_key_ls.append(k)
    else:
        print('No News found!!!')
    
    return search_news_key_ls


def formatted_entities_for_keyword(classified_paragraphs_list):
    entities = {'PERSON': list(), 'ORGANIZATION': list(), 'LOCATION': list()}

    for classified_paragraph in classified_paragraphs_list:
        for entry in classified_paragraph:
            entry_value = entry[0]
            entry_type = entry[1]

            if entry_type == 'PERSON':
                entities['PERSON'].append(entry_value)

            elif entry_type == 'ORGANIZATION':
                entities['ORGANIZATION'].append(entry_value)

            elif entry_type == 'LOCATION':
                entities['LOCATION'].append(entry_value)

    return entities

def main():

    # parse all the command line arguments
    args = parser.parse_args()
    args_is_tag = args.tag
    args_is_word = args.word

    # validate the path passed in the argument
    if not args_is_tag:
        arge.error("--tag is missing")
    else:
        tagger = StanfordNERTagger('/Users/Shared/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
               '/Users/Shared/stanford-ner/stanford-ner.jar',
               encoding='utf-8')
        
        news_corpus = [
            'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.',
            "Apple Inc. is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer software, and online services. Its hardware products include the iPhone smartphone, the iPad tablet computer, the Mac personal computer, the iPod portable media player, the Apple Watch smartwatch, and the Apple TV digital media player. Apple's consumer software includes the OS X and iOS operating systems, the iTunes media player, the Safari web browser, and the iLife and iWork creativity and productivity suites. Its online services include the iTunes Store, the iOS App Store and Mac App Store, and iCloud. Apple was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne on April 1, 1976, to develop and sell personal computers. It was incorporated as Apple Computer, Inc. on January 3, 1977, and was renamed as Apple Inc. on January 9, 2007, to reflect its shifted focus toward consumer electronics. Apple (NASDAQ: AAPL ) joined the Dow Jones Industrial Average on March 19, 2015.",
            "At least 100 security forces killed in fight for Afghan city",
            "Sonia Gandhi, Oscar Fernandes Move High Court In National Herald IT Case",
            "Musk talking to Saudi fund, others as he seeks Tesla buyout financing",
            "Volkswagen's Electrify America taps Flintstones, Jetsons for EV campaign",
            "Netflix finance chief David Wells to step down",
            "Independent labels urge EU to block Sony's $2.3 billion bid for EMI",
            "Samsung may suspend operations at China mobile phone plant - report",
            "Oil India's quarterly profit jumps 56 percent, but misses estimate",
            "SEBI proposes changes to consent settlement rules",
            "VF to spin off Lee and Wrangler jeans into public company",
            "Erdogan vows action against 'economic terrorists' over lira plunge",
            "Citigroup says global card chief Linville leaving in shakeup",
            "Tesla short sellers trim exposure but stay the course",
            "Facebook pages with large U.S. following to require more authorization"
            "Hackers at convention test voting systems for bugs"
                    ]
        
        news_dict = {}
        for i,each_news in enumerate(news_corpus):
            tokenized_list = word_tokenize(each_news)
            news_dict[i] = formatted_entities_for_tag(tagger.tag(tokenized_list))


        if args_is_word:
            search_news_key_ls = keyword_search(args_is_tag,args_is_word,news_corpus,news_dict,tagger)
        else:
            search_news_key_ls = tag_search(args_is_tag,news_dict)
        
        search_news_ls = []
        for each_key in search_news_key_ls:
            search_news_ls.append(news_corpus[each_key])
               
        news_df = pd.DataFrame({'News':search_news_ls})
        news_df.to_csv('News.csv',index = False)               
        
if __name__ == '__main__':
  main()

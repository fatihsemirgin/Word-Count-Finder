# 2019510068 by Fatih Semirgin
SYMBOLS = """:;,.`’+-—"”“()!#$%&'*/<>=?[]\|_^"""
stops = (
    'able', 'about', 'above', 'abroad', 'according', 'accordingly', 'across', 'actually', 'adj', 'after', 'afterwards',
    'again', 'against', 'ago', 'ahead', "ain't", 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'alongside',
    'already', 'also', 'although', 'always', 'am', 'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any',
    'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear', 'appreciate',
    'appropriate', 'are', "aren't", 'around', 'as', "a's", 'aside', 'ask', 'asking', 'associated', 'at', 'available',
'away', 'awfully', 'back', 'backward', 'backwards', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been',
    'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'best', 'better',
    'between', 'beyond', 'both', 'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', "can't", 'caption', 'cause',
    'causes', 'certain', 'certainly', 'changes', 'clearly', "c'mon", 'co', 'co.', 'com', 'come', 'comes', 'concerning',
'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', "couldn't",
    'course', "c's", 'currently', 'dare', "daren't", 'definitely', 'described', 'despite', 'did', "didn't", 'different',
'directly', 'do', 'does', "doesn't", 'doing', 'done', "don't", 'down', 'downwards', 'during', 'each', 'edu', 'eg',
'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'entirely', 'especially', 'et', 'etc',
'even', 'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example',
'except', 'fairly', 'far', 'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed', 'following', 'follows',
'for', 'forever', 'former', 'formerly', 'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore', 'get',
'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'greetings', 'had', "hadn't",
'half', 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", 'hello', 'help',
'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', "here's", 'hereupon', 'hers', 'herself', "he's", 'hi', 'him',
'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 'however', 'hundred', "i'd", 'ie', 'if', 'ignored', "i'll",
"i'm", 'immediate', 'in', 'inasmuch', 'inc', 'inc.', 'indeed', 'indicate', 'indicated', 'indicates', 'inner', 'inside',
'insofar', 'instead', 'into', 'inward', 'is', "isn't", 'it', "it'd", "it'll", 'its', "it's", 'itself', "i've", 'just',
'k', 'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
'less', 'lest', 'let', "let's", 'like', 'liked', 'likely', 'likewise', 'little', 'look', 'looking', 'looks', 'low',
'lower', 'ltd', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', "mayn't", 'me', 'mean', 'meantime',
'meanwhile', 'merely', 'might', "mightn't", 'mine', 'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs',
'much', 'must', "mustn't", 'my', 'myself', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need', "needn't",
'needs', 'neither', 'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'no', 'nobody',
'non', 'none', 'nonetheless', 'noone', 'no-one', 'nor', 'normally', 'not', 'nothing', 'notwithstanding', 'novel', 'now',
'nowhere', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', "one's", 'only',
'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought', "oughtn't", 'our', 'ours', 'ourselves', 'out',
'outside', 'over', 'overall', 'own', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus',
'possible', 'presumably', 'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather', 'rd', 're', 'really',
'reasonably', 'recent', 'recently', 'regarding', 'regardless', 'regards', 'relatively', 'respectively', 'right',
'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed',
'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven', 'several', 'shall',
"shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'since', 'six', 'so', 'some', 'somebody', 'someday',
'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified',
'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking', 'tell', 'tends', 'th',
'than', 'thank', 'thanks', 'thanx', 'that', "that'll", 'thats', "that's", "that've", 'the', 'their', 'theirs', 'them',
'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', "there'd", 'therefore', 'therein', "there'll",
"there're", 'theres', "there's", 'thereupon', "there've", 'these', 'they', "they'd", "they'll", "they're", "they've",
'thing', 'things', 'think', 'third', 'thirty', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three', 'through',
'throughout', 'thru', 'thus', 'till', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly',
'try', 'trying', "t's", 'twice', 'two', 'un', 'under', 'underneath', 'undoing', 'unfortunately', 'unless', 'unlike',
'unlikely', 'until', 'unto', 'up', 'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using', 'usually', 'v',
'value', 'various', 'versus', 'very', 'via', 'viz', 'vs', 'want', 'wants', 'was', "wasn't", 'way', 'we', "we'd",
'welcome', 'well', "we'll", 'went', 'were', "we're", "weren't", "we've", 'what', 'whatever', "what'll", "what's",
"what've", 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', "where's", 'whereupon',
'wherever', 'whether', 'which', 'whichever', 'while', 'whilst', 'whither', 'who', "who'd", 'whoever', 'whole', "who'll",
'whom', 'whomever', "who's", 'whose', 'why', 'will', 'willing', 'wish', 'with', 'within', 'without', 'wonder', "won't",
'would', "wouldn't", 'yes', 'yet', 'you', "you'd", "you'll", 'your', "you're", 'yours', 'yourself', 'yourselves',
"you've", 'zero', 'a', "how's", 'i', "when's", "why's", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'I', 'www', 'amount', 'bill', 'bottom', 'call', 'computer', 'con',
'couldnt', 'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen', 'fifty', 'fill', 'find', 'fire',
'forty', 'front', 'full', 'give', 'hasnt', 'herse', 'himse', 'interest', 'itse”', 'mill', 'move', 'myse”', 'part',
'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten', 'thick', 'thin', 'top', 'twelve', 'twenty', 'abst',
'accordance', 'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah', 'announce', 'anymore', 'apparently',
'approximately', 'aren', 'arent', 'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol', 'briefly', 'ca', 'date',
'ed', 'effect', 'et-al', 'ff', 'fix', 'gave', 'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately',
'importance', 'important', 'index', 'information', 'invention', 'itd', 'keys', 'kg', 'km', 'largely', 'lets', 'line',
"'ll", 'means', 'mg', 'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted', 'obtain', 'obtained',
'omitted', 'ord', 'owing', 'page', 'pages', 'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present',
'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran', 'readily', 'ref', 'refs', 'related', 'research',
'resulted', 'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes', 'showed', 'shown', 'showns', 'shows',
'significant', 'significantly', 'similar', 'similarly', 'slightly', 'somethan', 'specifically', 'state', 'states',
'stop', 'strongly', 'substantially', 'successfully', 'sufficiently', 'suggest', 'thered', 'thereof', 'therere',
'thereto', 'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til', 'tip', 'ts', 'ups', 'usefully',
'usefulness', "'ve", 'vol', 'vols', 'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words', 'world',
'youd', 'youre')


def remove_symbols(words):  # To remove punctuation marks(symbols) from words. Actually here I keep the original word.
    for word in words:      # For example, isn't --> isn't, whale's --> whale's or ./whale's., --> whale's
        index = words.index(word)   # So whale's and whales are different and the meaning of the word is preserved.
        for symbol in SYMBOLS:      # Checking the front and back of the symbol.(Line 84)
            if symbol in word:      # It checks symbols for the beginning and end of the word.(Line 82)
                if word.index(symbol) == 0 or word.index(symbol) == len(word) - 1:
                    word = word.replace(symbol, "").lower()     # The word is updated as the symbol is deleted.
                elif not (word[word.index(symbol) + 1].isalpha() and word[word.index(symbol) - 1].isalpha()):
                    word = word.replace(symbol, "").lower()     # The word is updated as the symbol is deleted.
        words[index] = word.strip()     # The last form of the word is added to the list again.
    return words


def final_word_list(number_of_word, txt_name):  # To determine the number of words by removing the punctuation marks
    words = []                                  # from the words in the book and then separating the stop words from
    if ".txt" not in txt_name:
        txt_name += ".txt"
    book_file = open(txt_name, 'r', encoding='utf-8')
    for line in book_file:
        temp_words = line.strip().lower().split()  # Reading the book line by line and dividing it into spaces
        words += remove_symbols(temp_words)        # Also removing punctuation.
    book_file.close()                              # The words list contains words without punctuation.
    temp, freq_count, count, flag = [], {}, 0, False  # temp,flag,count for the case of more 1 word(Word Order 2,3,...)
    for word in words:                                # freq_count is a dictionary of words and word counts.
        if word != '' and word not in stops:
            if count > number_of_word - 2 and not number_of_word == 1:
                temp.append(word)
                for i in range(number_of_word - 1):  # For each word group.(Word Order: 1,2,3,4...)
                    word = temp[count - (i + 1)] + " " + word   # word[0]+word[1] , word[1]+word[2]...
                flag = False
            elif not number_of_word == 1:   # Adding first word if word order 2,3,4,5...
                temp.append(word)
                flag = True
            if not flag and word in freq_count.keys():
                freq_count[word] = freq_count[word]+1   # Increase the number of words in the dictionary
            elif not flag:
                freq_count[word] = 1    # Adding a word that is not in the dictionary and starting its value from 1.
            if not number_of_word == 1:
                count += 1
    return freq_count   # return a dictionary(word and their counts.


def Word_Order_Frequency_Two_Books(book1, book2, number_of_word=1, out_txt="out_default_2"):
    try:                            # Function that returns words common to two books.
        print(" WORD ORDER FINDER ".center(83, '-'))
        if number_of_word > 0:
            total_dic = {}          # total_dic containing common words and numbers of words in two books.
            book = book1  # For use in error display. (Line 152)
            book_1 = final_word_list(number_of_word, book1)  # book_1 is dictionary of first book.
            book = book2  # For use in error display. (Line 152)
            book_2 = final_word_list(number_of_word, book2)  # book_1 is dictionary of second book.
            if ".txt" not in out_txt:
                out_txt += ".txt"
            save_file = open(out_txt, "w", encoding='utf-8')
            for key1 in book_1.keys():
                if key1 in book_2.keys():   # Checking for words in the first book to exist in the second book.
                    total_dic[key1] = book_1[key1] + book_2[key1]  # to add the common word and its value to the dict.
            save_file.write("{:<12}{:^1}{:^13}{:^1}{:^13}{:^1}{:^16}\n".format("| TOTAL", "|", "BOOK1", "|", "BOOK2",
                                                                               "|", "WORD      |"))
            save_file.write("{:<12}{:^1}{:^13}{:^1}{:^13}{:^1}{:^16}\n".format("| ORDER", "|", "ORDER", "|", "ORDER",
                                                                               "|", "ORDER     |"))
            save_file.write("{:<12}{:^1}{:^13}{:^1}{:^13}{:^1}{:^16}\n".format("| FREQUENCY", "|", "FREQUENCY", "|",
                                                                               "FREQUENCY",  "|", "FREQUENCY |"))
            save_file.write("-" * 54 + "\n")
            i = 0
            for key, value in sorted(total_dic.items(), key=lambda item: item[1], reverse=True):  # For sorted dict.
                i += 1
                save_file.write("{:^12}{:^1}{:^13}{:^1}{:^13}{:^1}{:^12}\n".format(value, "|", book_1[key], "|",
                                book_2[key], "|", key))     # to write to the file.
                if i == 100:   # for the first 100 words.
                    break
            save_file.close()

            print("+ 'Word_Order_Frequency_Two_Books' function is used. \n"+f"+ Your arguments: {book1}, {book2}, {number_of_word}, {out_txt}" 
                  "\n+ The process has been completed."+f"You can check the saved file '{out_txt}' for output.")
        else:   # error messages for errors in function inputs
            print("IOERROR : Number of word invalid, must be > 0 ")
    except FileNotFoundError:  # error messages for errors in function inputs
        print(f"Your book name {book} is not found. Please enter a valid book name")
    except Exception as err:  # error messages for errors in function inputs
        print("+ ",err, "\n+ Please enter only 'valid' inputs --> (String)book_name,(String)book_name,(int)number_word,"
              "(String)save_file_name")


def Word_Order_Frequency_One_Book(book1, number_of_word=1, out_txt="out_default_1"):
    try:                                    # Words and numbers of words for one book, number_of_word means Word Order.
        print(" WORD ORDER FINDER ".center(83, '-'))
        if number_of_word > 0:
            book_1 = final_word_list(number_of_word, book1)  # book_1 is dictionary of first book.
            if ".txt" not in out_txt:
                out_txt += ".txt"
            save_file,i = open(out_txt, "w", encoding='utf-8'),0
            save_file.write("{:^15}{:^7}{:^15}\n".format("WORD", "|", "WORD"))
            save_file.write("{:^15}{:^7}{:^15}\n".format("ORDER", "|", "ORDER"))
            save_file.write("{:^15}{:^7}{:^15}\n".format("FREQUENCY", "|", "FREQUENCY"))
            save_file.write("-" * 37 + "\n")
            for key, value in sorted(book_1.items(), key=lambda item: item[1], reverse=True):   # For sorted dict.
                i += 1
                save_file.write("{:^15} {:^6} {:^15}\n".format(value, "|", key))    # To write to the file.
                if i == 100:    # for the first 100 words.
                    break
            save_file.close()
            print("+ 'Word_Order_Frequency_One_Book' function is used.\n"+f"+ Your arguments: {book1}, {number_of_word}, {out_txt}"  
                  "\n+ The process has been completed."+f"You can check the saved file '{out_txt}' for output.")
        else:
            print("Number of word invalid, must be > 0 ")   # Error messages for errors in function inputs

    except FileNotFoundError:   # Error messages for errors in function inputs
        print(f"Your book name {book1} is not found! ---> Please enter valid (String) book name")
    except Exception as err:    # Error messages for errors in function inputs
        print("+ ",err, "\n+ Please enter only 'valid' inputs --> (String)book_name,(int)number_word,(String)save_file_name")

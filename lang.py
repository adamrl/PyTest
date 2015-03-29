from nltk import stem

def test_stemming(word):
    print 'WordNetLemmatizer:', stem.WordNetLemmatizer().lemmatize(word)
    print 'LancasterStemmer:', stem.LancasterStemmer().stem(word)
    print 'PorterStemmer:', stem.PorterStemmer().stem(word)
    print 'RegexpStemmer:', stem.RegexpStemmer('ing$|s$|e$', min=4).stem(word)
    print 'SnowballStemmer:', stem.SnowballStemmer('english').stem(word)
    #print 'StemmerI:', stem.StemmerI().stem(word)


def main():
    test_stemming('running')
    print
    test_stemming('bass')


if __name__ == '__main__':
    main()

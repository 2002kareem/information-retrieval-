import nltk
#nltk.download('punkt')
from nltk import word_tokenize,sent_tokenize
from nltk.stem import PorterStemmer 
from nltk.stem.snowball import SnowballStemmer
port = PorterStemmer()
snow = SnowballStemmer('english')
z = input('enter the text')
a = input( 'chose the kind  (word or sent or origenal or other)')
if a == 'word':
    x = word_tokenize(z)
    print(x)
elif a == 'sent' :
    y = sent_tokenize(z)
    print(y)
elif a == 'origenal' :
    print(z)
elif a == 'other' :
    k = input('chose the kind of stemming (port or snowball)')
    if k == 'port':
        l = port.stem(z)
        print(l)
    elif k == 'snowball' :
        e = snow.stem(z)
        print(e)


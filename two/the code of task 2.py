import nltk
#nltk.download()
#import nltk
from nltk import word_tokenize,sent_tokenize
z = input('enter the text')
a = input( 'chose the kind  (word or sent)')
if a == 'word':
    x = word_tokenize(z)
    print(x)
elif a == 'sent' :
    y = sent_tokenize(z)
    print(y)
else :
    print(z)
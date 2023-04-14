import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

document = "my name is kareem elrawady,my father is working photograbher,my mother is working nurse,my sister is working translitor."

words = nltk.word_tokenize(document)

stop_words = set(stopwords.words('english'))

filtered_words = [word for word in words if word.lower() not in stop_words]

print(filtered_words)
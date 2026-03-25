import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Auto download
try:
    nltk.data.find('tokenizers/punkt')
except:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except:
    nltk.download('punkt_tab')

try:
    nltk.data.find('corpora/stopwords')
except:
    nltk.download('stopwords')

stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w not in stop_words]
    return " ".join(tokens)
# In this example, you do not need to preprocess the text data,
# as this will be done on the fly.

# I am personally not a fan of this, as I like to keep the different
# concerns separated.

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def to_lower(text):
    return text.lower()

def remove_punctuation(text):
    pattern = "[" + string.punctuation + "]+"
    text = re.sub(pattern, " ", text)
    text = text.replace("\n", " ")
    return text

def lemmatize_stopwords(s):
    # I combine lemmatization and stopword removal to
    # have them both use nlp()
    # This is the slow function! Can you do something about it?
    doc = nlp(s)
    lemma = [] 
    for token in doc:
        if token.text not in stopwords:
            lemma.append(token.lemma_)
    return ' '.join(lemma)

def lsw(text):
    return lemmatize_stopwords(text)


def preprocessor(text):
    text = to_lower(text)
    text = remove_punctuation(text)
    text = lsw(text)
    return text


vectorizer = CountVectorizer(min_df=4,
                             max_df=.5,
                             ngram_range=[1,2],
                            preprocessor=preprocessor)

df = pd.DataFrame({'text':data.data, 'target':data.target})

bow = vectorizer.fit_transform(df.text)
bow.shape
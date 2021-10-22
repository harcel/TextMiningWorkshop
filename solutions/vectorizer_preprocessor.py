# In this example, you do not need to preprocess the text data,
# as this will be done on the fly.

# I am personally not a fan of this, as I like to keep the different
# concerns separated.

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def to_lower(text):
    return text.str.lower()

def remove_punctuation(text):
    pattern = "[" + string.punctuation + "]+"
    text = text.str.replace(pattern, " ", regex=True)
    text = text.str.replace("\n", " ", regex=False)
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
    return text.apply(lemmatize_stopwords)


def preprocessor(text):
    text = to_lower(text)
    text = remove_punctuation(text)
    text = lsw(text)
    return text


vectorizer = CountVectorizer(min_df=4,
                             max_df=.5,
                             ngram_range=[1,2],
                            preprocessor=preprocessor)

bow = vectorizer.fit_transform(data.text)
bow.shape

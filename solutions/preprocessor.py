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


df = pd.DataFrame({'text':data.data, 'target':data.target})

processed = (df.text.pipe(to_lower)
                    .pipe(remove_punctuation)
                    .pipe(lsw)
            )


# Of course, this is just an example
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
vectorizer = CountVectorizer(min_df=4,
                             max_df=.5,
                             ngram_range=[1,2])
bow = vectorizer.fit_transform(processed)
bow.shape

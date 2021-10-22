mango = nlp('mango').vector
strawberry = nlp('strawberry').vector
brick = nlp('brick').vector

print(((mango - strawberry)**2).sum())
print(((mango - brick)**2).sum())
print(((strawberry - brick)**2).sum())

# If you do not download the larger language model like below,
# spaCy will complain about not having word vectors for the similarity
# measures. Download the larger model to your computer using 
# $ python -m spacy download en_core_web_lg
# Note that this takes about 800 MB of disk space
nlp = spacy.load('en_core_web_lg')
tokens = nlp('mango strawberry brick')
for i, token1 in enumerate(tokens):
    # similarities are symmetric!
    for token2 in tokens[i+1:]:
        print(token1.text, token2.text, token1.similarity(token2))
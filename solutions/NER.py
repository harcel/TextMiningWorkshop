new_sent = sentence.replace("Marcel", "Steve")
for ent in nlp(new_sent).ents: print(f"{ent} is a {ent.label_} and appears in the sentence at position {ent.start_char}")

displacy.render(nlp("Steve worked for Apple until January 2011"), style='ent', jupyter=True)

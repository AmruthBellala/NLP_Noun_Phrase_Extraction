# -*- coding: utf-8 -*-
"""
Created on Tue Aug 4 2020

@author: AmruthBellala
@title: NLP Using NLTK

"""
class Nlp:
    def extract_NN(self,sent):
        grammar = r"""
        NBAR:
            # Nouns and Adjectives, terminated with Nouns
            {<NN.*>*<NN.*>}
    
        NP:
            {<NBAR>}
            
            {<NBAR><IN><NBAR>}
        """
        chunker = nltk.RegexpParser(grammar)
        ne = set()
        chunk = chunker.parse(nltk.pos_tag(nltk.word_tokenize(sent)))
        for tree in chunk.subtrees(filter=lambda t: t.label() == 'NP'):
            ne.add(' '.join([child[0] for child in tree.leaves()]))
        return ne



import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

text=input("enter the query:")
obj = Nlp()
ne = list(obj.extract_NN(text))
lemmatizer = WordNetLemmatizer()
td = []


for word in ne:
    if word not in stopwords.words('english'):
        tem = lemmatizer.lemmatize(word)
        td.append(tem)
    else:
        continue

td.sort()
print(td)





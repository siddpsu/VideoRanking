'''
Created on 20-Feb-2014

@author: siddban
'''
import nltk
import urllib2
import re,math
import json
from pprint import pprint
from collections import Counter

def extract_entity_names(t):
    entity_names = []
    
    if hasattr(t, 'node') and t.node:
        if t.node == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
                
    return entity_names

f = open('myfile','w')
list_for_Scoring=[];
data = json.loads(open('CodeAssignmentDataSet.json').read())
for i in data:
    #pprint(i['title']);
    sentence=i['title'] + " " + i['description'];
    entity_names=[]
    categories=i['categories']
    #print categories
    #pprint(sentence)
    tokenized_sentence = nltk.word_tokenize(sentence)
    tagged_sentence =  nltk.pos_tag(tokenized_sentence)
    chunked_sentence = nltk.ne_chunk(tagged_sentence, binary=True)
    
    #print(chunked_sentence)
    entity_names.extend(extract_entity_names(chunked_sentence))
    entity_names=set(entity_names)
    appendstring=' '.join(entity_names)
    appendstring=appendstring + " " + ' '.join(categories)
    list_for_Scoring.append(appendstring)# + i['categories'])
    for i in entity_names:
        #if(i=="Petsami"):
            #pprint(i)
            f.write(','.join(entity_names))
            
    f.write("\n")
    #print "*****"

f.close()
    
## Video algorithm


#cosine sim
WORD = re.compile(r'\w+')

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)
 
def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator



#i=1

for word in list_for_Scoring:
    scores=[]
    #i=i+1
    #j=1
    for word2 in list_for_Scoring:
        #j=j+1
        #if(i!=j): 
        vector1 = text_to_vector(word)
        vector2 = text_to_vector(word2)
        cosine = get_cosine(vector1, vector2)
        scores.append(cosine)
    print sorted(range(len(scores)), key=lambda i: scores[i])[-4:]    


print "End"        











 
    
    
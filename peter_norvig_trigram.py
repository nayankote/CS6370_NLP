import re
from collections import Counter, defaultdict

# getting words from file
def get_words(lines):
    return re.findall(r'\w+', lines.lower())

def get_trigrams(lines):
    trigrams=[]
    for line in lines:
        words = ['<s>'] + re.findall(r'\w+', line.lower()) + ['</s>']
        trigrams.extend([(words[i-1],words[i],words[i+1]) for i in range(1,len(words)-1) ])
    return trigrams

# word frequencies
lines = open('brown.txt').read()
words_dict = Counter(get_words(lines))
trigram_dict = Counter(get_trigrams(lines))
number_of_words = sum(words_dict.values())
number_of_trigrams = sum(trigram_dict.values())

# P(w)
def prior_word(word):
    return words_dict[word]/number_of_words

def prior_trigram(trigram):
    return trigram_dict[trigram]/number_of_trigrams

# pruning edit distance words to only feasible 
def prune(edit_words):
    return ([word for word in edit_words if word in words_dict])

# possible 1 edit distance words
def edits1(word):
    
    letters='abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i],word[i:]) for i in range(len(word)+1)]
    deletes = [L + R[1:] for L,R in splits if R]
    inserts = [L + c + R for L,R in splits for c in letters]
    substitutions = [L + c + R[1:] for L,R in splits if R for c in letters]
    transpositions = [L + R[1] + R[0] +R[2:] for L,R in splits if len(R)>1]
    
    return set(deletes + inserts + substitutions + transpositions)

# possible 2 edit distance words 
def edits2(word):
    edits2=set()
    for edit1 in edits1(word) : edits2.update(edits1(edit1))
    return edits2

def known(words):
    return [word for word in words if word in words_dict]

def candidates(word):
    return known([word]) or known(prune(edits1(word))) or known(prune(edits2(word))) or word

def correction(word):
    return (max(candidates(word), key=prior_word))

#print(correction('Nayan'))
query="<s>"+input("Please enter a query : ")+"</s>"

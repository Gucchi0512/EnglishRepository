# -*- coding: utf-8 -*-
import re
import nltk
from ClassifyPerfect import perfect_classify
from be_verb import CheckBeSentence


def pos_tag(sentence = "I have been waiting for him since last night."):
    t = nltk.word_tokenize(sentence)
    pos = nltk.pos_tag(t)
    #print(pos)
    return(pos)

def get_verb_index(sentence):
    for index, pos in enumerate((sentence)):
        if re.match("VB*",pos[1]):
            return index

def is_Have(word):
    if word == "have" or word == "has" or word == "had": return True
    else: return False
        
def is_Be(word):
    if word == "be" or word == "is" or word == "am" or word == "are" or word == "was" or word == "were": return True
    else: return False

def check_Tense(pos, label, i):
    if pos[i-1][0] == "will": return "Futu" + label
    elif pos[i][1] == "VBD": return "Past" + label
    else: return "Pres" + label

def addLabel(label):
    return "[" + label +"]";



if __name__ == "__main__":
    path = 'in.txt'
    with open(path) as f:
        text = f.read()
    #text  = "I was a man."
    text = text.split(".")
    text.pop(-1)
    for i, x in enumerate(text):
        label = ""
        text[i] = x + "."
        pos = pos_tag(text[i])
        start_i = get_verb_index(pos)
        if is_Have(pos[start_i][0]):
            label = perfect_classify(pos)  
        if is_Be(pos[start_i][0]):
            label = CheckBeSentence(pos, start_i)
        label = check_Tense(pos,label,start_i)
        text[i] += addLabel(label)
        print(text[i])


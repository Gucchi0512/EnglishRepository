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

def is_Be(word):
    if word == "is" or word == "am" or word == "are" or word == "was" or word == "were":
        return True
    else: return False

def check_Tense(pos, label):
    if pos[0] == "will": return "Futu" + label
    elif pos[1] == "VBD": return "Past" + label
    else: return "Pres" + label

def addLabel(label):
    return "[" + label +"]";

if __name__ == "__main__":
    text = "I have been waiting for him since last night."
    pos = pos_tag(text)
    start_i = get_verb_index(pos)
    if pos[start_i][0] == "have" or pos[start_i][0] == "has" or pos[start_i][0] == "had":
        label = perfect_classify(pos)  
    if is_Be(pos[start_i][0]):
        label = CheckBeSentence(pos, start_i)
    label = check_Tense(pos[start_i],label)
    text += addLabel(label)
    print(text)
    

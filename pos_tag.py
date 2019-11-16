import nltk

def test():
    sentence = "I have been waiting for him since last night."
    #sentence = input()
    pos_tag(sentence)

def pos_tag(sentence):
    t = nltk.word_tokenize(sentence)
    pos = nltk.pos_tag(t)
    print(pos)
    return(pos)

test()

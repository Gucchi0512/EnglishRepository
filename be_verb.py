import nltk

def CheckBeSentence(pos, index):
    count=0
    label=''
    for data in pos:
        count+=1
        tag = data[1]
        if count-1<index:
            continue
        if tag == 'VBG':
            label+='Cont'
            break
        elif tag == 'VBN':
            label+=(CheckBeSentence(pos, count))
            break
        elif tag[0]!='V':
            label+='Simp'
            break
    return label
            



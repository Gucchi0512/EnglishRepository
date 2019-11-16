import nltk

def CheckBeCentence(pos, index):
    count=0
    label=''
    for data in pos:
        count+=1
        tag = data[1]
        if count-1<index:
            continue
        if tag == 'RB':
            label+='Negative'
        elif tag == 'VBG':
            label+='Progressive'
            break
        elif tag == 'VBN':
            label+=('Passive'+CheckBeCentence(pos, count))
            break
        elif tag[0]!='V':
            label+='Simple'
            break
    return label
            



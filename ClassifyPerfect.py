from be_verb import CheckBeSentence

def perfect_classify(t):
    f_flag = ''
    s = ''
    flag=0
    for i,pos in enumerate(t,0):
        if flag != 0 :
            if pos[1] == 'VBN' :
                if  pos[0] == 'been':
                    s = CheckBeSentence(t,i)
                break
            elif pos[1]=='RB': 
                continue
            else : flag = 0
        #elif(pos[0]=='will'):
         #   f_flag='Futu'
        elif pos[0]=='have' :
            flag = 1
        elif pos[0]=='has' :
            flag = 2
        elif pos[0]=='had' :
            flag = 3
    return attach_label(flag,s,f_flag)

def attach_label(f,s,f_flag):
    if f == 0:
        return 'None'
    #elif f == 3:
     #   return f_flag+'PerfectPast' + s
    else :
        return f_flag+'Perf' + s

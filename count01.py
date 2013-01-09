def check(out):
    return out.count('1')

def countN(out,level):
    global count
    if level == 0:
        if  check(out) == 5:
            count+=1
            print out
        return
        
 #       print count
    else:
        countN(out+'0',level-1)
        countN(out+'1',level-1)
count = 0
out = ''        
countN(out,10)
print count

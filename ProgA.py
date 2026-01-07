def longdist(seq):
    letters= 'ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvxyz'
    numbers = '1234567890'
    used = []
    pair = dict()
    reverse = seq[::-1]
    maxlength = 0
    maxl = 'None'
    for l in letters + numbers:
        if l in seq:
            used.append(l)
            if seq.index(l) == (len(seq)- reverse.index(l)):
                pair[l] = 0
            else:
                pair[l] =  abs((seq.index(l)+1) - (len(seq)- (reverse.index(l))-1))
                print(l)
                print(pair[l])

                if pair[l]>maxlength:
                    maxlength = pair[l]
                    maxl = l
    return maxl, maxlength
    




    
    
print(longdist(input()))
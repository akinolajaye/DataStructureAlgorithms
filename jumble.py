scramble = 'hlltehtewoloord'
wordset = ['hello','to','the','world']

def wordsetToDict(wordset):
    worddict = {}
    for word in wordset:
        key = 1
        key2 = 0
        for c in word:
            key *= ord(c)#creates
            key2 += ord(c)
        worddict[(key,key2)] = word
    return worddict



worddict = wordsetToDict(wordset)
print(worddict)

def unscramble(scramble,worddict):
    outstr = ''
    key = (1,0)
    counter = 0
    begin = 0
    while (counter < len(scramble)):
        c = scramble[counter]
        # make c to be considered in key
        key = (key[0]*ord(c),key[1]+ord(c))
        # test for existence in wordset
        if key in worddict:
            # Add word to output string
            outstr += worddict[key] + ' '
            # update where to begin
            begin = begin + len(worddict[key])
            # move counter to the beginning
            counter = begin
            # reset key
            key = (1,0)
        else:
            # increment counter
            counter += 1
    return outstr[0:(len(outstr)-1)]

unscramble(scramble,worddict)
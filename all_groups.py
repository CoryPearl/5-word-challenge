#time to compleat: 889.6405 seconds (14.83 minutes)
#33 groups of 5 found
#[['ampyx', 'bortz', 'chivw', 'fjeld', 'gunks'], ['becks', 'frowl', 'japyx', 'vingt', 'zhmud'], ['becks', 'fultz', 'japyx', 'mordv', 'whing'], ['bilks', 'fconv', 'grewt', 'japyx', 'zhmud'], ['bleck', 'frows', 'japyx', 'vingt', 'zhmud'], ['block', 'fremt', 'japyx', 'vughs', 'windz'], ['blows', 'freck', 'japyx', 'vingt', 'zhmud'], ['bocks', 'flegm', 'japyx', 'thruv', 'windz'], ['bongs', 'chivw', 'fremd', 'japyx', 'klutz'], ['bortz', 'chivw', 'dunks', 'flegm', 'japyx'], ['bovld', 'freck', 'japyx', 'muntz', 'whigs'], ['breck', 'flows', 'japyx', 'vingt', 'zhmud'], ['brews', 'flock', 'japyx', 'vingt', 'zhmud'], ['brock', 'flews', 'japyx', 'vingt', 'zhmud'], ['brock', 'japyx', 'seqwl', 'vingt', 'zhmud'], ['brows', 'fleck', 'japyx', 'vingt', 'zhmud'], ['chimb', 'expwy', 'fjord', 'klutz', 'vangs'], ['chivw', 'expdt', 'flamb', 'grosz', 'junky'], ['chivw', 'expdt', 'flank', 'grosz', 'jumby'], ['chivw', 'expdt', 'furzy', 'jambs', 'klong'], ['chivw', 'expdt', 'jumby', 'klong', 'zarfs'], ['chivw', 'fjord', 'glaky', 'muntz', 'pbxes'], ['chivw', 'fjord', 'klutz', 'mangy', 'pbxes'], ['dhikr', 'expwy', 'fultz', 'gconv', 'jambs'], ['dumbs', 'fritz', 'gconv', 'japyx', 'whelk'], ['expdt', 'furzy', 'gconv', 'jambs', 'whilk'], ['expdt', 'gconv', 'jumby', 'whilk', 'zarfs'], ['flong', 'japyx', 'twick', 'verbs', 'zhmud'], ['flong', 'jarvy', 'pbxes', 'twick', 'zhmud'], ['frack', 'jowly', 'pbxes', 'vingt', 'zhmud'], ['frock', 'japyx', 'seqwl', 'vingt', 'zhmud'], ['frowl', 'jacky', 'pbxes', 'vingt', 'zhmud'], ['fultz', 'jacky', 'mordv', 'pbxes', 'whing']]

import time
st = time.time()

words = []
vowels = 'aeiou'

with open('words_alpha.txt', 'r') as file:
    lines = file.readlines() 

for line in lines:
    newLine = line.strip()
    sortedLine = sorted(newLine)
    if len(newLine) == 5 and len(set(newLine)) == len(newLine):
        vowelCount = 0
        for char in newLine:
            if char in vowels:
                vowelCount += 1
        if vowelCount < 2:
            is_anagram = False
            for word in words:
                if sorted(newLine) == sorted(word):
                    is_anagram = True
                    break
            if not is_anagram:
                words.append(newLine)

quintuples = []
for i, word1 in enumerate(words):
    print(i)
    for j in range(i+1, len(words)):
        if not any(char in word1 for char in words[j]):
            for k in range(j+1, len(words)):
                if not any(char in word1 or char in words[j] for char in words[k]):
                    for l in range(k+1, len(words)):
                        if not any(char in word1 or char in words[j] or char in words[k] for char in words[l]):
                            for m in range(l+1, len(words)):
                                if not any(char in word1 or char in words[j] or char in words[k] or char in words[l] for char in words[m]):
                                    quintuples.append([word1, words[j], words[k], words[l], words[m]])

et = time.time()
elapsed_time = et - st
print('Execution time:', round(elapsed_time, 4), 'seconds')
print('Total Words:', len(words))
print('Total Quintuples:', len(quintuples))
print(quintuples)

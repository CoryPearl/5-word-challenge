#time to compleat: 14.5399 seconds
#['ampyx', 'bortz', 'chivw', 'fjeld', 'gunks']

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

found_quintuple = False
for i, word1 in enumerate(words):
    if found_quintuple:
        break
    for j in range(i+1, len(words)):
        if found_quintuple:
            break
        if not any(char in word1 for char in words[j]):
            for k in range(j+1, len(words)):
                if found_quintuple:
                    break
                if not any(char in word1 or char in words[j] for char in words[k]):
                    for l in range(k+1, len(words)):
                        if found_quintuple:
                            break
                        if not any(char in word1 or char in words[j] or char in words[k] for char in words[l]):
                            for m in range(l+1, len(words)):
                                if not any(char in word1 or char in words[j] or char in words[k] or char in words[l] for char in words[m]):
                                    print("\nFound group: " + str([word1, words[j], words[k], words[l], words[m]]))
                                    found_quintuple = True
                                    break

et = time.time()
elapsed_time = et - st
print('Execution time:', round(elapsed_time, 4), 'seconds\n')

test_str = (input( "word: " ))
all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = dict(reversed(list(all_freq.items())))
print ("Count of all characters in the word is :\n "+ str(all_freq))
print("The reversed order dictionary : " + str(res))
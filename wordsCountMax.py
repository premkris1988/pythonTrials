name = input('Enter file:')
handle = open(name,'r')
text = handle.read()
words = text.split()
counts = dict()
for word in words:
    counts[word]=counts.get(word,0)+1
maxOccurance = max(counts.values())
for word,count in counts.items():   
    if count >= maxOccurance:
        print(str(word) +"\t" +str(count))

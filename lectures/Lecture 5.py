#q1 --> Most Frequent Word
def freqword(filepath):
    with open(filepath) as file:
 # Count word frequency
        counts = dict()
        for line in file:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word,0) + 1
 # Find the most frequent word
        maxcount = None
        maxword = None
        for word,count in counts.items():
            if maxcount is None or count > maxcount:
                maxword = word
                maxcount = count
 # Return the result
    return(f"The most frequent word is: {maxword}, and the number of times appeared is: {maxcount}")


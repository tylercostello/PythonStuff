import ast

#Loads list of words from text file
def loadWords(file_path): 
    with open(file_path) as f:
        words = f.read().split("\n")
    return words

#Pre-Generates list of editDistance deletes per word
def processWords(words, editDistance):
    output = {} 
    for i in words:
        print(i)
        variation = generateVariations(i, editDistance)
        for x in variation:
            if x not in output: 
                output[x] = [i]
            else: 
                if i not in output[x]:
                    output[x].append(i)
    f = open("variations.txt", "w+")
    f.write(str(output))
    f.close()
    return output
    
#Creates list of deletes
def generateVariations(word, editDistance):
    words = [word]
    outputs = [] 
    temp = None
    for x in range(editDistance):
        words = removeOne(words)
        outputs += words
    return outputs

#Generates list of all the deletes for a word
def removeOne(words): 
    output = []
    for x in words:
        for i in range(len(x)):
            output.append(x[:i] + x[i + 1:])  
    return output

#Loads pre generated deletes file
def loadPreGen(file_path):
    return ast.literal_eval(open(file_path).read())

#Checks a word, returns dictionary with frequency of matches
def checkWord(word, variations, edit_distance):
    words = generateVariations(word, edit_distance)
    results = {}
    for i in words:
        if i in variations:
            for x in variations[i]:
                if x in results:
                    results[x] += 1
                else:
                    results[x] = 1
    return results
    
#Example usage, spellchecking the word sunshin (sunshine)
if __name__ == "__main__":
    pregenned = loadPreGen("variations.txt")
    freq = checkWord("sunshin", pregenned, 2)
    print(max(freq, key=lambda x: freq[x]))
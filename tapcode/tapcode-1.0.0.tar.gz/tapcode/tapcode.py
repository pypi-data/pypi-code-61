#!/usr/bin/env python

# polybe square 
polybe = [
    ["A","B","C","D","E"],
    ["F","G","H","I","J"],
    ["L","M","N","O","P"],
    ["Q","R","S","T","U"],
    ["V","W","X","Y","Z"]
]

def prepare_sentence(sentence):
    """
    Prepare a sentence for the encryption
    
    Args: 
        sentence (string): Sentences to encode.
    
    return:
        string. Cleaned sentences.

    """

    accent = ["âà", "éèêë", "îï", "ô", "ûü", "ç"]
    ascii = ["A", "E", "I", "O", "U", "C"]
    i=0
    for word in accent: # Replacing accented characters possible
        for letter in word:
            sentence = sentence.replace(letter, ascii[i])
        i += 1
    for letter in "',-;:!?":  # Remove punctuation
        sentence = sentence.replace(letter, "")
    sentence = sentence.upper()

    return sentence.split(".")

def decipher(code,wordSep,sentenceSep):
    """
    Decipher tapcode sentences.

    Args: 
        code : Tapcode sentence to decipher.
        wordSep (string) : Separator for word (basically just a space by default)
        sentenceSep (string) : Separator for sentence (basically just a dot by default)

    Return:
        string. Deciphered tapcode sentences.

    """
    deciphered = []
        
    for p in code.split(sentenceSep) :
        for word in p.strip().split(wordSep) :
            splitting = [(word[l],word[l+1]) for l in range(0,len(word),2)]  

            for tuple in splitting :
                deciphered.append(polybe[int(tuple[0])-1][int(tuple[1])-1]) # minus one because index start at 0 but number in code start at 1
            deciphered.append(wordSep)
        deciphered.append(sentenceSep)

    return "".join(deciphered)

def encipher(sentence,wordSep,sentenceSep):
    """
    encipher a sentence with tapcode system

    args:
        sentence (list) : List of sentence
        wordSep (string) : Separator for word (basically just a space by default)
        sentenceSep (string) : Separator for sentence (basically just a dot by default)
    
    return:
        string. Enciphered sentences.
    """
    sentence = prepare_sentence(sentence)

    encipheredText = []

    for p in sentence :
        for word in p.strip().split(" "):
            for letter in word:
                for i in range(len(polybe)):
                    for j in range(len(polybe[i])):
                        if polybe[i][j] == letter:
                            encipheredText.append(str(i+1)+str(j+1))
            encipheredText.append(wordSep)
        encipheredText.append(sentenceSep)
    

    return "".join(encipheredText)


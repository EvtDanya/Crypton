import argparse
from prettytable import PrettyTable

parser = argparse.ArgumentParser()

def readFile(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def splitText(text, size):
    alphabet = {',','.',';','_','-','/',}
    splitText = text.split()
    for symb in alphabet:
        splitText = [word for line in splitText for word in line.split(symb)]
    for word in splitText:
        if word == '':
            splitText.remove(word)
    splitText = list(filter(None, splitText))
    for i in range(len(splitText)):
        while True:
            word = splitText[i]
            if len(word) > size:
                splitText.append(word[0:size])
                splitText[i] = word[size:]
            else:
                break
    return splitText

def countMatches(text, accuracy):
    size = len(text)
    frequency = {}
    for word in text:
        count = frequency.get(word,0)
        frequency[word] = count + 1
    for word in frequency.keys():
        frequency[word] = round(frequency[word] * 100 / size, accuracy)
    return frequency

def sortMatches(text):
    return {k: v for k, v in sorted(text.items(), key=lambda item: item[1], reverse=True)}
    
if __name__ == '__main__': 
    
    print('                       _              ')
    print('  ___ _ __ _   _ _ __ | |_ ___  _ __  ')
    print(' / __| \'__| | | | \'_ \| __/ _ \| \'_ \ ')
    print('| (__| |  | |_| | |_) | || (_) | | | |')
    print(' \___|_|   \__, | .__/ \__\___/|_| |_|')
    print('           |___/|_|   \n')
    
    parser.add_argument('-f', type=str, required=True, help='The file containing the text for cryptoanalysis')    
    parser.add_argument('-s', type=int, default=1, required=False, help='Word\'s size (if not specified, the frequency of letters is investigated)')
    parser.add_argument('-a', type=int, default=3, required=False, help='Accuracy of frequency calculations (must be a number)')
    parser.add_argument('-sort', action="store_true", required=False, help='Sorting by ascending frequency values')
    
    args = parser.parse_args()  
        
    text = readFile(args.f)
    match = splitText(text,args.s)
    frequency = countMatches(match, args.a)
    if (args.sort):
        frequency=sortMatches(frequency)
    
    print('Length of input text: ' + str(len(match)))
    t = PrettyTable(['Word', 'Frequency (in %)'])
    t.align["Word"] = "l"
    t.align["Frequency (in %)"] = "r"
    for word in frequency:
        t.add_row([word, frequency[word]])
        
    print(t)
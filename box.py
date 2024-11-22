import pdb

class node:
    next = [None] * 26
    leaf = False

list = node()
puzzle = ""
viableWords = []

def main():
    print("running main...")
    # dictionary file
    #     iterate through and create a 26 node tree
    buildDict("words_alpha.txt")

    # ingest puzzle sides
    puzzle = input("Enter puzzle letters, begin from top left corner: ")

    # follow game logic, recursively test each path
    for i in range (0, 12):
        discoverWord(puzzle[i], i, puzzle)

    print(f"list of viable words: {viableWords}")
    '''
    every new letter that's considered
        check if path exists for it in dictionary tree 
    if a word is discovered, add it to a word bank

    make array of answers
    with the word bank
        pop first word from wordlist, add to word array
        grab last letter of first word
        iterate through rest of list
    no no no no, it's gonna need to be recursive
    this might take some more thought than expected

    '''

def discoverWord(word, position, puzzle):
    if not letterExists(word):
        print(f"not a real word: {word}")
        return
    if (wordIsLeaf(word)):
        viableWords.append(word)

    # snap position to next side
    position = ((position + 3) // 3) * 3

    # try 9 valid choices for next letter
    for i in range(position, position + 9):
        # pdb.set_trace()
        discoverWord(word + puzzle[i%12], i%12, puzzle)

# word tree:
# 26-tree
# each node has:
    # 26 childeren nodes
    # boolean (leaf or not)
    # boolean (valid or not, does not indicate anything about childeren)
# functions:
# wordIsLeaf(): traverse down tree, if node you landed on is a leaf return true
# wordIsValid(): similar but not the same.  if node you land on is the end of a valid word, return true.  does not indicate anything about leaf status though
    # this function must also not crash when word is nonsense (handle null pointer errors!)
# this is hard.  leafs are always valid.  but valid words are not always leafs.  


def buildDict(filename):
    counter = 0
    with open(filename) as file:
        for word in file:
            if counter % 10000 == 0: print(f"inserting {counter}th word {word.rstrip()} into trie...")
            insert(word.rstrip())
            counter += 1

def insert(word):
    current = list 
    for letter in word:
        # print(f"current letter: {letter}")
        index = ord(letter) - ord('a')
        # print(f"index: {index}")
        if not current.next[index]:
            current.next[index] = node()
            current = current.next[index]
    current.leaf = True

def wordIsLeaf(word):
    # traverse down word tree and check if where you land is a leaf
    current = list 
    for letter in word:
        index = ord(letter) - ord('a')
        if not current.next[index]:
            return False
        current = current.next[index]
    return current.leaf

def letterExists(wor):
    # similar but not the same.  if node you land on is the end of a valid word, return true.  does not indicate anything about leaf status though
    # this function must also not crash when word is nonsense (handle null pointer errors!)
    # traverse down word tree and check if where you land is a leaf
    # Note: words that are passed in here will frequently be partial words, hence 'wor'
    current = list 
    for letter in wor:
        index = ord(letter) - ord('a')
        if not current.next[index]:
            return False
        current = current.next[index]
    return current != None

# RAMIN: tweak discoverWord to deal with the fact that leafs can have children in this implementation

main()
# initial thoughts

puzzle = ""

def main():

    # dictionary file
    #     iterate through and create a 26 node tree

    # ingest puzzle sides
    puzzle = input("Enter puzzle letters, begin from top left corner: ")
    sides = [puzzle[0:3], puzzle[3:6], puzzle[6:9], puzzle[9:12]]

    # follow game logic, recursively test each path
    for side in sides: 
        for letter in side:
            discoverWord([letter], puzzle, 0) 

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

def discoverWord(word, position):
    if (wordIsValid(word)):
        addToWordList(word) # if we want leafs only, move this to the next if
    else:
        return
    if (wordIsLeaf(word)):
        return

    # snap position to next side
    position = ((position + 3) // 3) * 3

    # try 9 valid choices for next letter
    for i in range(position, (position + 9) % 12):
        discoverWord(word + puzzle[i], i)

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


# return next valid letter position (going clockwise)
def next(current): 
    n = current % 12
    if (n + 1) // 3 == n // 3:
        return (n + 3) // 3
    return (n + 1) % 12

    # 0 3
    # 1 3
    # 2 3
    # 3 6
    # 4 6
    # 5 6
    # 6 9
    # 7 9
    # 8 9
    # 9 0
    # 10 0
    # 11 0
    
    # nextPossible:
        # if 0, 1, or 2 you can only select 3-11
        # or you must "round up" to the next side then iterate numerically from there
        # I think this is the key: ((n+3) // 3) * 3
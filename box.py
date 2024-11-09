# initial thoughts


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

def discoverWord(letters, puzzle, position):
    # BASE CASE: if the letters in a word lead it down a path in the dictTree that doesn't exist, return false

    # if letters form a complete word, add word to wordBank (but do not return!)
        # (a complete word is a word whose letters lead it to a leaf in the dictionary tree)

    # test 9 possible next letter options
    for i in range(position, position + 12):
        nextPos = next(position)

    discoverWord(letters + puzzle[nextPos], puzzle, nextPos)
    pass

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
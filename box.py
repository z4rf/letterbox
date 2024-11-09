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
            discoverWords([letter], puzzle, 0) 

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

def discoverWords(letters, puzzle, position):
    # BASE CASE: if the letters in a word lead it down a path in the dictTree that doesn't exist, return false

    # if letters form a complete word, add word to wordBank (but do not return!)
        # (a complete word is a word whose letters lead it to a leaf in the dictionary tree)

    # obtain next letter
        # jump to next possible side and iterate through its letters
        # position += 1
        # while ((currentIndex + 1) % 12) // 3 != currentIndex // 3
        # ...no
        # 
        # nextPosition = (position + 3) // 3
    # discoverWords(letters + puzzle[nextPos], puzzle, nextPos)
    pass

# return next valid letter position (going clockwise)
def next(n): 
    if ((n + 1) % 12) // 3 == n // 3:
        return (n + 3) // 3
    return (n + 1) % 12
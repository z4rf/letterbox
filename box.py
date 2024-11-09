# initial thoughts


# dictionary file
#     iterate through and create a 26 node tree

# ingest puzzle sides
puzzle = input("Enter puzzle letters, begin from top left corner: ")
sides = [puzzle[0:3], puzzle[3:6], puzzle[6:9], puzzle[9:12]]

# follow game logic, recursively test each path
for side in puzzle: 
    for letter in side:
        discoverWords() 

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
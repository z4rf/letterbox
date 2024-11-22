

class dictTree:
    
    next = {
        "a": None, 
        "b": None, 
        "c": None,
        "d": None,
        "e": None,
        "f": None,
        "g": None,
        "h": None,     
        "i": None,
        "j": None,
        "k": None,
        "l": None,
        "m": None,
        "n": None,
        "o": None,
        "p": None,
        "q": None,
        "r": None,
        "s": None,
        "t": None,
        "u": None,
        "v": None,
        "w": None,
        "x": None,
        "y": None,
        "z": None
    }

    leaf = False
    valid = False

    def wordIsLeaf(word):
        # traverse down word tree and check if where you land is a leaf
        pass
    
    def wordIsValid(word):
        # similar but not the same.  if node you land on is the end of a valid word, return true.  does not indicate anything about leaf status though
        # this function must also not crash when word is nonsense (handle null pointer errors!)
        pass

    def buildDict(filename):

        with open(filename) as file:
            for word in file:
                addToTree(word)
    
    def addToTree(word):
        

import pdb
import time
import sys

class node:
    def __init__(self): 
        self.next = [None] * 26
        self.leaf = False

dictionary = node()
puzzle = ""
viableWords = []
solutions = []

def main():

    # wordlist sourced from: https://github.com/dwyl/english-words
    buildDict("popular.txt")

    puzzle = sys.argv[1]
    numWords = int(sys.argv[2])

    # follow game logic, recursively test each path
    for i in range (0, 12):
        discoverWord(puzzle[i], i, puzzle)

    # print(f"list of viable words: {viableWords}")
    
    for i in range(0, numWords):
        # print(f"trying chains of length {i}...")
        for word in viableWords:
            findChain([word], viableWords, i, puzzle)
        if len(solutions) > 0:
            print(f"shortest solutions of length {i+1} found: ")
            break
    
    # convert to set and back to remove duplicate entries (which are lists) from solution list
    tupleList = []
    for tempList in solutions:
        tempList.sort()
        tupleList.append(tuple(tempList))
    
    finalList = list(set(tupleList))

    print(str(finalList))

    

def discoverWord(word, position, puzzle):
    if not letterExists(word):
        return
    if (wordIsLeaf(word)):
        viableWords.append(word)

    # snap position to next side
    position = ((position + 3) // 3) * 3

    # try 9 valid choices for next letter
    for i in range(position, position + 9):
        discoverWord(word + puzzle[i%12], i%12, puzzle)

# read from dictionary file and populate trie with words
def buildDict(filename):
    counter = 0
    with open(filename) as file:
        for word in file:
            # if counter % 10000 == 0: print(f"inserting {'{:,}'.format(counter)}th word {word.rstrip()} into trie...")
            insert(word.rstrip())
            counter += 1

# insert word into trie
def insert(word):
    current = dictionary 
    for letter in word:
        index = ord(letter) - ord('a')
        if not current.next[index]:
            current.next[index] = node()
        current = current.next[index]
    current.leaf = True


# traverse down word tree and check if where you land is a leaf
def wordIsLeaf(word):
    current = dictionary 
    for letter in word:
        index = ord(letter) - ord('a')
        if not current.next[index]:
            return False
        current = current.next[index]
    return current.leaf

# similar to wordIsLeaf(word) but not the same.  if node you land on is the end of a valid word, return true.  
# does not indicate anything about leaf status though this function must also not crash when word is 
# nonsense (handle null pointer errors!)
# Note: words that are passed in here will frequently be partial words, hence 'wor'
def letterExists(wor):
    current = dictionary 
    for letter in wor:
        index = ord(letter) - ord('a')
        if not current.next[index]:
            return False
        current = current.next[index]
    return current != None

# ==========

def findChain(chain, bank, depth, puzzle):
    if len(chain) > depth:
        return

    if checkSolution(chain, puzzle):
        # print(f"solution found! {str(chain)}")
        temp = chain.copy()
        solutions.append(temp)
        return

    for word in bank:
        lastLetter = chain[-1][-1]
        
        if word in chain:
            continue

        nextWord = None
        if lastLetter == word[0]:
            nextWord = word
        if not nextWord:
            continue
        chain.append(nextWord)
        findChain(chain, bank, depth, puzzle)
        chain.remove(nextWord)

# given an array of words, ensure they use every letter of the puzzle
def checkSolution(words, puzzle):
    combined = "".join(words)
    for letter in puzzle: 
        if letter not in combined:
            return False
    return True


main()

# a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
# 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25


# for the puzzle 'tlqsrubfiemo' all possible words are:
# ['t', 'ts', 'tsi', 'tsetse', 'tsetses', 'tsere', 'tsotsi', 'tst', 'tr', 'trf', 'tri', 'tries', 'trier', 'trim', 'trims', 'trio', 'triol', 'triols', 'triole', 'triolet', 'triolets', 'trios', 'triose', 'trioses', 'triosteum', 'trior', 'triobol', 'trit', 'tritium', 'tritiums', 'trite', 'tritest', 'triter', 'tritolo', 'tritor', 'tritorium', 'trilit', 'trilite', 'trilium', 'trilobe', 'triquet', 'trisetum', 'trisetose', 'trist', 'tristful', 'triste', 'triumf', 'tret', 'trets', 'tretis', 'tres', 'tresis', 'trest', 'treble', 'treblet', 'trebles', 'tref', 'trefoil', 'trefoils', 'trefle', 'treitre', 'trot', 'trots', 'trotol', 'trouble', 'troubles', 'troubler', 'troue', 'trout', 'trouts', 'troutful', 'troutiest', 'troutier', 'trouter', 'troft', 'troilite', 'troilites', 'troilism', 'trois', 'trt', 'tu', 'tub', 'tube', 'tubelet', 'tubes', 'tuber', 'tuberosities', 'tuberose', 'tuberoses', 'tubeform', 'tubeful', 'tublet', 'tubs', 'tubster', 'tubuli', 'tubule', 'tubulet', 'tubules', 'tubulose', 'tuft', 'tufts', 'tuftiest', 'tuftier', 'tufter', 'tui', 'tuis', 'tuism', 'tue', 'tuebor', 'tum', 'tumtum', 'tumli', 'tumuli', 'tumulose', 'tumbester', 'tumble', 'tumbles', 'tumbler', 'tumblerful', 'tumbril', 'tumbrils', 'tumbrel', 'tumbrels', 'tut', 'tuts', 'tutster', 'tutu', 'tutiorism', 'tutiorist', 'tute', 'tutele', 'tutelo', 'tutor', 'tutorism', 'tutorer', 'tulsi', 'tulu', 'tule', 'tules', 'tuque', 'tuques', 'tuquoque', 'tb', 'tbs', 'tfr', 'ti', 'tie', 'ties', 'tier', 'tierer', 'tim', 'timbe', 'timbestere', 'timber', 'timberer', 'timbo', 'timbre', 'timbrel', 'timbrels', 'timbreler', 'timbres', 'timist', 'tiou', 'tit', 'tits', 'titre', 'titres', 'tituli', 'titule', 'titfer', 'titi', 'tities', 'titis', 'tite', 'titer', 'titoism', 'titoist', 'til', 'tils', 'tilsit', 'tile', 'tiles', 'tiler', 'tileries', 'tis', 'tire', 'tires', 'tiresol', 'tirer', 'tiro', 'tirolese', 'tiros', 'tirl', 'tirls', 'tiu', 'te', 'tetrol', 'tetrole', 'tetrose', 'tetrobol', 'tetum', 'tete', 'tetel', 'tetotum', 'tetotums', 'tel', 'telfer', 'teli', 'telium', 'tele', 'teletube', 'teles', 'telesis', 'teleses', 'teleseism', 'telesm', 'teleut', 'teleuto', 'teleutosori', 'teleutoform', 'telei', 'teleiosis', 'telos', 'teloi', 'test', 'tests', 'testril', 'testule', 'testiest', 'testier', 'testiere', 'testitis', 'testis', 'teste', 'testes', 'tester', 'testor', 'ter', 'teri', 'teretism', 'terete', 'teres', 'tereu', 'term', 'terms', 'termite', 'termites', 'tertio', 'tertium', 'tebet', 'tebu', 'tef', 'teil', 'teise', 'tm', 'to', 'tot', 'tots', 'totum', 'tote', 'totes', 'toter', 'toto', 'totoro', 'tol', 'tolsel', 'tolsester', 'tolu', 'toluol', 'toluols', 'toluole', 'toluoles', 'tolite', 'tole', 'toles', 'tolerism', 'toque', 'toquet', 'toquets', 'toques', 'tos', 'tost', 'tor', 'torfel', 'torfle', 'tori', 'tories', 'toriest', 'torilis', 'tore', 'toret', 'tores', 'torero', 'toreros', 'toro', 'torotoro', 'toros', 'torosities', 'torose', 'tort', 'torts', 'tortue', 'tortuosities', 'tortuose', 'tortie', 'tortil', 'tortile', 'tortis', 'torte', 'tortes', 'tortor', 'tortoise', 'tortoises', 'torque', 'torques', 'torqueses', 'torquer', 'tou', 'tout', 'touts', 'touter', 'tob', 'tobe', 'tofore', 'toft', 'tofts', 'tofter', 'tofu', 'toi', 'toit', 'toits', 'toitoi', 'toil', 'toils', 'toilful', 'toile', 'toilet', 'toilets', 'toiletries', 'toiles', 'toiler', 'toise', 'toist', 'l', 'ls', 'lst', 'lr', 'lu', 'lub', 'lube', 'lubes', 'lubritorium', 'lui', 'luite', 'luis', 'lue', 'lues', 'lum', 'lums', 'lumut', 'lumber', 'lumberer', 'lumisterol', 'luo', 'lut', 'lutist', 'lutists', 'lute', 'lutetium', 'lutetiums', 'lutelet', 'lutes', 'luter', 'luteum', 'lutose', 'lulu', 'lb', 'lbs', 'lf', 'li', 'lie', 'lies', 'liest', 'lier', 'lieu', 'lieue', 'lieut', 'lief', 'liefest', 'liefer', 'lim', 'limli', 'limu', 'limuli', 'limb', 'limber', 'limberest', 'limberer', 'limbo', 'limbos', 'limbs', 'limbu', 'limiest', 'limier', 'limit', 'limits', 'limites', 'limiter', 'limitor', 'lit', 'lits', 'litster', 'litre', 'litres', 'litu', 'litui', 'lituite', 'lituites', 'liti', 'lite', 'lites', 'liter', 'literose', 'litotes', 'lilies', 'lilium', 'lile', 'liles', 'liq', 'liquet', 'liquer', 'liquor', 'liquorist', 'liquorer', 'lis', 'lisiere', 'lise', 'lisere', 'list', 'lists', 'listful', 'listel', 'listels', 'lister', 'listeriosis', 'listerioses', 'listerism', 'lisle', 'lisles', 'lir', 'lire', 'lirot', 'le', 'let', 'lets', 'letrist', 'lete', 'leto', 'les', 'lese', 'lest', 'leste', 'lester', 'leslie', 'ler', 'lere', 'lerot', 'leu', 'lebes', 'left', 'lefts', 'lefties', 'leftism', 'leftisms', 'leftist', 'leftists', 'leftest', 'lefter', 'lefsel', 'lei', 'leis', 'leister', 'leisterer', 'lm', 'lo', 'lot', 'lots', 'lotrite', 'lotium', 'lote', 'loto', 'lotos', 'lotoses', 'lotor', 'loli', 'lolium', 'lolo', 'loq', 'lose', 'losel', 'losels', 'loselism', 'loses', 'loser', 'lost', 'lor', 'lori', 'lories', 'loriot', 'lorilet', 'loris', 'lorises', 'lore', 'lorel', 'lorelei', 'lores', 'loro', 'loros', 'lou', 'louie', 'louies', 'louis', 'louise', 'lout', 'louts', 'loutre', 'louter', 'loulu', 'lob', 'lobe', 'lobelet', 'lobes', 'lobo', 'lobolo', 'lobolos', 'lobos', 'lobose', 'lobs', 'lobster', 'lobuli', 'lobule', 'lobules', 'lobulose', 'lof', 'loft', 'lofts', 'loftiest', 'loftier', 'lofter', 'loiter', 'loiterer', 'lois', 'loir', 'q', 'qs', 'qr', 'qu', 'qui', 'quiet', 'quiets', 'quieti', 'quietism', 'quietisms', 'quietist', 'quietists', 'quietest', 'quieter', 'quim', 'quit', 'quits', 'quitu', 'quite', 'quito', 'quiles', 'quileses', 'quileute', 'quis', 'quist', 'quistiti', 'quisle', 'quisler', 'quisqueite', 'quirite', 'quirites', 'quire', 'quires', 'quirt', 'quirts', 'quirl', 'que', 'quet', 'quelite', 'ques', 'quest', 'quests', 'questrist', 'questful', 'quester', 'questor', 'queries', 'querier', 'querist', 'querists', 'querele', 'queres', 'querl', 'queue', 'queues', 'queuer', 'quei', 'quo', 'quot', 'quotum', 'quotieties', 'quoties', 'quote', 'quotes', 'quoter', 'quos', 'quor', 'quoit', 'quoits', 'quoiter', 'qe', 'qeri', 'qere', 'qm', 's', 'sb', 'sf', 'sfm', 'si', 'sie', 'siest', 'sier', 'sim', 'sims', 'simsim', 'simul', 'simulium', 'simule', 'simuler', 'simblum', 'simblot', 'simiesque', 'similimum', 'similiter', 'simile', 'similes', 'similor', 'siol', 'sit', 'sits', 'situ', 'siti', 'sitio', 'site', 'sites', 'sitosterol', 'sil', 'silique', 'siliques', 'siliquose', 'sile', 'silo', 'silos', 'siloist', 'sis', 'sisi', 'sise', 'sisel', 'sises', 'sist', 'sister', 'sir', 'siris', 'sire', 'sires', 'siros', 'sium', 'siums', 'se', 'set', 'sets', 'setule', 'setulose', 'setier', 'setose', 'setout', 'setouts', 'sel', 'sels', 'self', 'selfs', 'sele', 'seq', 'sequel', 'sequels', 'sequest', 'sequester', 'seseli', 'sestuor', 'sesti', 'sestet', 'sestets', 'sestertium', 'sestole', 'sestolet', 'sesqui', 'ser', 'serb', 'serf', 'serfs', 'seri', 'series', 'serio', 'seriosities', 'serioso', 'sere', 'seres', 'serest', 'serer', 'sero', 'serosities', 'serositis', 'serose', 'sert', 'sertum', 'sertulum', 'sertule', 'sebum', 'sebums', 'sei', 'seit', 'seis', 'seise', 'seises', 'seiser', 'seism', 'seisms', 'seismism', 'seismisms', 'seisor', 'sm', 'sml', 'smriti', 'smut', 'smuts', 'smit', 'smite', 'smites', 'smiter', 'smile', 'smilet', 'smiles', 'smiler', 'smileful', 'smiris', 'so', 'sot', 'sots', 'sotie', 'soter', 'soteres', 'sotol', 'sotols', 'sol', 'sols', 'solstitium', 'soluble', 'solubles', 'solum', 'solums', 'solutio', 'solute', 'solutes', 'soli', 'solio', 'soliloquies', 'soliloquise', 'soliloquiser', 'soliloquist', 'soliloquium', 'solist', 'soliste', 'sole', 'soles', 'soler', 'soleret', 'solerets', 'solert', 'soleil', 'solo', 'solos', 'soloist', 'soloists', 'sos', 'sosie', 'soso', 'sosquil', 'sorb', 'sorbet', 'sorbets', 'sorbol', 'sorbose', 'sorboses', 'sorbs', 'sori', 'sorite', 'sorites', 'sore', 'sorel', 'sorels', 'sores', 'sorest', 'sorer', 'sorosil', 'sorosis', 'sorosises', 'sorose', 'soroses', 'sororities', 'sort', 'sorts', 'sortie', 'sorties', 'sortes', 'sorter', 'sou', 'soubriquet', 'soum', 'souter', 'soul', 'souls', 'soulful', 'sob', 'sober', 'soberest', 'soberer', 'sobeit', 'sobole', 'soboles', 'sobs', 'sobrieties', 'sobriquet', 'sobriquets', 'sofer', 'soft', 'softs', 'softie', 'softies', 'softest', 'softer', 'soil', 'soils', 'soiliest', 'soilier', 'soir', 'st', 'str', 'striolet', 'strit', 'stre', 'stret', 'streit', 'streite', 'strout', 'strobe', 'strobes', 'stroil', 'stu', 'stub', 'stube', 'stuber', 'stubs', 'stue', 'stum', 'stums', 'stumble', 'stumbles', 'stumbler', 'stumblebum', 'stut', 'stulm', 'sties', 'stim', 'stimuli', 'stimulose', 'stimies', 'stite', 'stilb', 'stilbestrol', 'stilbum', 'stile', 'stilet', 'stiles', 'stir', 'stire', 'stet', 'stets', 'stele', 'steles', 'ster', 'steri', 'sterilities', 'sterilise', 'steriliser', 'sterile', 'stere', 'steres', 'stereum', 'stero', 'sterol', 'sterols', 'stert', 'stertor', 'sterlet', 'sterlets', 'stm', 'stot', 'stoter', 'stolist', 'stole', 'stoles', 'stor', 'stories', 'storier', 'store', 'stores', 'storer', 'storm', 'storms', 'stormful', 'stormiest', 'stormier', 'stout', 'stouts', 'stoutest', 'stouter', 'stob', 'stobs', 'stof', 'stoit', 'stoiter', 'sl', 'slub', 'slubs', 'sluit', 'slue', 'slues', 'sluer', 'slum', 'slums', 'slumber', 'slumberful', 'slumberer', 'slut', 'sluts', 'sliest', 'slier', 'slim', 'slims', 'slimsiest', 'slimsier', 'slimiest', 'slimier', 'slit', 'slits', 'slite', 'slirt', 'slete', 'sleb', 'slot', 'slots', 'slote', 'slob', 'slobs', 'sq', 'sqrt', 'squit', 'squirism', 'squire', 'squiret', 'squirelet', 'squires', 'squirm', 'squirms', 'squirmiest', 'squirmier', 'squirt', 'squirts', 'squirter', 'squirl', 'squet', 'r', 'rf', 'rfs', 'rie', 'riel', 'riels', 'ries', 'rier', 'rim', 'rims', 'rimu', 'rimulose', 'rimiest', 'rimier', 'rio', 'riot', 'riots', 'riotise', 'riotist', 'rioter', 'rit', 'rite', 'rites', 'rile', 'riles', 'risberm', 'rise', 'rises', 'riser', 'rist', 'ristori', 'risqu', 'risque', 'riroriro', 're', 'ret', 'rets', 'retries', 'retrier', 'retrim', 'retrims', 'retro', 'retrot', 'retros', 'retroform', 'retube', 'retumble', 'retie', 'reties', 'retier', 'retimber', 'retile', 'retire', 'retires', 'retirer', 'rete', 'retest', 'retests', 'retore', 'retort', 'retorts', 'retorter', 'rel', 'relies', 'relier', 'relief', 'reliefer', 'reliefs', 'relimit', 'relit', 'reliquism', 'relique', 'reliques', 'relist', 'relists', 'relet', 'relets', 'reles', 'relot', 'relose', 'relost', 'req', 'requit', 'requite', 'requites', 'requiter', 'requiteful', 'requisite', 'requisites', 'requisitor', 'require', 'requires', 'requirer', 'request', 'requests', 'requester', 'requestor', 'requote', 'res', 'resit', 'resilium', 'resile', 'resiles', 'resist', 'resists', 'resistful', 'resister', 'resistor', 'reset', 'resets', 'reself', 'resequester', 'reseise', 'reseiser', 'resmile', 'resoluble', 'resolute', 'resolutes', 'resolutest', 'resoluter', 'resole', 'resoles', 'resorb', 'resorbs', 'resort', 'resorts', 'resorter', 'resoil', 'rest', 'rests', 'restr', 'restful', 'restio', 'restitue', 'restitute', 'restitutor', 'restis', 'restir', 'restes', 'rester', 'restore', 'restores', 'restorer', 'reslot', 'rerise', 'rerises', 'rerose', 'reroute', 'reroutes', 'rerob', 'rerobe', 'reub', 'reuel', 'reutilise', 'reb', 'rebel', 'rebels', 'rebelief', 'rebeset', 'rebote', 'reboso', 'rebosos', 'rebore', 'rebob', 'reboil', 'reboils', 'reboiler', 'reboise', 'reblue', 'reblister', 'reblot', 'rebs', 'rebut', 'rebuts', 'rebute', 'ref', 'refete', 'refel', 'refels', 'refer', 'reforfeit', 'reforest', 'reforests', 'reform', 'reforms', 'reformism', 'reformist', 'reft', 'refl', 'reflies', 'reflet', 'reflets', 'refs', 'refr', 'refries', 'refreit', 'refuel', 'refuels', 'refute', 'refutes', 'refuter', 'rei', 'reim', 'reit', 'reiter', 'reis', 'reist', 'reister', 'rm', 'rms', 'ro', 'rot', 'rots', 'rotse', 'rotulet', 'roti', 'rote', 'rotes', 'roter', 'roto', 'rotos', 'rotor', 'rolf', 'rolfe', 'role', 'roles', 'roquist', 'roque', 'roquet', 'roquets', 'roques', 'roquer', 'roquefort', 'ros', 'rosiest', 'rosier', 'rosieresite', 'rose', 'roset', 'rosets', 'rosetum', 'rosel', 'roselite', 'roselet', 'roses', 'roseries', 'rosoli', 'rosolio', 'rosolios', 'rosolite', 'rostel', 'roster', 'rori', 'rort', 'roub', 'rouble', 'roubles', 'roue', 'roues', 'rouerie', 'rout', 'routs', 'routier', 'route', 'routes', 'router', 'rob', 'robe', 'robes', 'rober', 'robert', 'roberts', 'roberto', 'robot', 'robots', 'robotries', 'robotism', 'robotisms', 'robotesque', 'roble', 'robles', 'robs', 'roi', 'roit', 'roitelet', 'roil', 'roils', 'roiliest', 'roilier', 'roist', 'roister', 'roisterer', 'rt', 'rti', 'rte', 'rle', 'u', 'uberties', 'ufer', 'ufo', 'ufos', 'ufs', 'ui', 'uit', 'um', 'umset', 'umu', 'umbel', 'umbels', 'umbeset', 'umber', 'umbo', 'umbos', 'umble', 'umbles', 'umbriel', 'umbril', 'umbre', 'umbret', 'umbrel', 'umbrere', 'umbrose', 'umist', 'umiri', 'ut', 'uts', 'utu', 'utum', 'uti', 'util', 'utilities', 'utilise', 'utilises', 'utiliser', 'utile', 'ute', 'uteri', 'uteritis', 'utero', 'ulster', 'ulsterite', 'ulu', 'ululu', 'ulitis', 'ule', 'b', 'be', 'bet', 'bets', 'betso', 'betrim', 'betutor', 'betulites', 'betimber', 'betis', 'betise', 'betises', 'betire', 'bete', 'betel', 'betels', 'betes', 'betoil', 'bel', 'bels', 'belsire', 'belue', 'belute', 'belfries', 'belie', 'belies', 'belier', 'belief', 'beliefs', 'belite', 'belili', 'beliquor', 'belis', 'beleft', 'belout', 'bequest', 'bequests', 'bequote', 'bes', 'besit', 'beset', 'besets', 'besmut', 'besmuts', 'besmile', 'besmiles', 'besot', 'besots', 'besort', 'besoul', 'besoil', 'best', 'bests', 'bestir', 'bester', 'bestore', 'bestorm', 'besluit', 'besquirt', 'ber', 'berber', 'berberi', 'berberis', 'beri', 'bere', 'beret', 'berets', 'beresite', 'bereft', 'berm', 'berms', 'berob', 'bert', 'bertie', 'berloque', 'beblister', 'beblot', 'bef', 'before', 'befoul', 'befouls', 'befoulier', 'befouler', 'beflum', 'beflout', 'befret', 'befrets', 'bm', 'bo', 'bot', 'bots', 'botulism', 'botulisms', 'botflies', 'boti', 'bote', 'botete', 'botel', 'botels', 'boteler', 'boterol', 'bol', 'bolster', 'bolsterer', 'bolis', 'bole', 'boleti', 'bolete', 'boletes', 'boles', 'bolero', 'boleros', 'boleite', 'bolo', 'bolos', 'boloism', 'bos', 'bose', 'boser', 'bosque', 'bosquet', 'bosquets', 'bosques', 'bor', 'bori', 'borities', 'boris', 'borism', 'bore', 'borel', 'borele', 'bores', 'borer', 'boreism', 'boro', 'bororo', 'bort', 'borts', 'boubou', 'bouet', 'bout', 'bouts', 'boutre', 'boutique', 'boutiques', 'boutel', 'boutefeu', 'bouto', 'boul', 'boule', 'boules', 'bouquet', 'bouquets', 'bouquetiere', 'bob', 'bobet', 'bobo', 'bobotie', 'bobol', 'boblet', 'bobs', 'boite', 'boites', 'boil', 'boils', 'boiler', 'boilerful', 'bois', 'boise', 'boiserie', 'boiseries', 'boist', 'bt', 'btu', 'btise', 'bl', 'bls', 'blub', 'blufter', 'bluism', 'blue', 'bluet', 'bluets', 'bluetit', 'blues', 'bluest', 'bluer', 'bliest', 'blier', 'blit', 'blitum', 'blite', 'blites', 'blist', 'blister', 'blirt', 'blet', 'blets', 'blest', 'blere', 'bleu', 'bleb', 'blebs', 'blo', 'blot', 'blots', 'blote', 'blore', 'blout', 'blob', 'blobs', 'bs', 'bsf', 'br', 'brie', 'bries', 'brier', 'brief', 'briefest', 'briefer', 'briefs', 'brim', 'brims', 'brimse', 'brimborium', 'brimful', 'brio', 'briolet', 'brios', 'brit', 'brits', 'brite', 'brique', 'briquet', 'briquets', 'brise', 'brises', 'briseis', 'brist', 'bristol', 'bristols', 'brisque', 'bret', 'breloque', 'brest', 'brere', 'brei', 'bro', 'brot', 'brotel', 'bros', 'brosimum', 'brose', 'broses', 'brosot', 'brob', 'broil', 'broils', 'broiler', 'brl', 'bu', 'bub', 'bube', 'bubo', 'bubos', 'bubs', 'bufo', 'buist', 'bum', 'bums', 'bumbelo', 'bumbo', 'bumble', 'bumbles', 'bumbler', 'bumf', 'bumfs', 'but', 'buts', 'butut', 'bututs', 'bute', 'butolism', 'bul', 'bulse', 'bulb', 'bulbel', 'bulbels', 'bulbotuber', 'bulbose', 'bulblet', 'bulbs', 'bulbul', 'bulbuls', 'bulbule', 'bulies', 'f', 'fe', 'fet', 'fets', 'fetis', 'fetise', 'fete', 'fetes', 'fetor', 'fels', 'felsite', 'felsites', 'felis', 'fele', 'fesels', 'fest', 'feste', 'fester', 'fer', 'ferberite', 'ferfet', 'ferfel', 'ferie', 'ferio', 'ferities', 'fere', 'feretories', 'feres', 'fermi', 'fermis', 'fermium', 'fermiums', 'fertil', 'fertilities', 'fertilise', 'fertiliser', 'fertile', 'ferter', 'ferlie', 'ferlies', 'feu', 'feute', 'feuter', 'feuterer', 'febrile', 'febris', 'febres', 'fei', 'feil', 'feis', 'feist', 'feists', 'feistiest', 'feistier', 'feirie', 'fm', 'fmt', 'fo', 'fot', 'fotui', 'fol', 'folie', 'folies', 'folio', 'foliot', 'foliole', 'foliolose', 'folios', 'foliose', 'folium', 'foliums', 'fole', 'fosie', 'fosite', 'foster', 'fosterite', 'fosterer', 'for', 'forb', 'forbesite', 'forbore', 'forbs', 'forfeit', 'forfeits', 'forfeiter', 'fore', 'foret', 'forel', 'forelimb', 'forelimbs', 'fores', 'foreset', 'forest', 'forests', 'forestries', 'forestful', 'forester', 'forerequest', 'form', 'forms', 'formulise', 'formuliser', 'formulism', 'formulist', 'formule', 'formful', 'formism', 'fort', 'forts', 'fortuities', 'fortuitism', 'fortuitist', 'forties', 'fortier', 'fortiori', 'fortis', 'forte', 'fortes', 'forlie', 'forlet', 'forlese', 'forleft', 'forleit', 'forlore', 'fou', 'foutre', 'foute', 'fouter', 'foul', 'fouls', 'foulest', 'fouler', 'fob', 'fobs', 'foiter', 'foil', 'foils', 'foiler', 'foism', 'foist', 'foists', 'foister', 'ft', 'fl', 'flrie', 'flu', 'flub', 'flubs', 'flue', 'flues', 'fluer', 'fluor', 'fluorite', 'fluorites', 'fluorosis', 'fluoroform', 'fluoborite', 'flutiest', 'flutier', 'flutist', 'flutists', 'flute', 'flutes', 'fluter', 'flb', 'flies', 'fliest', 'flier', 'flimsies', 'flimsiest', 'flimsier', 'flit', 'flits', 'flite', 'flites', 'flirt', 'flirts', 'flirtiest', 'flirtier', 'flirter', 'flet', 'flo', 'flot', 'flots', 'flote', 'floter', 'flor', 'florist', 'florists', 'floret', 'florets', 'floretum', 'flores', 'flout', 'flouts', 'flouter', 'flob', 'floit', 'fs', 'fsiest', 'fstore', 'fr', 'fries', 'friese', 'frieseite', 'frier', 'frim', 'frit', 'frits', 'fris', 'frise', 'frises', 'frist', 'frislet', 'fret', 'frets', 'fretum', 'fretful', 'freq', 'frere', 'freres', 'freit', 'freir', 'fro', 'frot', 'frost', 'frosts', 'frostiest', 'frostier', 'froster', 'frore', 'froufrou', 'froise', 'frt', 'fu', 'fub', 'fubs', 'fubsiest', 'fubsier', 'fuel', 'fuels', 'fueler', 'fuerte', 'fum', 'fumuli', 'fumble', 'fumbles', 'fumbler', 'fumiest', 'fumier', 'fumitories', 'fut', 'futilities', 'futile', 'fute', 'fulful', 'i', 'ie', 'im', 'imu', 'imbe', 'imbesel', 'imber', 'imberbe', 'imbrier', 'imbrium', 'imbu', 'imbue', 'imbues', 'imbute', 'imi', 'imit', 'io', 'iolite', 'iolites', 'ios', 'iou', 'iof', 'it', 'its', 'itself', 'itel', 'iter', 'ito', 'itoubou', 'itoism', 'itoist', 'il', 'ilium', 'ile', 'ilesite', 'ileum', 'ileitis', 'ilot', 'iq', 'iqs', 'is', 'isis', 'ise', 'iserite', 'iseum', 'ism', 'isms', 'iso', 'isoteles', 'isotere', 'isoseist', 'isoster', 'isosterism', 'isostere', 'isort', 'isoflor', 'ist', 'isl', 'isls', 'isle', 'islet', 'islets', 'isles', 'islot', 'ir', 'iritis', 'iritises', 'iris', 'irises', 'ire', 'ires', 'ireful', 'iroquois', 'e', 'et', 'etrier', 'etui', 'etuis', 'etiquet', 'etoile', 'etoiles', 'el', 'els', 'else', 'elses', 'elroquite', 'elute', 'elutes', 'elutor', 'elul', 'elb', 'elbert', 'elf', 'eli', 'eliot', 'elitism', 'elitisms', 'elitist', 'elitists', 'elite', 'elites', 'elisor', 'eleut', 'elm', 'elms', 'elmiest', 'elmier', 'eloise', 'eq', 'equities', 'equitist', 'equites', 'equisetum', 'equisetums', 'eques', 'es', 'ese', 'eses', 'esere', 'esoterism', 'esoterist', 'est', 'estriol', 'estriols', 'estre', 'ester', 'esteros', 'estoque', 'estoil', 'estoile', 'eslisor', 'esq', 'esquire', 'esquires', 'er', 'erf', 'erie', 'eris', 'ere', 'erer', 'ermit', 'erotism', 'erotisms', 'erotesis', 'eros', 'erose', 'eroses', 'eu', 'eumitosis', 'euosmite', 'euler', 'eblis', 'ebriose', 'ef', 'efoliose', 'eft', 'efts', 'eftest', 'efl', 'efs', 'eir', 'eire', 'm', 'mt', 'mts', 'mtier', 'ml', 'ms', 'mster', 'msl', 'mr', 'mu', 'mufti', 'muftis', 'muist', 'muir', 'muesli', 'mum', 'mums', 'mumbo', 'mumble', 'mumbles', 'mumbler', 'mut', 'muts', 'mutuel', 'mutuels', 'mutule', 'mutules', 'mutism', 'mutisms', 'mutist', 'mute', 'mutes', 'mutest', 'muter', 'mulse', 'mulier', 'mulierose', 'muliebrile', 'mulism', 'mule', 'mulet', 'mules', 'mulm', 'mulmul', 'mb', 'mbeuer', 'mbori', 'mf', 'mfr', 'mi', 'mim', 'mimble', 'mimi', 'mimir', 'miosis', 'mioses', 'mit', 'mitre', 'mitres', 'mitrer', 'mitu', 'mitiest', 'mitier', 'mitis', 'mitises', 'mite', 'mites', 'miter', 'miterer', 'mitosis', 'mitoses', 'mil', 'mils', 'milsie', 'milreis', 'milfoil', 'milfoils', 'milieu', 'miliolite', 'milit', 'milium', 'mile', 'miles', 'miler', 'milo', 'milos', 'milor', 'miquelet', 'miquelets', 'mis', 'misbelief', 'misbeliefs', 'misform', 'misforms', 'mise', 'mises', 'miser', 'miseries', 'miserism', 'misere', 'miserere', 'misereres', 'miso', 'misos', 'mist', 'mists', 'mistrist', 'mistutor', 'mistful', 'mistiest', 'mistier', 'mister', 'misterm', 'misterms', 'mislie', 'mislies', 'mislit', 'mislest', 'misquote', 'misquotes', 'misquoter', 'mir', 'miri', 'miriest', 'mirier', 'mire', 'mires', 'miro', 'o', 'ot', 'otiosities', 'otiose', 'otitis', 'otis', 'otium', 'oto', 'ototoi', 'otolite', 'otosis', 'ol', 'olio', 'olios', 'ole', 'oles', 'oleum', 'oleums', 'olm', 'ololiuqui', 'olor', 'oloroso', 'olof', 'os', 'osi', 'osier', 'osieries', 'osiris', 'osirism', 'ose', 'oses', 'osmite', 'osmium', 'osmiums', 'ostsis', 'ostsises', 'ostiole', 'ostioles', 'ostitis', 'ostium', 'osteitis', 'ostosis', 'ostosises', 'ostoses', 'oslo', 'or', 'orb', 'orblet', 'orbs', 'orf', 'orfe', 'oriel', 'oriels', 'oriole', 'orioles', 'ore', 'ores', 'orestes', 'oreilet', 'ort', 'orts', 'ortet', 'ortol', 'orl', 'orle', 'orlet', 'orles', 'orlo', 'orlos', 'oubliet', 'ouf', 'oui', 'ouistiti', 'ouistitis', 'out', 'outs', 'outsit', 'outsits', 'outset', 'outsets', 'outsert', 'outserts', 'outsmile', 'outsmiles', 'outsole', 'outsoles', 'outsoler', 'outstole', 'outstorm', 'outr', 'outre', 'outrelief', 'outbore', 'outblot', 'outform', 'outfort', 'outflue', 'outflies', 'outer', 'ob', 'obe', 'obeli', 'obelise', 'obelises', 'obelism', 'obelisms', 'obes', 'obesities', 'obese', 'obeism', 'obmit', 'obol', 'obols', 'oboli', 'obole', 'obolet', 'oboles', 'obolos', 'oboist', 'oboists', 'obtest', 'obtests', 'obl', 'obli', 'obliquities', 'oblique', 'obliques', 'obloquies', 'obs', 'obsequies', 'obsequium', 'obsoletism', 'obsolete', 'obsoletes', 'obstet', 'obstetrist', 'of', 'ofer', 'ofo', 'oft', 'oftest', 'ofter', 'oflete', 'oie', 'oil', 'oils', 'oiliest', 'oilier', 'oiler']


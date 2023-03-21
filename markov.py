"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path)
    text_string = contents.read()
    contents.close()
    return text_string

#print(open_and_read_file('green-eggs.txt'))


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    #turn argument into one long string with .read()
    #iterate through the long string 
        #for i in range(len(text) - 1):
        #print text[i], text[i + 1]
    #put pairs (via index) into the return variable chains
    #sentence: "Good morning, how are you doing?"

    #(words[i], words[i + 1]...words[i + 1], words[i + 2])
    #('Would', 'you'): ['could', 'could', 'could', 'could', 'like', 'like'],

    #######
    # pick a random starting point
    # choose random next word (value in current key)
    # make new key, choose next word
    # append words into return variable

    chains = {}
    words = text_string.split()

    for i in range(len(words) - 2): #set up a for loop; key values reassigned w/ every step of the loop
        key = (words[i], words[i + 1])
        value = words[i + 2]
        if key not in chains: #check if the key exists, if not - add the key to dict. 
            chains[key] = []
        chains[key].append(value) #appends value to the key
       
    return chains

def make_text(chains):
    """Return text from chains."""

    words = [] #this is our accumulator
    first_key = choice(list(chains.keys())) #this converts tuple to list (this becomes indexable)
    word1, word2 = first_key #reset first_key to tuple based on words1 and words 1; 
    word3 = choice(chains[first_key]) #word1 will equal the first chain dictionary value, word 2 will equal the second chain dict value
    
    while True:
        words.append(word1) #this is where we assign the values of the word variables on line 78
        word1 = word2
        word2 = word3

        if (word1,word2) in chains: #if this key is here, we can keep adding... if true, keep adding to the string
            word3 = choice(chains[(word1, word2)])
        else:
            words.extend([word1,word2])
            return ' '.join(words)

    


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
print(chains)

# Produce random text
random_text = make_text(chains)

print(random_text)




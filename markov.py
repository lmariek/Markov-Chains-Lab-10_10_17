"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as suess_text:
        text_string = suess_text.read()
        

    return text_string

print open_and_read_file("green-eggs.txt")


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words_list = text_string.split()

    for i in range(len(words_list)-2):

        key = (words_list[i], words_list[i+1])
        value = words_list[i + 2]

        chains[key] = chains.get(key, [])
        chains[key].append(value)

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    #creating a list of all keys from the chains dictionary
    all_keys = chains.keys()
    #choosing a random key, using the choice() module
    key = choice(all_keys)

    #appending the first word of the key tuple to the 'words' list
    words.append(key[0])


    while True:
        #if the key exists in the chains dictionary
        if key in chains:
            #create a new link (tuple)
            new_key = (key[1], choice(chains[key]))
            #append the link to the 'words' list
            words.append(new_key[1])
            #rebind key to the new link
            key = new_key

        else:
            break
    #return the list of links as a string
    return " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text

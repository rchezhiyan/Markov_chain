"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    line = open(file_path).read()


    return line


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
    text_string = text_string.split()
    chains = {}

    n = len(text_string)

    for i in range(n-2):
        #print(text_string[i])
        k = tuple()
        k = (text_string[i], text_string[i+1])

        if k in chains:

            chains[k].extend([text_string[i+2]])

        else:
            chains[k] = [text_string[i+2]]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # new_key = choice(list(chains))

    chain = True
    First_key = choice(list(chains))
    new_key = First_key
    words.append(new_key[0])
    words.append(new_key[1])
    ran_val = choice(chains[new_key])
    words.append(ran_val)
    next_key = words[-2::]

    # words = [word1, word2, word3]

    # next_key = [(word2, word3)]

    while chain:

        new_key = tuple(next_key)
        #print(new_key)
        if new_key in chains:
            ran_val = choice(chains[new_key])
        else:
            chain = False
            break
        #print(ran_val)
        words.append(ran_val)
        next_key = words[-2::]
        #print(next_key)
    
    return  ' '.join(words)


input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
#print(chains)
# Produce random text
random_text = make_text(chains)

print(random_text)

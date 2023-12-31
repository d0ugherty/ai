"""This program generates random text in the style of a 
given sample using ngrams.

Original Python 2 version by Nathan Sprague at JMU
Updated to Python 3 and assignment modifications by Jennifer Kay at Rowan 
"""


import random
import string

def textToList(textFilePath):
    """ Converts textFilePath  to a list of words.  All
    Removes all punctuation and converts everything to
    lower-case.

    Argument:
        textFilePath - The path to the file.
    Returns
        A list of all the words in the file.
    """
    with open(textFilePath, 'r') as handle:
        text = handle.read().lower()
    text = text.translate(
        str.maketrans(string.punctuation,
                         " " * len(string.punctuation)))
    return text.split()

def selectRandomItem(distributionDictionary):
    """
    Select an item from the the probability distribution
    represented by the provided dictionary.

    Example:
    >>> selectRandomItem({'a':.9, 'b':.1})
    'a'
    """

    # Make sure that the probabilities add up to something pretty close to 1.
    assert abs(sum(distributionDictionary.values()) - 1.0) < .00001, \
        "Probability distribution does not add up to 1!"

    r = random.random()
    totalSum = 0
    for item in distributionDictionary:
        totalSum += distributionDictionary[item]
        if r < totalSum:
            return item

    #If we get here something is wrong!!!
    assert False, "Error in selectRandomItem!"


def countsToProbs(countsDict):
    """ Convert a dictionary of word counts to a dictionary of probabilities.

    Argument:
       countsDict - a dictionary map from words to ints

    Returns:
       A new dictionary where each of the counts has been divided by the sum
       of all the entries in countsDict.

    Example:

    >>> countsToProbs({'a':8, 'b':2})
    {'a': 0.8, 'b': 0.2}

    """
    probabilityDict = {}
    totalSum = 0
    for item in countsDict:
        totalSum += countsDict[item]
    for item in countsDict:
        probabilityDict[item] = countsDict[item] / float(totalSum)
    return probabilityDict


def computeUnigramProbs(word_list):

    unigrams = {}
    for word in word_list:
        if word not in unigrams:
            unigrams[word] = 0
        
        unigrams[word] += 1
        
    return countsToProbs(unigrams)


def generateRandomUnigramSequence(unigrams, num_words):

    result = ""
    for i in range(num_words):
        next_word = selectRandomItem(unigrams)
        result += next_word + " "
    return result.rstrip()


def computeBigramProbs(word_list):

    bigram_counts = {}
    bigram_prob = {}

    for i, word in enumerate(word_list):
        
        if i + 1 < len(word_list):

            next_word = word_list[i + 1]
            if word not in bigram_counts:
                bigram_counts[word] = {}
            if next_word not in bigram_counts[word]:
                bigram_counts[word][next_word] = 0
            bigram_counts[word][next_word] += 1

        bigram_prob[word] = countsToProbs(bigram_counts[word])

    return bigram_prob


def computeTrigramProbs(word_list):
    """Calculates, for each adjacent pair of words in the list, the
    probability distribution over possible subsequent words.

    The returned dictionary maps from two-word tuples to dictionaries
    that represent probability distributions over subsequent
    words.

    Example:

    >>> b = computeTrigramProbs(['i', 'think', 'therefore', 'i', 'am',\
                                'i', 'think', 'i', 'think'])
    >>> print b
    {('think', 'i'): {'think': 1.0},
    ('i', 'am'): {'i': 1.0},
    (None, None): {'i': 1.0},
    ('therefore', 'i'): {'am': 1.0},
    ('think', 'therefore'): {'i': 1.0},
    ('i', 'think'): {'i': 0.5, 'therefore': 0.5},
    (None, 'i'): {'think': 1.0},
    ('am', 'i'): {'think': 1.0}}
    """
    # YOUR CODE HERE
    pass

def generateRandomBigramSequence(first_word, bigrams, num_words):
    
    result = first_word + " "
    curr_word = first_word

    print(bigrams[curr_word])

    for i in range(num_words):
        next_word = selectRandomItem(bigrams[curr_word])
        result += next_word + " "
        curr_word = next_word
        
    return result.rstrip()



def generateRandomTrigramSequence(first_word, second_word, bigrams, trigrams, num_words):
    """Generate a random sequence of words according to the provided
    bigram and trigram distributions.

    By default, each new word will be generated using the trigram
    distribution.  The bigram distribution will be used when a
    particular word pair does not have a corresponding trigram.

    Arguments:
       first_word -          The first word in the generated text.
       second_word -         The second word in the generated text.
       bigrams -             bigram probabilities (as returned by the
                             computeBigramProbs function).
       trigrams -            trigram probabilities (as returned by the
                             computeBigramProbs function).
       num_words -           The number of words of random text to generate.

    Returns:
       The random string of words with each subsequent word separated by a
       single space.

    """
    # YOUR CODE HERE
    pass

def goUnigrams():
    """ Generate text from Alice in Wonderland unigrams."""
    words = textToList('alice.txt')
    unigrams = computeUnigramProbs(words)
    print (generateRandomUnigramSequence(unigrams, 100))

def goBigrams():
    """ Generate text from Alice in Wonderland bigrams."""
    words = textToList('alice.txt')
    bigrams = computeBigramProbs(words)
    print (generateRandomBigramSequence('the', bigrams, 100))

def goTrigrams():
    """ Generate text from Alice in Wonderland trigrams."""
    words = textToList('alice.txt')
    bigramProbs = computeBigramProbs(words)
    trigramProbs = computeTrigramProbs(words)
    print (generateRandomTrigramSequence('there', 'are', bigramProbs, trigramProbs, 100))


if __name__ == "__main__":
    # You can insert testing code here, or switch out the main method
    # to try bigrams or trigrams. 

    bigrams = computeBigramProbs(['i', 'think', 'therefore', 'i', 'am',\
                               'i', 'think', 'i', 'think'])
    
    print(generateRandomBigramSequence('think', bigrams, 5))
    #goUnigrams()

import nltk
from nltk.collocations import *
import string


def cleanData(jobDesc):
    words = nltk.tokenize.word_tokenize(jobDesc)  # tokenize

    # remove punctuation
    table = str.maketrans('', '', string.punctuation)  # strips commas from end of words
    stripped = [word.translate(table) for word in words]
    words = [word for word in stripped if word.isalpha()]  # removes standalone punctuation and numbers
    wordDist = nltk.FreqDist(word.lower() for word in words)

    # remove stop words and irrelevant words
    stopWords = nltk.corpus.stopwords.words('english')
    # this list is compiled manually to get rid of obviously common words that don't contribute to a potential desirable skills list
    irrelevant = ["experience", "software", "systems", "engineering", "work", "team", "job", "system", "requirements",
                  "new", "skills", "engineer", "computer", "us", "required", "ability", "support", "develop", "development",
                  "must", "engineers", "knowledge", "degree", "years", "world", "including", "related", "position",
                  "employer", "products", "status", "responsibilities", "role", "opportunity", "employees", "company",
                  "may", "equal", "disability", "looking", "make", "employment", "national", "qualifications"]
    for word in irrelevant:
        stopWords.append(word)
    filteredWords = nltk.FreqDist(word.lower() for word in words if word.lower() not in stopWords)

    return filteredWords


# TODO: bigrams and trigrams only ever appear once because every post is written uniquely, try to find a way to rank freq regardless of word order
def bigrams_and_trigrams(filteredWords):
    # individual words
    solograms = filteredWords.most_common(30)

    # bigrams
    findBigrams = nltk.bigrams(filteredWords)
    bigrams = (nltk.FreqDist(findBigrams)).most_common(30)

    # trigrams
    findTrigrams = nltk.trigrams(filteredWords)
    trigrams = (nltk.FreqDist(findTrigrams)).most_common(30)

    return solograms, bigrams, trigrams


# DRIVER CODE
jobDesc = open("Job Descriptions.txt").read()
filteredWords = cleanData(jobDesc)

solo, bi, tri = bigrams_and_trigrams(filteredWords)
print("individual words: ", solo)
print("bigrams: ", bi)
print("trigrams: ", tri)

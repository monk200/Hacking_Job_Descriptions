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
                  "may", "equal", "disability", "looking", "make", "employment", "national", "qualifications", "customers",
                  "general", "help", "life", "bachelor", "etc", "benefits", "applicants", "gender", "customer", "level",
                  "using", "industry", "protected", "part", "provide", "preferred", "tasks", "apply", "join", "andor",
                  "identity", "individuals", "one", "qualified", "travel", "product", "global", "insurance", "include",
                  "future", "race", "religion", "sexual", "orientation", "people", "quality", "meet", "government",
                  "without", "opportunities", "best", "medical", "age", "use", "please", "duties", "veteran", "every",
                  "specific", "implement", "perform", "next", "responsible", "procedures", "across", "employee",
                  "able", "capabilities", "bring", "candidates", "regard", "based", "closely", "sex", "diverse", "professional",
                  "like", "specifications", "familiarity", "day", "candidate", "excellent", "area", "learn", "also",
                  "processes", "clearance", "diversity", "want", "access", "background", "standard", "minimum", "need",
                  "aurora", "strong", "field", "understanding", "good", "tests", "impact", "committed", "ensure",
                  "university", "plus", "health", "bs", "understand", "multiple", "business"]
    for word in irrelevant:
        stopWords.append(word)
    filteredWords = nltk.FreqDist(word.lower() for word in words if word.lower() not in stopWords)

    return filteredWords


def bigrams_and_trigrams(filteredWords):
    # individual words
    solograms = filteredWords.most_common(100)

    # bigrams
    # these two lines will return the 30 most common bigrams, preserving their order
    #findBigrams = nltk.bigrams(filteredWords)
    #bigrams = (nltk.FreqDist(findBigrams)).most_common(30)

    # these lines will return a sorted list of the most common bigrams, disregarding their order
    findBigrams = list(nltk.bigrams(filteredWords))
    foundList = []
    bigrams = []
    # loop through list of discovered bigrams
    for i in range(0, len(findBigrams)):
        # no need to look for duplicates if we've already found this combination
        if findBigrams[i] in foundList:
            continue;
        count = 1

        for j in range(i+1, len(findBigrams)):      # look through and compare to other bigrams
            # find when same tokens or when swapped tokens
            if ((findBigrams[i][0] == findBigrams[j][0]) and (findBigrams[i][1] == findBigrams[j][1]))\
                    or ((findBigrams[i][0] == findBigrams[j][1]) and (findBigrams[i][1] == findBigrams[j][0])):
                count += 1
                foundList.append(findBigrams[j])       # add to foundList because we don't want to have duplicates in final list

        bigrams.append((findBigrams[i], count))

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

# create text for word cloud from solo
wordCloud = open(r'individual_words.txt','w')
for word, count in solo:
    for i in range(0, count):
        wordCloud.write(word + " ")
wordCloud.close()

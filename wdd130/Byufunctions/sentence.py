import random



def main():
    
    sentence = make_sentence()


    return sentence
    
    
    
    
    

def make_sentence():
    
    words = get_determiner(quantity=1)
    noun = get_noun(quantity=1)
    verbs = get_verb(quantity=1, tense = "past")
    preposition = get_preposition()
    prepositional_phrase = get_prepositional_phrase(quantity= 1) 
    adverb = get_adverb()
    print(f"{words.capitalize()} {noun} {verbs} {preposition} {prepositional_phrase} {adverb}")

    words = get_determiner(quantity=1)
    noun = get_noun(quantity=1)
    verbs = get_verb(quantity=1, tense = "present")
    preposition = get_preposition()
    prepositional_phrase = get_prepositional_phrase(quantity= 1) 
    adverb = get_adverb()
    print(f"{words.capitalize()} {noun} {verbs} {preposition} {prepositional_phrase} {adverb}")

    words = get_determiner(quantity=1)
    noun = get_noun(quantity=1)
    verbs = get_verb(quantity=1, tense="future")
    preposition = get_preposition()
    prepositional_phrase = get_prepositional_phrase(quantity= 1) 
    adverb = get_adverb()
    print(f"{words.capitalize()} {noun} {verbs} {preposition} {prepositional_phrase} {adverb}")

    words = get_determiner(quantity=0)
    noun = get_noun(quantity=0)
    verbs = get_verb(quantity=0, tense = "past")
    preposition = get_preposition()
    prepositional_phrase = get_prepositional_phrase(quantity= 0) 
    adverb = get_adverb()
    print(f"{words.capitalize()} {noun} {verbs} {preposition} {prepositional_phrase} {adverb}")

    words = get_determiner(quantity=0)
    noun = get_noun(quantity=0)
    verbs = get_verb(quantity=0,tense ="present")
    preposition = get_preposition()
    prepositional_phrase = get_prepositional_phrase(quantity= 0) 
    adverb = get_adverb()
    print(f"{words.capitalize()} {noun} {verbs} {preposition} {prepositional_phrase} {adverb}")

    words = get_determiner(quantity=0)
    noun = get_noun(quantity=0)
    verbs = get_verb(quantity=0, tense = "future")
    preposition = get_preposition()
    prepositional_phrase = get_prepositional_phrase(quantity= 0) 
    adverb = get_adverb()
    print(f"{words.capitalize()} {noun} {verbs} {preposition} {prepositional_phrase} {adverb}")
    

    

def get_determiner(quantity):
   
  
  if quantity == 1:
      words = ["a", "one", "the"]
  if quantity == 0:
      words = ["some", "many", "the"]
  
  word = random.choice(words)
  
  return word

def get_noun(quantity):

    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
      "dog", "girl", "man", "rabbit", "woman"]
    if quantity == 0: 
        nouns = ["birds", "boys", "cars", "cats", "children",
      "dogs", "girls", "men", "rabbits", "women"]


    nouns = random.choice(nouns)

    return(nouns)

def get_verb(quantity, tense):
    
    
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
      "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
      "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
      "will think", "will run", "will sleep", "will talk",
      "will walk", "will write"]
    
    verbs = random.choice(verbs)
    return(verbs)
def get_preposition():
    preposition = ["about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"]  

    preposition = random.choice(preposition)
    return preposition
def get_prepositional_phrase(quantity):
    
    if quantity == 1:
      prepositional_phrase = ["the car", "one child", "the toy", "a rabbit", "one dog", "a cat", "the house", "a country"]
    else:
      prepositional_phrase = ["the cars", "some childrens", "the toys", "many rabbits", "many dogs", "some cats", "The houses", "some countries"]

    prepositional_phrase = random.choice(prepositional_phrase)

    return prepositional_phrase

def get_adverb():
    adverb = ["around", "here", "Above", "there", "inside", "outside", "between", "over", "enough", "often", "sometimes", "normally", "out"]
    adverb = random.choice(adverb)
    return adverb



main()
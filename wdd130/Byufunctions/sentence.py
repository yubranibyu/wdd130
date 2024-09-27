import random



def main():
    
    sentence = make_sentence()


    return sentence
    
    
    
    
    

def make_sentence():
    
    words = get_determiner(quantity=1)
    noun = get_noun(quantity=1)
    verbs = get_verb(quantity=1, tense = "past")
    print(f"{words.capitalize()} {noun} {verbs}")

    words = get_determiner(quantity=1)
    noun = get_noun(quantity=1)
    verbs = get_verb(quantity=1, tense = "present")
    print(f"{words.capitalize()} {noun} {verbs}")

    words = get_determiner(quantity=1)
    noun = get_noun(quantity=1)
    verbs = get_verb(quantity=1, tense="future")
    print(f"{words.capitalize()} {noun} {verbs}")

    words = get_determiner(quantity=0)
    noun = get_noun(quantity=0)
    verbs = get_verb(quantity=0, tense = "past")
    print(f"{words.capitalize()} {noun} {verbs}")

    words = get_determiner(quantity=0)
    noun = get_noun(quantity=0)
    verbs = get_verb(quantity=0,tense ="present")
    print(f"{words.capitalize()} {noun} {verbs}")

    words = get_determiner(quantity=0)
    noun = get_noun(quantity=0)
    verbs = get_verb(quantity=0, tense = "future")
    print(f"{words.capitalize()} {noun} {verbs}")
    

    

def get_determiner(quantity):
   
  
  if quantity == 1:
      words = ["a", "one", "the"]
  if quantity == 0:
      words = ["some", "many", "the"]
  # Randomly choose and return a determiner.
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



main()
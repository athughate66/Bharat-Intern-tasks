#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk
from nltk.corpus import wordnet

def correct_or_nearest_word(word):
  """Returns the correct or nearest word to the given word.

  Args:
    word: The word to be corrected or found the nearest word to.

  Returns:
    The correct or nearest word to the given word.
  """

  synsets = wordnet.synsets(word)
  if len(synsets) == 0:
    return None
  else:
    most_similar_synset = synsets[0]
    for synset in synsets:
      if synset.wup_similarity(most_similar_synset) > 0.9:
        most_similar_synset = synset
    return most_similar_synset.name()

def main():
  """Prints the correct or nearest word to the given word."""

  word = input("Enter a word: ")
  corrected_word = correct_or_nearest_word(word)
  if corrected_word is None:
    print("The word {} does not exist.".format(word))
  else:
    print("The correct or nearest word to {} is {}.".format(word, corrected_word))

if __name__ == "__main__":
  main()


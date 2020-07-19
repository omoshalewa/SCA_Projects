# the function anagram will identify if words contain the same letter

def anagram(word, word_list):
# the variable sorted_word holds the function sorted() which sorts the word whose anagrams we need
    sorted_word = sorted(word)
# ana_gram is a container that holds words with identical letters
    ana_gram = []
# 'words' represent words in word_list
# this loop ensures all the words in word_list are checked to know if they are anagrams to sorted_word
    for words in word_list:
        if sorted_word == sorted(words):
# to add anagrams to the container(list) created
            ana_gram.append(words)
    return ana_gram


print(anagram('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagram('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagram('laser', ['lazing', 'lazy', 'lacer']))


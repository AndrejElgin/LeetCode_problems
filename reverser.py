
"""code reverses each letter in a string"""
from re import A
import string


sentence_for_reversing = input("give your string ")

def sentence_reverser(sentence):
    words = sentence.split(" ")
    a = []
    for word in words:
        a.append(word_reverser(word))
    return " ".join(a)
       
    
def word_reverser(word):
    letters = list(word)
    word = "".join(letters[::-1])
    return word

print(sentence_reverser(sentence_for_reversing))
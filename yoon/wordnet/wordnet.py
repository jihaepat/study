import sys
from termcolor import colored, cprint
from nltk.corpus import wordnet

text = colored('========================', 'green')
text_pint = colored(':', 'red',attrs=['blink','bold'])
print(text)
print(wordnet.synsets('lunch'))

lunch_n = wordnet.synsets('lunch')[0]
print(lunch_n)

print('lunch_n.examples 예시', text_pint, lunch_n.examples())

print('lunch_n.part_meronyms 부분어', text_pint, lunch_n.part_meronyms())

lunch_v1 = wordnet.synsets('lunch')[1]
print('wordnet.synsets(lunch)[1]', text_pint, lunch_v1)

print(dir(lunch_n))

print('lunch_n.hyponyms 하의어', text_pint, lunch_n.hyponyms())

print('lunch_n.hypernyms 상의어', text_pint,  lunch_n.hypernyms())

print(lunch_n.hypernyms()[0].hyponyms())

for s in wordnet.synsets('eye'):
    print(s, s.definition())

eye = wordnet.synsets('eye')[0]
print('eye.part_meronyms 부분어', text_pint, eye.part_meronyms())
print(text)
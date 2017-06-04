import sys
import os
from time import time
from random import randint
sys.path.append(os.path.join(os.path.dirname(__file__), 'binary_search_tree-master', 'binary_search_tree-master'))

from linkedbst import LinkedBST

with open("words.txt", "r") as file:
    words = [line.replace("\n", "") for line in file.readlines()]

words.sort()
numbers = [randint(0, len(words) - 1) for _ in range(10000)]
seeking_words = [words[n] for n in numbers]

words_tree = LinkedBST(words)
words_tree.rebalance()

words_list = words

list1 = list()
list2 = list()
print("searching 10000 words in 967 words...")

time1 = time()
for word in seeking_words:
    if word in words_list:
        list1.append(word)
t1 = time() - time1
print("searching in list takes: ", t1)

time2 = time()
for word in seeking_words:
    list2.append(words_tree.find(word))
t2 = time() - time2
print("searching in BST takes: ", t2)
print("total difference: {}ms".format(t1 - t2))

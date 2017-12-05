# Patrick Eddy
# TCSS 435
# Programming Assignment 3

from collections import deque
from random import randint
import re
import json
import os.path


class BookGen():
    """Generate books by training with other books."""

    def __init__(self, save_training_data=False, skip_training_if_saved=False):
        self.save_filename = 'training_data.txt'
        self.save_training_data = save_training_data
        self.skip_training = skip_training_if_saved

    def train(self, book):
        """Trains the generator using the book string."""
        self.main_hash = {}

        if self.skip_training and os.path.exists(self.save_filename): # skip training if specified
            return

        split_book = deque(re.split(r"\s", book))
        if (len(split_book) > 3):
            first_w = self.__get_valid_next_word(split_book)
            second_w = self.__get_valid_next_word(split_book)

            while (len(split_book) > 3):
                third_w = self.__get_valid_next_word(split_book)
                self.__add_word(thehash=self.main_hash, words=[first_w, second_w, third_w]) # add those words
                first_w = second_w
                second_w = third_w

        if self.save_training_data:
            f = open(self.save_filename, 'wb')
            f.write(json.dumps(self.main_hash))
            f.close

    def generate(self, num_words):
        """Generates a book of variable length."""

        if self.save_training_data:
            data = open(self.save_filename, 'r').read()
            self.main_hash = json.loads(data)

        first_word = self.__random_word(self.main_hash)
        second_word = self.__random_word(self.main_hash[first_word]) if self.main_hash[first_word] else self.__random_word(self.main_hash)
        new_book = first_word + " " + second_word

        while num_words > 0:
            third_word = self.__generate_word(first_word, second_word)
            first_word = second_word
            second_word = third_word

            new_book += " " + third_word
            num_words -= 1

        return new_book

    def __get_valid_next_word(self, split_text):
        word = ''
        while word == '' and len(split_text) > 0:
            word = split_text.popleft()
        return word.lower()

    def __add_word(self, thehash, words):
        self.__rec_add(thehash, words)

    def __rec_add(self, hashref, words):
        if len(words) == 1:
            hashref[words[0]] = hashref[words[0]] + 1 if words[0] in hashref.keys() else 1
            return 
        hashref[words[0]] = hashref[words[0]] if words[0] in hashref.keys() else {} # init if necessary
        self.__rec_add(hashref[words[0]], words[1:3])

    def __random_word(self, hash):
        random_hash_index = lambda keys: randint(0, len(keys)-1)
        return hash.keys()[random_hash_index(hash.keys())]

    def __generate_word(self, first_word, second_word):
        new_word = self.__random_word(self.main_hash) # default to a random word from the main list

        if second_word in self.main_hash[first_word].keys():
            if len(self.main_hash[first_word][second_word]) > 0:
                prob_list = [] # generate a list with proportional probablities
                for key in self.main_hash[first_word][second_word].keys():
                    prob_list.append(key)

                new_word = prob_list[randint(0, len(prob_list)-1)] # randomly select from prob list

        return new_word

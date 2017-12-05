from collections import deque
from random import randint
import re
import json

class BookGen():
    """Generate books by training with other books."""

    def __init__(self, save_training_data=False):
        self.main_hash = {}
        self.save_training_data = save_training_data

    def train(self, book):
        """Trains the generator using the book string."""
        split_book = deque(re.split(r"\s", book))
        if (len(split_book) > 3):
            first_w = self.__get_valid_next_word(split_book)
            second_w = self.__get_valid_next_word(split_book)

            while (len(split_book) > 3):
                third_w = self.__get_valid_next_word(split_book)
                self.__add_word([first_w, second_w, third_w], self.main_hash) # add those words
                first_w = second_w
                second_w = third_w

        if self.save_training_data:
            f = open('training_data.txt', 'wb')
            f.write(json.dumps(self.main_hash))
            f.close

    def generate(self, num_words):
        """Generates a book of variable length."""

        if self.save_training_data:
            data = open('training_data.txt', 'r').read()
            self.main_hash = json.loads(data)

        first_word = self.__random_word(self.main_hash)
        second_word = self.__random_word(self.main_hash[first_word]) if self.main_hash[first_word] else self.__random_word(self.main_hash)
        new_book = first_word + " " + second_word

        while num_words > 0:
            new_book += " " + self.__generate_word(first_word, second_word)
            num_words -= 1

        return new_book

    def __get_valid_next_word(self, split_text):
        # print(len(split_text))
        word = ''
        while word == '' and len(split_text) > 0:
            word = split_text.popleft()
        return word.lower()

    def __add_word(self, words, hash):
        if words[0] in hash.keys():
            if words[1] in hash[words[0]].keys():
                if words[2] in hash[words[0]][words[1]].keys():
                    hash[words[0]][words[1]][words[2]] += 1
                else: 
                    hash[words[0]][words[1]][words[2]] = 1
            else:
                hash[words[0]][words[1]] = {}
        else:
            hash[words[0]] = {}

    def __random_word(self, hash):
        random_hash_index = lambda keys: randint(0, len(keys)-1)
        return hash.keys()[random_hash_index(hash.keys())]

    def __generate_word(self, first_word, second_word):
        new_word = self.__random_word(self.main_hash) # default to a random word from the main list

        if second_word in self.main_hash[first_word].keys():
            if len(self.main_hash[first_word][second_word]) > 0:
                prob_list = [] # generate a list with proportional probablities
                for key in self.main_hash[first_word][second_word].keys() and key != second_word: 
                    prob_list.append(key)

                new_word = prob_list[randint(0, len(prob_list)-1)] if len(prob_list) > 0 else new_word # randomly select from prob list

        return new_word




# Patrick Eddy
# TCSS 435
# Programming Assignment 3

from bookgen import BookGen
from datetime import datetime

def get_book(filename):
    print("Reading " + str(filename) + "...")
    f = open("books/" + str(filename), "r")
    b = f.read()
    f.close()
    return b

def gen_book(bookgen, num_words, name='book'):
    print("Generating book...\n")
    book = bookgen.generate(num_words)
    print(book + '\n')
    f = open('generated/' + str(name) + '_' + str(datetime.utcnow()) + '.txt', 'w')
    f.write(book)
    f.close()

def main():
    book_files = {
        'alice': ['alice-27.txt'],
        'doyle': ['doyle-27.txt', 'doyle-case-27.txt'],
        'london': ['london-call-27.txt'],
        'melville': ['melville-billy-27.txt'],
        'twain': ['twain-adventures-27.txt']
    }
    bookgen = BookGen(save_training_data=False, skip_training_if_saved=False)
    train = lambda book: bookgen.train(get_book(book))

    print("Training with all books...")
    all_values = lambda bfs: reduce(lambda prev, curr: prev + curr, bfs.values())
    map(train, all_values(book_files))
    gen_book(bookgen=bookgen, num_words=1000, name='all')

    # # train multiple categories    
    # print("Training with multiple categories...")
    # get_filenames_merged = lambda bfs: reduce(lambda prev, curr: prev + book_files[curr], bfs, [])
    # map(train, get_filenames_merged(['doyle', 'london']))
    # gen_book(bookgen=bookgen, num_words=1000, 'doyle_london')

    # train one category
    print("Training with Sherlock books...")
    map(train, book_files['doyle'])
    gen_book(bookgen=bookgen, num_words=1000, name='sherlock')

if __name__ == '__main__':
    main()

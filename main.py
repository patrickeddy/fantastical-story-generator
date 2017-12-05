# Patrick Eddy
# TCSS 435
# Programming Assignment 3

# Steps
# 1. Read in words, and give them to the trainer
# 2. Trainer creates a hash table filled with linked lists
#    where every third node has a freq count.
# 3. Trainer spits out a new book, and hands it over to readwrite that writes
#    the new book to a file.

from bookgen import BookGen

def get_book(filename):
    print("Reading " + str(filename))
    f = open("books/" + str(filename), "r")
    b = f.read()
    f.close()
    return b

# Main method
def main():
    book_files = {
        'alice': ['alice-27.txt'],
        'doyle': ['doyle-27.txt'],
        'doyle2': ['doyle-case-27.txt'],
        'london': ['london-call-27.txt'],
        'melville': ['melville-billy-27.txt'],
        'twain': ['twain-adventures-27.txt']
    }
    bookgen = BookGen(save_training_data=True)

    print("Training BookGen...")
    train = lambda book: bookgen.train(get_book(book))
    all_values = lambda bfs: reduce(lambda prev, curr: prev + curr, bfs.values())
    map(train, all_values(book_files)) # train
    print("Training done.")

    print("Generating book...")
    print(bookgen.generate(1000)) # generate a book

if __name__ == '__main__':
    main()

# Patrick Eddy
# TCSS 435
# Programming Assignment 3

from bookgen import BookGen

def get_book(filename):
    print("Reading " + str(filename) + "...")
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
    bookgen = BookGen(save_training_data=True, skip_training_if_saved=True)

    print("Training BookGen...")
    train = lambda book: bookgen.train(get_book(book))
    
    # train all books
    # all_values = lambda bfs: reduce(lambda prev, curr: prev + curr, bfs.values())
    # map(train, all_values(book_files))

    # train some books
    get_filenames_merged = lambda bfs: reduce(lambda prev, curr: prev + book_files[curr], bfs, [])
    print(get_filenames_merged(['doyle', 'doyle2']))
    map(train, get_filenames_merged(['doyle', 'doyle2']))

    # train just one book
    # map(train, book_files['doyle'])
    
    print("Training done.")

    print("Generating book...\n")
    print(bookgen.generate(num_words=1000))

if __name__ == '__main__':
    main()

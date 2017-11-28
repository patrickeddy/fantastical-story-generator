# Patrick Eddy
# TCSS 435
# Programming Assignment 3

import linkedlist as ll

sentence = "Pie is fantastic on Friday evenings."
words = sentence.split(' ')

root = ll.make_list(words[0])

curr = root
for w in words[1:]:
    next = ll.append_to(curr, w)
    curr = next

curr = root
while (curr != None):
    print(curr['word'])
    curr = curr['next']

print('Get node relative: ' + str(ll.get_node_relative(root['next']['next'], -1)['word']))

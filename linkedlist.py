def make_node(prev, word, next = None):
    return {
        'prev': prev,
        'word': word,
        'next': next
    }

def get_node_relative(node, vector):
    curr = node
    i = vector
    sign = lambda a: (a>0) - (a<0)
    while (sign(i) == sign(vector)) and i != 0:
        if i < 0:
            curr = curr['prev']
        elif i > 0:
            curr = curr['next']
        i += -sign(vector) # makes closer to zero
    return curr

def append_to(node, word):
    n = make_node(node, word, node['next'])
    node['next'] = n
    return n

def make_list(word):
    return make_node(None, word)

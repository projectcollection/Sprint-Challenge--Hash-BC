#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length*2)

    """
    YOUR CODE HERE
    """
    for weight in weights:
        hash_table_insert(ht, weight, weight)
    
    for weight in weights:
        a = hash_table_retrieve(ht, weight)
        complement_key = limit-weight
        b = hash_table_retrieve(ht, complement_key)
        if a is not None and b is not None:
            idx_a = weights.index(a)
            weights[idx_a] = -1
            idx_b = weights.index(b)
            return (idx_b, idx_a) if a <= b else (idx_a, idx_b)
            
        else:
            hash_table_insert(ht, weight, weight)

    return None


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
